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

# Locations Dictionary
LOCATIONS = {
    "Reed Jeep Chrysler Dodge Ram of Kansas City Service Center": ("107525660123223074874", "6602925040958900944"),
    "Reed Jeep of Kansas City": ("107525660123223074874", "1509419292313302599"),
    "Reed Jeep Chrysler Dodge Ram of Kansas City Parts Store": ("107525660123223074874", "13301160076946238237"),
    "Reed Chrysler Dodge Jeep Ram": ("111693813506330378362", "11797626926263627465"),
    "Reed Jeep Ram Service Center of St. Joseph": ("111693813506330378362", "14280468831929260325"),
    "Reed Jeep Ram Parts Store": ("111693813506330378362", "2418643850076402830"),
    "Reed Hyundai St. Joseph": ("106236436844097816145", "11886236645408970450"),
    "Reed Hyundai Service Center St. Joseph": ("106236436844097816145", "14394473597121013675"),
    "Reed Hyundai of Kansas City": ("109745744288166151974", "8949845982319380160"),
    "Reed Hyundai Service Center of Kansas City": ("109745744288166151974", "14191266722711425624"),
    "Reed Hyundai Parts Store": ("109745744288166151974", "16832194732739486696"),
    "Reed Collision Center": ("118020935772003776996", "14476819248161239911"),
    "Reed Chevrolet of St Joseph": ("101540168465155832676", "4906344306812977154"),
    "Reed Chevrolet Service Center": ("101540168465155832676", "7432353734414121407"),
    "Reed Chevrolet Parts": ("101540168465155832676", "13264330561216148213"),
    "Reed Buick GMC, INC.": ("109231983509135903650", "9980434767027047433"),
    "Reed Buick GMC Service Center": ("109231983509135903650", "9597638825461585665"),
    "Reed Buick GMC Collision Center": ("109231983509135903650", "10315051056232587965")
}
