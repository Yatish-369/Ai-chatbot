from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

TOGETHER_API_KEY = "your_api_key_here"
MODEL = "mistralai/Mistral-7B-Instruct-v0.2"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    response = requests.post(
        "https://api.together.ai/v1/chat/completions",
        headers={"Authorization": f"Bearer {TOGETHER_API_KEY}"},
        json={
            "model": MODEL,
            "messages": data["messages"],
            "temperature": 0.7,
            "max_tokens": 1024
        }
    )
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(port=5000)
