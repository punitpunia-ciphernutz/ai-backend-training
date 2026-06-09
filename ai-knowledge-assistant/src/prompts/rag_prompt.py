from langchain_core.prompts import ChatPromptTemplate

rag_prompt = ChatPromptTemplate.from_template(
    """
You are an AI Knowledge Assistant.

Answer using only the provided context.

Context:
{context}

Question:
{question}

Answer:
"""
)