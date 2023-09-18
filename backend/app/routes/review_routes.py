from flask import Blueprint, request, jsonify
from app.utils.openai_operations import get_completion
from app.utils.redis_operations import redis_client
import json
import logging

# Initialize the Blueprint
review_routes = Blueprint('review_routes', __name__)

# Initialize logger
logger = logging.getLogger(__name__)

@review_routes.route('/summarize_reviews', methods=['POST'])
def summarize_reviews():
    try:
        location_name = request.json.get('location_name', None)
        if not location_name:
            return jsonify({"error": "No location_name provided"}), 400

        # Fetch reviews from Redis based on location_name
        redis_key = f"reviews_{location_name}"
        reviews_json = redis_client.get(redis_key)

        if reviews_json is None:
            return jsonify({"error": "No reviews found for the given location, please fetch them first"}), 400

        reviews = json.loads(reviews_json)

        summaries = []
        for review in reviews:
            comment = review.get('comment', '')
            prompt = f"Your task is to summarize the following review in 20 words: ```{comment}```"
            summary = get_completion(prompt)
            logger.debug(f"Generated Summary: {summary}")  # Debugging line
            summaries.append(summary)

        return jsonify({"summary": " ".join(summaries)})

    except Exception as e:
        logger.error(f"Exception occurred: {e}")
        logger.exception("Exception details:")
        return jsonify({"error": str(e)}), 500
