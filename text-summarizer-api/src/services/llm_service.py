import google.generativeai as genai

from src.core.config import GEMINI_API_KEY
from src.utils.prompt_templates import summary_prompt

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

async def summarize_text(text: str) -> str:
    text=text.strip()
    prompt = summary_prompt(text)
    response = model.generate_content(prompt)
    return response.text.strip()