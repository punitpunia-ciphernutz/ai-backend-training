from src.ingestion.ingest import ingest
from src.agents.rag_agent import agent_executor
from src.memory.chat_memory import memory

def main():

    ingest()

    print("RAG Agent Started")

    while True:

        question = input("\nYou: ")

        if question.lower() == "exit":
            break


        response = agent_executor.invoke(
            {
                "input": question
            }
        )

        print(
            "\nAssistant:",
            response["output"]
        )
        


if __name__ == "__main__":
    main()