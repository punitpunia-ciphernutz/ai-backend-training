from src.database.db import SessionLocal
from src.database.models import Message

def save_message(role, content):
    db = SessionLocal()

    msg = Message(
        role=role,
        content=content
    )

    db.add(msg)
    db.commit()
    db.close()

def get_messages():

    db = SessionLocal()
    messages = db.query(Message).all()
    db.close()

    return messages