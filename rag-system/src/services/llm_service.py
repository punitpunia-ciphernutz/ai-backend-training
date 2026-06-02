import google.generativeai as genai

model = genai.GenerativeModel(
    "gemini-3.1-flash-lite"
)

async def generate_answer(question,context):
    prompt = f"""
Use the provided context.

Context:
{context}

Question:
{question}
"""

    response = model.generate_content(
        prompt
    )

    return response.text