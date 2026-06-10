from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from src.core.database import get_db
from src.core.security import get_current_user

from src.services.rag_service import (
    ask_question
)

router = APIRouter()


@router.post("/chat")
async def chat(
    question: str,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    answer = await ask_question(
        db=db,
        user_id=current_user.id,
        question=question
    )

    return {
        "answer": answer
    }