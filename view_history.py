from agents.summarizer_agent import get_summary_history

def display_history(user_id):
    history = get_summary_history(user_id)

    if not history:
        print(f"\n🕵️ No summaries found for user '{user_id}'.")
        return

    print(f"\n📚 Summary History for user '{user_id}':\n")
    for i, entry in enumerate(history, 1):
        print(f"--- Summary #{i} ---")
        print(f"🕒 Created: {entry['created_at']}")
        print(f"🧠 Preferences: {entry['preferences']}")
        print(f"📰 Article: {entry.get('original_article', 'N/A')[:100]}...")
  # First 100 chars
        print(f"📝 Summary: {entry['summary']}")
        print("\n")

if __name__ == "__main__":
    user_id = input("Enter user ID to view history: ")
    display_history(user_id)
