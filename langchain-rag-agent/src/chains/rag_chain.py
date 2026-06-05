from src.prompts.rag_prompt import rag_prompt
from src.core.llm import llm

rag_chain = rag_prompt | llm