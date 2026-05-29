from sqlalchemy.ext.asyncio import (create_async_engine, AsyncSession)
from sqlalchemy.orm import sessionmaker, declarative_base
import os

DATABASE_URL = os.getenv("DATABASE_URL")

#DATABASE_URL = "postgresql+asyncpg://mac@localhost:5432/taskdb"

engine = create_async_engine(DATABASE_URL, echo=True)

session_local = sessionmaker(bind=engine, class_ = AsyncSession, expire_on_commit=False)

Base = declarative_base()