from src.memory.history_service import (save_message, get_messages)
from src.chains.chat_chain import chat_chain
from src.tracking.token_tracker import (extract_usage)
from src.tracking.cost_calculator import (calculate_cost)
from src.database.token_service import (save_token_usage)

def chat(question):

    history = ""

    messages = get_messages()

    for msg in messages:

        history += (
            f"{msg.role}: "
            f"{msg.content}\n"
        )

    response = chat_chain.invoke(
        {
            "history": history,
            "question": question
        }
    )
    
    usage = extract_usage(response)

    cost = calculate_cost(
        usage["input_tokens"],
        usage["output_tokens"]
    )

    save_token_usage(
        usage["input_tokens"],
        usage["output_tokens"],
        usage["total_tokens"],
        cost
    )

    print("\nTOKEN USAGE")

    print(f"Input Tokens: {usage['input_tokens']}")

    print(f"Output Tokens: {usage['output_tokens']}")

    print(f"Total Tokens: {usage['total_tokens']}")

    print(f"Cost: ${cost:.8f}")

    save_message(
        "user",
        question
    )

    try:
        if isinstance(response.content, list) and len(response.content) > 0:
            ai_text = response.content[0].get('text', str(response.content))
        else:
            ai_text = str(response.content)
    except Exception:
        # Fallback in case the structure varies unexpectedly
        ai_text = str(response.content)

    save_message(
        "assistant",
        ai_text
    )

    return ai_text