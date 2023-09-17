# app/utils/google_api.py
from app.config import settings

def load_google_api_config():
    return settings.SCOPES, settings.API_SERVICE_NAME, settings.API_VERSION
