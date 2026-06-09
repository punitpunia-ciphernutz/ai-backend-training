from sqlalchemy import Column, Integer, Text, String

from src.database.db import Base


class ChatMessage(Base):

    __tablename__ = "chat_messages"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    role = Column(String)

    content = Column(Text)