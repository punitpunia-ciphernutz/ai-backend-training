from langchain_core.tools import tool

@tool
def calculator(expression: str) -> str:
    """
    Calculate mathematical expressions.
    """

    try:
        return str(eval(expression))

    except Exception as e:
        return str(e)