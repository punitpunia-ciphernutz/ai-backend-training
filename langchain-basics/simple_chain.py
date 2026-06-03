from dotenv import load_dotenv
from langchain_google_genai import (ChatGoogleGenerativeAI)
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

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