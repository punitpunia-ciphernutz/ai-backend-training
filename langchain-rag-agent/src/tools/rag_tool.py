from langchain.tools import tool

from src.retrieval.retriever import retriever

@tool
def search_docs(query: str):

    """
    Search documents.
    """

    docs = retriever.invoke(query)

    return "\n\n".join(
        doc.page_content
        for doc in docs
    )