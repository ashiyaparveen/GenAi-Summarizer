from flask import Flask, request, jsonify
from agents.summarizer_agent import summarize_content, get_summary_history
from memory.vector_memory import fetch_user_preferences
from tools.real_time_web import fetch_article_summary
from config import pinecone_vector_db
from pymongo import MongoClient
from datetime import datetime
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app)

# 🔗 MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["genai"]
summaries_collection = db["summaries"]

# 📌 Route: Generate summary
@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.json
    user_id = data.get("user_id")
    url = data.get("url")

    if not user_id or not url:
        return jsonify({"error": "Please provide both user_id and url"}), 400

    article = fetch_article_summary(url)
    preferences = fetch_user_preferences(user_id, pinecone_vector_db)
    summary = summarize_content(user_id, article, preferences)

    # Save summary to MongoDB
    summaries_collection.insert_one({
        "user_id": user_id,
        "url": url,
        "summary": summary,
        "original_content": article,
        "preferences": preferences,
        "timestamp": datetime.utcnow()
    })

    return jsonify({"summary": summary})

# 📌 Route: History via Pinecone or other method
@app.route("/history", methods=["GET"])
def history():
    user_id = request.args.get("user_id")

    if not user_id:
        return jsonify({"error": "Please provide a user_id"}), 400

    history = get_summary_history(user_id)

    output = []
    for entry in history:
        output.append({
            "created_at": entry["created_at"],
            "summary": entry["summary"],
            "preferences": entry.get("preferences", {}),
            "original": entry.get("original_content", "")[:100] + "..."
        })

    return jsonify({"user_id": user_id, "history": output})

# 📌 Route: History from MongoDB (used by frontend /history.jsx)
@app.route("/api/summaries", methods=["GET"])
def get_summaries():
    user_id = request.args.get("user_id")
    if not user_id:
        return jsonify({"error": "Missing user_id"}), 400

    results = list(summaries_collection.find(
        {"user_id": user_id},
        {"_id": 0}
    ).sort("timestamp", -1))  # Sort by newest

    return jsonify(results)

# 🔍 Example fetch logic (manual test)
if __name__ == "__main__":
    # Simulate backend test
    user_id = "ashiya123"
    url = "https://techcrunch.com/2024/03/13/openai-launches-new-generative-ai-model/"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all("p")
        content = "\n".join(p.get_text() for p in paragraphs)
    else:
        content = "Article content could not be fetched. HTTP Status Code: " + str(response.status_code)

    article = fetch_article_summary(url)
    preferences = fetch_user_preferences(user_id, pinecone_vector_db)
    summary = summarize_content(user_id, article, preferences)

    print("\n🧠 Tailored Summary:\n", summary)
    print("\n📄 Original Article (truncated):\n", article[:300] + "...\n")

    app.run(debug=True)
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from GenAI!"

# Only needed if you're running locally
if __name__ == "__main__":
    app.run()
