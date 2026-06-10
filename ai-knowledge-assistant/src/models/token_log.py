from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer

from src.core.database import Base

class TokenLog(Base):

    __tablename__ = "token_logs"

    id = Column(
        Integer,
        primary_key=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    input_tokens = Column(
        Integer,
        nullable=False
    )

    output_tokens = Column(
        Integer,
        nullable=False
    )

    total_tokens = Column(
        Integer,
        nullable=False
    )

    cost = Column(
        Float,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )