from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import Float

from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Message(Base):

    __tablename__ = "messages"

    id = Column(Integer,primary_key=True)
    role = Column(String)
    content = Column(Text)

class TokenLog(Base):

    __tablename__ = "token_logs"

    id = Column(Integer,primary_key=True)

    input_tokens = Column(Integer)

    output_tokens = Column(Integer)

    total_tokens = Column(Integer)

    cost = Column(Float)