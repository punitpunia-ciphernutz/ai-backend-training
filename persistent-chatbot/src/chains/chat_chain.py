from langchain_core.prompts import ChatPromptTemplate
from src.core.llm import llm

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant."
        ),
        (
            "human",
            """
History:

{history}

Question:

{question}
"""
        )
    ]
)

chat_chain = prompt | llm