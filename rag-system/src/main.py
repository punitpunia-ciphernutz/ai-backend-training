from fastapi import FastAPI
from src.api.ingest_routes import (router as ingest_router)

from src.api.chat_routes import (router as chat_router)

app = FastAPI()

app.include_router(ingest_router)

app.include_router(chat_router)