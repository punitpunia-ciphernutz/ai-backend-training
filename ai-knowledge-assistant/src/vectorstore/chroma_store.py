from langchain_chroma import Chroma

from src.core.embeddings import embeddings

vector_db = Chroma(
    collection_name="documents",
    embedding_function=embeddings,
    persist_directory="chroma_db"
)
