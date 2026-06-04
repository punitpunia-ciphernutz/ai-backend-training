from langchain_core.chat_history import (InMemoryChatMessageHistory)
from src.core.llm import llm


def run_chatbot():
    memory = InMemoryChatMessageHistory()
    print("Type 'exit' to quit")

    while True:
        question = input("\nYou: ")

        if question.lower() == "exit":
            break

        memory.add_user_message(question)

        response = llm.invoke(memory.messages)

        memory.add_ai_message(response.content)

        print("\nAI:",response.content)