from sqlalchemy.orm import Session

from src.chains.rag_chain import rag_chain

from src.services.chat_history_service import (
    save_message,
    get_chat_history,
    format_chat_history
)


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

    messages = get_chat_history(
        db,
        user_id
    )

    history = format_chat_history(
        messages
    )

    answer = await rag_chain.ainvoke(
        {
            "question": question,
            "history": history
        }
    )

    save_message(
        db,
        user_id,
        "assistant",
        answer
    )

    return answer