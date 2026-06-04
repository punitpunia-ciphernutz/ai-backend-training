from langchain_core.messages import (HumanMessage,ToolMessage)
from src.core.llm import llm
from src.tools.calculator_tool import calculator


llm_with_tools = llm.bind_tools([calculator])


def run_calculator_agent():

    while True:
        question = input("\nYou: ")

        if question.lower() == "exit":
            break

        response = llm_with_tools.invoke([HumanMessage(content=question)])

        if response.tool_calls:

            tool_call = response.tool_calls[0]

            result = calculator.invoke(tool_call["args"])

            final_response = llm_with_tools.invoke(
                [
                    HumanMessage(content=question),

                    response,

                    ToolMessage(
                        content=result,
                        tool_call_id=tool_call["id"]
                    )
                ]
            )

            print("\nAI:",final_response.content)

        else:

            print("\nAI:",response.content)