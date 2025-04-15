# memory/vector_memory.py

from openai import embeddings


def fetch_user_preferences(user_id, index):
    result = index.fetch(ids=[user_id])

    # Ensure user_id exists in the response
    if user_id in result.vectors:
        return result.vectors[user_id].metadata
    else:
        return {}
