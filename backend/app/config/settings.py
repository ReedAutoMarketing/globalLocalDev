# app/config/settings.py
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Environment Variables
CLIENT_SECRETS_FILE = os.environ.get("CLIENT_SECRETS_FILE")
CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
AUTH_URI = os.environ.get("AUTH_URI")
TOKEN_URI = os.environ.get("TOKEN_URI")
AUTH_PROVIDER_X509_CERT_URL = os.environ.get("AUTH_PROVIDER_X509_CERT_URL")
REDIRECT_URIS = os.environ.get("REDIRECT_URIS").split(",")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SECRET_KEY = os.environ["SECRET_KEY"]

# Redis Configuration
REDIS_HOST = os.environ.get("REDIS_HOST")
REDIS_PORT = os.environ.get("REDIS_PORT")
REDIS_DB = os.environ.get("REDIS_DB")
REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD")

# Database Configuration
DB_HOST = os.environ.get("DB_HOST")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_PORT = os.environ.get("DB_PORT")

# Other Configs
SCOPES = ["https://www.googleapis.com/auth/business.manage"]
API_SERVICE_NAME = "mybusiness"
API_VERSION = "v4"
