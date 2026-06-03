from dotenv import load_dotenv
from langchain_google_genai import (ChatGoogleGenerativeAI)
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

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