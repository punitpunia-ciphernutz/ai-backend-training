from langchain_google_genai import (
    ChatGoogleGenerativeAI
)

from src.core.config import settings
from src.core.logger import logger


primary_llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    google_api_key=settings.GEMINI_API_KEY,
    temperature=0
)

fallback_llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=settings.GEMINI_API_KEY,
    temperature=0
)

logger.info(
    "LLM initialized with retry and fallback support"
)

llm = (
    primary_llm
    .with_retry(
        stop_after_attempt=3
    )
    .with_fallbacks(
        [fallback_llm]
    )
)