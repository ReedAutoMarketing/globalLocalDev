# app/utils/openai_operations.py
import json
import openai
import flask

# Initialize OpenAI by setting the API key
def initialize_openai(api_key):
    openai.api_key = api_key

# Function to get completion from OpenAI's GPT model
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.7  # Degree of randomness in output
    )
    return response.choices[0].message["content"]

# Function to add the summarize_reviews route to the Flask app
def add_summarize_reviews_route(app, redis_client, logger):
    
    @app.route("/summarize_reviews", methods=["POST"])
    def summarize_reviews():
        try:
            location_name = flask.request.json.get("location_name", None)
            if not location_name:
                return flask.jsonify({"error": "No location_name provided"}), 400

            # Fetch reviews from Redis based on location_name
            redis_key = f"reviews_{location_name}"
            reviews_json = redis_client.get(redis_key)

            if reviews_json is None:
                return flask.jsonify({"error": "No reviews found for the given location, please fetch them first"}), 400

            reviews = json.loads(reviews_json)

            summaries = []
            for review in reviews:
                comment = review.get("comment", "")
                prompt = f"""
    ...  # (your existing prompt here)
    """
                summary = get_completion(prompt)
                logger.debug(f"Generated Summary: {summary}")  # Debugging line
                summaries.append(summary)

            return flask.jsonify({"summary": " ".join(summaries)})

        except Exception as e:
            logger.error(f"Exception occurred: {e}")
            logger.exception("Exception details:")
            return flask.jsonify({"error": str(e)}), 500
