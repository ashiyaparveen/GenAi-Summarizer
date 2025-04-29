import os
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec

# Load environment variables from .env
load_dotenv(dotenv_path="E:/GenAI/.env")

# Correct variable names
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")

print("PINECONE_API_KEY:", PINECONE_API_KEY)
print("PINECONE_INDEX_NAME:", PINECONE_INDEX_NAME)

if not PINECONE_API_KEY or not PINECONE_INDEX_NAME:
    raise ValueError("Missing Pinecone API Key or Index Name from environment variables.")

pc = Pinecone(api_key=PINECONE_API_KEY)

# Create index if it doesn't exist
if PINECONE_INDEX_NAME not in pc.list_indexes().names():
    pc.create_index(
        name=PINECONE_INDEX_NAME,
        dimension=1536,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-west-2")
    )

pinecone_vector_db = pc.Index(PINECONE_INDEX_NAME)