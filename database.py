from dotenv import load_dotenv
import os
from pymongo import MongoClient # type: ignore

load_dotenv()

mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
db = client['genai']
summaries_collection = db['summaries']
