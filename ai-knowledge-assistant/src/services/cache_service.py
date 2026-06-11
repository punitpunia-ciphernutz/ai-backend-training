from src.core.cache import cache
from src.core.logger import logger


def get_cached_response(question):

    try:

        response = cache.get(
            f"chat:{question}"
        )

    except Exception as e:

        logger.exception(
            {
                "event": "redis_read_error",
                "error": str(e)
            }
        )

        return None

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

    try:

        cache.set(
            f"chat:{question}",
            answer,
            ex=3600
        )

    except Exception as e:

        logger.exception(
            {
                "event": "redis_write_error",
                "error": str(e)
            }
        )