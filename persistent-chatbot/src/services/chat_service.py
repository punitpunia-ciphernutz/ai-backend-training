from src.memory.history_service import (save_message, get_messages)
from src.chains.chat_chain import chat_chain

def chat(question):

    history = ""

    messages = get_messages()

    for msg in messages:

        history += (
            f"{msg.role}: "
            f"{msg.content}\n"
        )

    response = chat_chain.invoke(
        {
            "history": history,
            "question": question
        }
    )

    save_message(
        "user",
        question
    )

    try:
        if isinstance(response.content, list) and len(response.content) > 0:
            ai_text = response.content[0].get('text', str(response.content))
        else:
            ai_text = str(response.content)
    except Exception:
        # Fallback in case the structure varies unexpectedly
        ai_text = str(response.content)

    save_message(
        "assistant",
        ai_text
    )

    return ai_text