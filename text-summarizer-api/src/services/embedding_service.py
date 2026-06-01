import os
import json
import google.generativeai as genai
from src.core.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

EMBEDDING_FILE = "src/storage/embeddings.json"

#Generate Embedding Function

async def generate_embedding(text: str):
    response = genai.embed_content(model="gemini-embedding-001",content=text)
    return response["embedding"]

#Store Embedding Locally

async def save_embedding(text: str):
    embedding = await generate_embedding(text)
    record = {
        "text": text,
        "embedding": embedding
    }
    data = []
    if os.path.exists(EMBEDDING_FILE):
        with open(EMBEDDING_FILE,"r") as f:
            try:
                data = json.load(f)
            except:
                data = []
    data.append(record)
    with open(EMBEDDING_FILE,"w") as f:
        json.dump(data,f,indent=2)

    return record