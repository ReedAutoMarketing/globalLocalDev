# app/__init__.py
from flask import Flask
from flask_cors import CORS
from flask_session import Session
from werkzeug.middleware.proxy_fix import ProxyFix
from app.config import settings
from app.utils import redis_operations, google_api, openai_operations, db_operations
from .utils import openai_operations
from app.utils import openai_operations
from openai_operations import initialize_openai, add_summarize_reviews_route
import logging  # For the logger

def create_app():
    app = Flask(__name__)
    CORS(
        app,
        supports_credentials=True,
        origins=["https://app.gmb.reedauto.com", "https://localhost:3000"],
    )
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.secret_key = settings.SECRET_KEY

    # Initialize Logger
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    # Redis Session Configuration
    app.config["SESSION_TYPE"] = "redis"
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_USE_SIGNER"] = True
    app.config["SESSION_KEY_PREFIX"] = "session:"
    redis_client = redis_operations.init_redis()  # Initialize Redis client
    app.config["SESSION_REDIS"] = redis_client
    Session(app)

    # Initialize APIs
    google_api.load_google_api_config()
    initialize_openai(api_key="OPENAI_API_KEY")  # Initialize OpenAI only once

    # Add the summarize_reviews route to the Flask app
    add_summarize_reviews_route(app, redis_client, logger)
    
    return app
