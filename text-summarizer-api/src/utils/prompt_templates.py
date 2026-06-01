def summary_prompt(text: str) -> str:
    return f"""
    Summarize the following text in 3-5 concise bullet points.

    Text:
    {text}
    """ 