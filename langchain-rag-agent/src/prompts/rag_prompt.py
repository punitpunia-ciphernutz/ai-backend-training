from langchain_core.prompts import ChatPromptTemplate

rag_prompt = ChatPromptTemplate.from_template(
"""
Answer only from context.

Context:
{context}

Question:
{question}
"""
)
