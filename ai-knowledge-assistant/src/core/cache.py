import redis

from src.core.config import settings


cache = redis.Redis.from_url(
    settings.REDIS_URL,
    decode_responses=True
)