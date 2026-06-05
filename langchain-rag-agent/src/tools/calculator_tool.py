from langchain.tools import tool


@tool
def calculator(expression: str):

    """
    Solve math expressions.
    """

    return str(eval(expression))