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

    current = cache.get(key)

    if current is None:

        cache.set(
            key,
            1,
            ex=WINDOW
        )

    else:

        current = int(current)

        if current >= RATE_LIMIT:

            logger.warning(
                f"Rate limit exceeded: {key}"
            )

            return JSONResponse(
                status_code=429,
                content={
                    "detail":
                    "Rate limit exceeded"
                }
            )

        cache.incr(key)

    return await call_next(
        request
    )