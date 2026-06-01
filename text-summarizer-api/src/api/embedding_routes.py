from fastapi import APIRouter

from src.schemas.embedding import (EmbeddingRequest)

from src.services.embedding_service import (save_embedding)

router = APIRouter(
    prefix="/embeddings",
    tags=["Embeddings"]
)

@router.post("/")
async def create_embedding(request: EmbeddingRequest):
    return await save_embedding(request.text)

