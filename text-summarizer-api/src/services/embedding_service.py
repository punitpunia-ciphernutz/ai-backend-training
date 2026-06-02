import os
import json
import google.generativeai as genai
import numpy as np
from src.db.chroma_client import collection
from src.core.config import GEMINI_API_KEY  

genai.configure(api_key=GEMINI_API_KEY)

EMBEDDING_FILE = "src/storage/embeddings.json"

def cosine_similarity(vec1, vec2):

    vec1 = np.array(vec1)
    vec2 = np.array(vec2)

    similarity = np.dot(vec1, vec2) / (
        np.linalg.norm(vec1) *
        np.linalg.norm(vec2)
    )

    return float(similarity)

#Generate Embedding Function

async def generate_embedding(text: str):
    response = genai.embed_content(model="gemini-embedding-001",content=text)
    return response["embedding"]

#Store Embedding Locally

async def save_embedding(text: str):

    embedding = await generate_embedding(text)

    collection.add(
        ids=[str(hash(text))],
        documents=[text],
        embeddings=[embedding]
    )

    return {
        "message": "Stored successfully"
    }

#Load Stored Embeddings

async def load_embeddings():

    with open(EMBEDDING_FILE,"r") as f:
        return json.load(f)
    
#create a function to find the most similar embedding

async def similarity_search(query: str):

    query_embedding = await generate_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=1
    )

    return results