import os
import json
import google.generativeai as genai
import numpy as np
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

#Load Stored Embeddings

async def load_embeddings():

    with open(EMBEDDING_FILE,"r") as f:
        return json.load(f)
    
#create a function to find the most similar embedding

async def similarity_search(query: str):

    query_embedding = await generate_embedding(query)

    records = await load_embeddings()

    best_score = -1
    best_match = None

    for record in records:

        score = cosine_similarity(
            query_embedding,
            record["embedding"]
        )

        if score > best_score:

            best_score = score
            best_match = record

    return {
        "query": query,
        "score": best_score,
        "match": best_match["text"]
    }