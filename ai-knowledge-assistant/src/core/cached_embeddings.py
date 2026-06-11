import json

from langchain_google_genai import (
    GoogleGenerativeAIEmbeddings
)

from src.core.cache import cache
from src.core.logger import logger


class CachedEmbeddings:

    def __init__(self):

        self.embedding_model = (
            GoogleGenerativeAIEmbeddings(
                model="models/gemini-embedding-2"
            )
        )

    def embed_documents(
        self,
        texts
    ):

        results = []

        for text in texts:

            key = f"embedding:{hash(text)}"

            cached = cache.get(key)

            if cached:

                logger.info(
                    "Embedding Cache HIT"
                )

                results.append(
                    json.loads(cached)
                )

                continue

            logger.info(
                "Embedding Cache MISS"
            )

            embedding = (
                self.embedding_model
                .embed_query(text)
            )

            cache.set(
                key,
                json.dumps(embedding)
            )

            results.append(
                embedding
            )

        return results

    def embed_query(
        self,
        text
    ):

        key = f"embedding:{hash(text)}"

        cached = cache.get(key)

        if cached:

            logger.info(
                "Embedding Cache HIT"
            )

            return json.loads(
                cached
            )

        logger.info(
            "Embedding Cache MISS"
        )

        embedding = (
            self.embedding_model
            .embed_query(text)
        )

        cache.set(
            key,
            json.dumps(embedding)
        )

        return embedding