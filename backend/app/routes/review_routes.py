# app/routes/reviews.py
from flask import Blueprint, jsonify, request
from app.utils import google_api, redis_operations, openai_operations, db_operations

reviews = Blueprint('reviews', __name__)

# Your reviews-related routes go here
# For example, @reviews.route("/fetch_reviews", methods=["GET"]) ...
