from src.core.cache import cache
from src.core.logger import logger

def get_cached_response(question):

    response = cache.get(f"chat:{question}")

    if response:
        logger.info(
            {
                "event": "cache_hit",
                "question": question
            }
        )
    else:
        logger.info(
            {
                "event": "cache_miss",
                "question": question
            }
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