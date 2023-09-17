# app/utils/redis_operations.py
import os
import redis
from app.config import settings

def init_redis():
    """Initialize Redis client."""
    return redis.StrictRedis(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        db=settings.REDIS_DB,
        password=settings.REDIS_PASSWORD,
        ssl=False,  # Disable SSL
    )
