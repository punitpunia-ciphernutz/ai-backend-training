from langchain_core.prompts import PromptTemplate
from src.core.llm import llm



def run_multi_step_chain():
    summary_prompt = PromptTemplate(
    input_variables=["topic"],
    template="""
    Give a short summary of:

    {topic}
    """
    )

    teacher_prompt = PromptTemplate(
    input_variables=["summary"],
    template="""
    Explain this summary
    to a beginner:

    {summary}
    """
    )

    summary_chain = summary_prompt | llm
    teacher_chain = teacher_prompt | llm

    summary = summary_chain.invoke(
        {
            "topic": "FastAPI"
        }
    )

    final_answer = teacher_chain.invoke(
        {
            "summary": summary.content
        }
    )

    print(final_answer.content)