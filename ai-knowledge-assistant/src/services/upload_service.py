from src.ingestion.loader import load_text

from src.ingestion.chunker import chunk_text

from src.vectorstore.chroma_store import (
    vector_db
)
from src.core.logger import logger

def upload_document(file):

    text = load_text(file)

    docs = chunk_text(text)

    vector_db.add_documents(
        docs
    )
    logger.info(f"Document uploaded: {file.filename}")

    return {
        "chunks": len(docs),
        "status": "stored"
    }