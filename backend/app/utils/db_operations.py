# app/utils/db_operations.py
import os
import psycopg2
import json
from app.config import settings

def connect_to_db():
    """Connect to PostgreSQL database."""
    conn = psycopg2.connect(
        host=settings.DB_HOST,
        database=settings.DB_NAME,
        user=settings.DB_USER,
        password=settings.DB_PASSWORD,
        port=settings.DB_PORT
    )
    return conn

# ... (the rest of your DB operations)
