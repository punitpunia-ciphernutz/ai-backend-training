from src.services.chat_service import chat

def main():

    print("Persistent Chatbot Started")

    while True:

        question = input("\nYou: ")

        if question.lower() == "exit":
            break

        response = chat(
            questionw
        )

        print(
            "\nAssistant:",
            response
        )


if __name__ == "__main__":
    main()