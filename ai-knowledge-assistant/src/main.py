from src.core.config import settings
from fastapi import FastAPI
from src.api.auth import router
from src.core.database import (Base,engine)
from src.api.upload import (
    router as upload_router
)
from src.api.chat import (
    router as chat_router
)
from src.models.token_log import TokenLog

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(
    router,
    prefix="/auth"
)

app.include_router(
    upload_router,
    prefix="/upload"
)

app.include_router(
    chat_router,
    tags=["Chat"]
)