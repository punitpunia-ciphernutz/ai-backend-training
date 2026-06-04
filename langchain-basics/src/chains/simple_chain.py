from langchain_core.prompts import PromptTemplate
from src.core.llm import llm

def run_simple_chain():
    prompt = PromptTemplate(
    input_variables=["topic"],
    template="""
    You are a Python teacher.

    Explain {topic}
    in simple words.
    """
    )

    chain = prompt | llm

    response = chain.invoke(
        {
        "topic": "FastAPI"
        }
    )
    print(response.content)