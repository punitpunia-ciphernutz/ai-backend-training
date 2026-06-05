from langchain_chroma import Chroma

from src.core.embeddings import embeddings


vectorstore = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)


retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)