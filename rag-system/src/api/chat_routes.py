from fastapi import APIRouter
from src.schemas.chat import (ChatRequest)
from src.services.retrieval_service import (retrieve_context)
from src.services.llm_service import (generate_answer)

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

@router.post("/")
async def chat(request: ChatRequest):
    context = await retrieve_context(request.question)
    answer = await generate_answer(
        request.question,
        context
    )

    return {
        "answer": answer
    }