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

        raw_output = response.get("output")

        if isinstance(raw_output, list) and len(raw_output) > 0:
            clean_text = raw_output[0].get("text", "")
        else:
            clean_text = raw_output

        print("\nAssistant:", clean_text)
        


if __name__ == "__main__":
    main()