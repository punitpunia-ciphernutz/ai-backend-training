from fastapi import APIRouter
from src.schemas.ingest import (IngestRequest)
from src.services.chunk_service import (chunk_text)
from src.services.embedding_service import (store_chunks)

router = APIRouter(
    prefix="/ingest",
    tags=["Ingest"]
)

@router.post("/")
async def ingest_document(request: IngestRequest):
    chunks = chunk_text(request.text)
    await store_chunks(chunks)
    
    return {
        "chunks": len(chunks)
    }
