from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from src.core.database import get_db
from src.core.security import get_current_user

from src.services.rag_service import (
    ask_question
)
from fastapi.responses import StreamingResponse

from src.models.token_log import TokenLog
from src.services.rag_service import (
    stream_answer
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

@router.get("/usage")
async def usage(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    logs = (
        db.query(TokenLog)
        .filter(
            TokenLog.user_id == current_user.id
        )
        .all()
    )

    return logs

@router.post("/chat/stream")
async def chat_stream(
    question: str,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    return StreamingResponse(
        stream_answer(
            db=db,
            user_id=current_user.id,
            question=question
        ),
        media_type="text/event-stream"
    )