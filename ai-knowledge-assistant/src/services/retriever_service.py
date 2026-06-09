from src.vectorstore.chroma_store import vector_db

retriever = vector_db.as_retriever(
    search_kwargs={"k": 4}
)