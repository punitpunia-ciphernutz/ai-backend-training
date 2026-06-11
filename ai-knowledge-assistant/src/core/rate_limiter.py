from fastapi import Request
from fastapi.responses import JSONResponse

from src.core.cache import cache
from src.core.logger import logger


RATE_LIMIT = 20
WINDOW = 300


async def rate_limit_middleware(
    request: Request,
    call_next
):

    auth_header = request.headers.get(
        "Authorization"
    )

    if not auth_header:

        return await call_next(
            request
        )

    key = f"rate_limit:{auth_header}"

    try:

        current = cache.get(key)

    except Exception as e:

        logger.exception(
            {
                "event": "rate_limit_redis_error",
                "error": str(e)
            }
        )

        return await call_next(
            request
        )

    if current is None:

        try:

            cache.set(
                key,
                1,
                ex=WINDOW
            )

            logger.info(
                {
                    "event": "rate_limit_initialized",
                    "key": key
                }
            )

        except Exception as e:

            logger.exception(
                {
                    "event": "rate_limit_redis_error",
                    "error": str(e)
                }
            )

    else:

        current = int(current)

        if current >= RATE_LIMIT:

            logger.warning(
                {
                    "event": "rate_limit_exceeded",
                    "key": key,
                    "current_requests": current,
                    "limit": RATE_LIMIT
                }
            )

            return JSONResponse(
                status_code=429,
                content={
                    "detail": "Rate limit exceeded"
                }
            )

        try:

            cache.incr(key)

            logger.info(
                {
                    "event": "rate_limit_increment",
                    "key": key,
                    "current_requests": current + 1,
                    "limit": RATE_LIMIT
                }
            )

        except Exception as e:

            logger.exception(
                {
                    "event": "rate_limit_redis_error",
                    "error": str(e)
                }
            )

    return await call_next(
        request
    )