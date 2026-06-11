from sqlalchemy.orm import Session

from src.chains.rag_chain import (rag_message_chain)
from src.chains.rag_chain import (rag_stream_chain)

from src.services.token_service import (save_token_usage)

from src.services.chat_history_service import (
    save_message,
    get_chat_history,
    format_chat_history
)

from src.services.cache_service import (
    get_cached_response,
    set_cached_response
)

from src.core.logger import logger


async def ask_question(
    db: Session,
    user_id: int,
    question: str
):

    save_message(
        db,
        user_id,
        "user",
        question
    )

    cached_answer = get_cached_response(
        question
    )

    if cached_answer:

        save_message(
            db,
            user_id,
            "assistant",
            cached_answer
        )

        logger.info(
            f"Cache HIT user_id={user_id}"
        )

        return cached_answer

    messages = get_chat_history(
        db,
        user_id
    )

    history = format_chat_history(
        messages
    )

    logger.info(
        f"Cache MISS user_id={user_id}"
    )

    logger.info(
        f"Chat request user_id={user_id}"
    )

    response = await rag_message_chain.ainvoke(
        {
            "question": question,
            "history": history
        }
    )

    save_token_usage(
        db=db,
        user_id=user_id,
        usage=response.usage_metadata
    )

    answer = response.text

    set_cached_response(
        question,
        answer
    )

    save_message(
        db,
        user_id,
        "assistant",
        answer
    )

    logger.info(
        f"Chat completed user_id={user_id}"
    )

    return answer


async def stream_answer(
    db: Session,
    user_id: int,
    question: str
):

    save_message(
        db,
        user_id,
        "user",
        question
    )

    messages = get_chat_history(
        db,
        user_id
    )

    history = format_chat_history(
        messages
    )

    full_answer = ""

    async for chunk in rag_stream_chain.astream(
        {
            "question": question,
            "history": history
        }
    ):

        if chunk.content and len(chunk.content) > 0:

            text = chunk.content[0].get(
                "text",
                ""
            )

            full_answer += text

            yield f"data: {text}\n\n"

    save_message(
        db,
        user_id,
        "assistant",
        full_answer
    )