from fastapi import (APIRouter, HTTPException)
from src.schemas.summary import SummaryRequest, SummaryResponse
from src.services.llm_service import summarize_text

router = APIRouter(prefix="/summary",tags=["Summary"])

@router.post("/", response_model=SummaryResponse)
async def summarize(request: SummaryRequest) -> SummaryResponse:
    try:
        summary = await summarize_text(request.text)
        return SummaryResponse(summary=summary)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    