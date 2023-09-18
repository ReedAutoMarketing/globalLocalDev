# app/utils/redis_operations.py
import os
from flask import Blueprint
import redis
from app.config import settings

redis_operations = Blueprint('redis_operations', __name__)

def init_redis():
    """Initialize Redis client."""
    return redis.StrictRedis(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        db=settings.REDIS_DB,
        password=settings.REDIS_PASSWORD,
        ssl=False,  # Disable SSL
    )
