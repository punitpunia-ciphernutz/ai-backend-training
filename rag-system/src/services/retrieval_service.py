from src.db.chroma_client import (collection)
from src.services.embedding_service import (generate_embedding)

async def retrieve_context(question: str):

    query_embedding = (
        await generate_embedding(
            question
        )
    )

    results = collection.query(
        query_embeddings=[
            query_embedding
        ],
        n_results=3
    )

    return results["documents"][0]