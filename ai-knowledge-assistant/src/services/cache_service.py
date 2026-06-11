from src.core.cache import cache
from src.core.logger import logger

def get_cached_response(question):

    response = cache.get(f"chat:{question}")

    if response:
        logger.info(
            f"Cache HIT: {question}"
        )
    else:
        logger.info(
            f"Cache MISS: {question}"
        )

    return response


def set_cached_response(
    question: str,
    answer: str
):

    cache.set(
        f"chat:{question}",
        answer,
        ex=3600
    )