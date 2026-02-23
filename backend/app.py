from flask import Flask, jsonify, request
from flask_cors import CORS
import requests as req
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

HEADERS = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json"
}


# GET /comments - Fetch all comments
@app.route("/comments", methods=["GET"])
def get_comments():
    response = req.get(
        f"{SUPABASE_URL}/rest/v1/comments?select=*&order=created_at.desc",
        headers=HEADERS
    )
    return jsonify(response.json()), response.status_code


# POST /comments - Insert a new comment
@app.route("/comments", methods=["POST"])
def post_comment():
    data = request.get_json()

    name = data.get("name", "").strip()
    message = data.get("message", "").strip()

    if not name or not message:
        return jsonify({"error": "Name and message are required"}), 400

    response = req.post(
        f"{SUPABASE_URL}/rest/v1/comments",
        headers={**HEADERS, "Prefer": "return=representation"},
        json={"name": name, "message": message}
    )
    return jsonify(response.json()), response.status_code


if __name__ == "__main__":
    app.run(debug=True)
