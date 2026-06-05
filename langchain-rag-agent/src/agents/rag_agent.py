from langchain_classic.agents import create_tool_calling_agent, AgentExecutor

from langchain_core.prompts import ChatPromptTemplate

from src.tools.calculator_tool import calculator
from src.tools.rag_tool import search_docs
from src.core.llm import llm
from src.memory.chat_memory import memory


tools = [
    search_docs,
    calculator
]

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("placeholder", "{chat_history}"),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}")
    ]
)

agent = create_tool_calling_agent(
    llm,
    tools,
    prompt
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    memory=memory,
    verbose=True
)