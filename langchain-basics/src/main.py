from src.chains.simple_chain import (run_simple_chain)
from src.chains.multi_step_chain import (run_multi_step_chain)
from src.memory.conversational_chatbot import (run_chatbot)
from src.agents.calculator_agent import (run_calculator_agent)

print("\n1. Simple Chain")
print("2. Multi-Step Chain")
print("3. Memory Chatbot")
print("4. Calculator Agent")

choice = input("\nChoose: ")

if choice == "1":
    run_simple_chain()

elif choice == "2":
    run_multi_step_chain()

elif choice == "3":
    run_chatbot()

elif choice == "4":
    run_calculator_agent()