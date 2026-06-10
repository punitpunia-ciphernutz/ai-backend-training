from sqlalchemy.orm import Session

from src.models.chat import ChatMessage


def save_message(
    db: Session,
    user_id: int,
    role: str,
    content: str
):

    message = ChatMessage(
        user_id=user_id,
        role=role,
        content=content
    )

    db.add(message)
    db.commit()

    return message


def get_chat_history(
    db: Session,
    user_id: int
):

    return (
        db.query(ChatMessage)
        .filter(
            ChatMessage.user_id == user_id
        )
        .order_by(
            ChatMessage.created_at
        )
        .all()
    )

def format_chat_history(messages):

    return "\n".join(
        f"{msg.role}: {msg.content}"
        for msg in messages
    )