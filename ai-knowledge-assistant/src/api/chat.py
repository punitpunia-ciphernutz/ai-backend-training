from fastapi import APIRouter
from src.services.rag_service import (
    ask_question
)

router = APIRouter()

@router.post("/chat")
async def chat(
    question: str
):

    answer = await ask_question(
        question
    )

    return {
        "answer": answer
    }