from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from src.services.retriever_service import retriever
from src.prompts.rag_prompt import rag_prompt
from src.core.llm import llm


def format_docs(docs):
    return "\n\n".join(
        doc.page_content
        for doc in docs
    )


rag_chain = (
    {
        "context": lambda x: format_docs(
            retriever.invoke(x["question"])
        ),
        "question": lambda x: x["question"],
        "history": lambda x: x["history"]
    }
    | rag_prompt
    | llm
    | StrOutputParser()
)