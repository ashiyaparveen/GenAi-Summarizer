import google.generativeai as genai
from datetime import datetime
from pymongo import MongoClient

# Setup Gemini
genai.configure(api_key="AIzaSyBgQh5AKTSiBxf588QVmPjTPhJCWA7LwKY")
model = genai.GenerativeModel(model_name="gemini-1.5-pro")

# Setup MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Update if hosted elsewhere
db = client["genai_db"]
collection = db["summaries"]

def summarize_content(user_id, article, preferences):
    prompt = f"Summarize this article for user {user_id} with preferences: {preferences}\n\n{article}"
    response = model.generate_content(prompt)
    summary_text = response.text

    # Save to MongoDB
    summary_doc = {
        "user_id": user_id,
        "original_content": article,
        "summary": summary_text,
        "preferences": preferences,
        
        "created_at": datetime.utcnow()
    }
    collection.insert_one(summary_doc)

    return summary_text

def get_summary_history(user_id):
    return list(collection.find({"user_id": user_id}).sort("created_at", -1))
