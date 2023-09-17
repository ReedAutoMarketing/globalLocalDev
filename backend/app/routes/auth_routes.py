from flask import Blueprint, request, session, jsonify, redirect, current_app
import secrets
import google.oauth2.credentials
import google_auth_oauthlib.flow
from app.config import settings  # Import settings or config module
from app.utils.redis_operations import init_redis  # Import Redis utility

auth_routes = Blueprint('auth_routes', __name__)

# Helper Functions
def generate_random_string(length):
    return secrets.token_hex(length)

def credentials_to_dict(credentials):
    return {
        "token": credentials.token,
        "refresh_token": credentials.refresh_token,
        "token_uri": credentials.token_uri,
        "client_id": credentials.client_id,
        "client_secret": credentials.client_secret,
        "scopes": credentials.scopes,
    }

# Routes
@auth_routes.route("/authorize")
def authorize():
    # Use the already initialized Redis client
    redis_client = init_redis()

    state = generate_random_string(32)
    redis_client.set("state", state)

    next_page = request.args.get("next", "https://localhost:3000/")
    current_app.logger.debug(f"Setting next_page to {next_page}")
    session["next_page"] = next_page

    client_config = {
        "web": {
            "client_id": settings.CLIENT_ID,
            "client_secret": settings.CLIENT_SECRET,
            "auth_uri": settings.AUTH_URI,
            "token_uri": settings.TOKEN_URI,
            "auth_provider_x509_cert_url": settings.AUTH_PROVIDER_X509_CERT_URL,
            "redirect_uris": settings.REDIRECT_URIS,
        }
    }
    flow = google_auth_oauthlib.flow.Flow.from_client_config(
        client_config, scopes=settings.SCOPES
    )
    flow.redirect_uri = request.url_root + "oauth2callback"

    authorization_url, state = flow.authorization_url(
        access_type="offline", include_granted_scopes="false", state=state
    )

    return jsonify({"authorization_url": authorization_url})


@auth_routes.route("/oauth2callback")
def oauth2callback():
    redis_client = init_redis()
    stored_state = redis_client.get("state")
    if stored_state is not None:
        stored_state = stored_state.decode()
    url_state = request.args.get("state")

    if stored_state is None or stored_state != url_state:
        current_app.logger.error("Invalid state")
        return "Invalid state", 400

    # Initialize the same OAuth2 flow as in /authorize
    client_config = {
        "web": {
            "client_id": settings.CLIENT_ID,
            "client_secret": settings.CLIENT_SECRET,
            "auth_uri": settings.AUTH_URI,
            "token_uri": settings.TOKEN_URI,
            "auth_provider_x509_cert_url": settings.AUTH_PROVIDER_X509_CERT_URL,
            "redirect_uris": settings.REDIRECT_URIS,
        }
    }

    flow = google_auth_oauthlib.flow.Flow.from_client_config(
        client_config, scopes=settings.SCOPES, state=stored_state
    )
    flow.redirect_uri = request.url_root + "oauth2callback"

    authorization_response = request.url
    try:
        flow.fetch_token(authorization_response=authorization_response)
    except Exception as e:
        current_app.logger.error(f"Exception occurred: {e}")
        return f"Error: {e}", 500

    credentials = flow.credentials
    session["credentials"] = credentials_to_dict(credentials)
    session["access_token"] = credentials.token

    redis_client.delete("state")

    next_page = session.get("next_page", "https://localhost:3000")
    return redirect(next_page or "/")

@auth_routes.route("/check_auth")
def check_auth():
    if "credentials" in session:
        access_token = session.get("access_token")
        return jsonify({"isAuthenticated": True, "access_token": access_token})
    else:
        return jsonify({"isAuthenticated": False})
