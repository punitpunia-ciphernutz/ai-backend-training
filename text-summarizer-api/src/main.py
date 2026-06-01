from fastapi import FastAPI
from src.api.summary_routes import router as summary_router

app = FastAPI(title="Text Summarizer API")

app.include_router(summary_router)