from fastapi import APIRouter

from src.schemas.search import (SearchRequest)

from src.services.embedding_service import (similarity_search)

router = APIRouter(
    prefix="/search",
    tags=["Search"]
)

@router.post("/")
async def search(
    request: SearchRequest
):

    return await similarity_search(
        request.query
    )