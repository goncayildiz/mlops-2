"""
Main Flask Application Module.
This module defines the API endpoints for the prediction service.
"""

from flask import Flask, jsonify, request
from src.feature_eng import hash_feature

app = Flask(__name__)


@app.route('/health', methods=['GET'])
def health():
    """
    Health check endpoint to verify service status.
    """
    return jsonify({"status": "healthy"}), 200


@app.route('/predict', methods=['POST'])
def predict():
    """
    Prediction endpoint that hashes the city name.
    """
    data = request.get_json()
    if not data or 'city' not in data:
        return jsonify({"error": "No city provided"}), 400

    city = data['city']
    bucket = hash_feature(city)
    return jsonify({"city": city, "bucket": bucket}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
