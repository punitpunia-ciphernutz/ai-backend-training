from langchain_core.prompts import ChatPromptTemplate

rag_prompt = ChatPromptTemplate.from_template(
    """
You are an AI Knowledge Assistant.

Use the conversation history when relevant.

Answer using the conversation history and provided context.

Conversation History:
{history}

Context:
{context}

Question:
{question}

Answer:
"""
)