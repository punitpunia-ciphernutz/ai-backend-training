import google.generativeai as genai
from src.services.logger_service import LOGGER
from src.db.chroma_client import (collection)
from src.core.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

async def generate_embedding(text:str):

    response = genai.embed_content(model="gemini-embedding-001", content=text)
    return response["embedding"]

async def store_chunks(chunks):
    for index, chunk in enumerate(chunks):
        embedding = await generate_embedding(chunk)
        collection.add(
            ids=[f"chunk-{index}"],
            documents=[chunk],
            embeddings=[embedding]
        )