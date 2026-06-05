from langchain.tools import tool

from src.retrieval.retriever import retriever

@tool
def search_docs(query: str):

    """
    Search the knowledge base and retrieve information from stored documents.

    MUST be used for:
    - JWT questions
    - FastAPI questions
    - Course notes
    - Any factual question about stored documents

    Use this before answering.
    """

    docs = retriever.invoke(query)

    return "\n\n".join(
        doc.page_content
        for doc in docs
    )