import React, { useState } from "react";
import History from "./History"; // Adjust path as per your folder
import "./App.css";

const API_BASE_URL = "http://localhost:5000";

function App() {
  const [userId, setUserId] = useState("");
  const [url, setUrl] = useState("");
  const [summary, setSummary] = useState("");
  const [showHistory, setShowHistory] = useState(false);

  const handleSummarize = async () => {
    const response = await fetch(`${API_BASE_URL}/summarize`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ user_id: userId, url }),
    });
    const data = await response.json();
    setSummary(data.summary);
  };

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">🧠 GenAI Summarizer</h1>

      <input
        type="text"
        placeholder="Enter user ID"
        value={userId}
        onChange={(e) => setUserId(e.target.value)}
        className="border p-2 mr-2"
      />
      <input
        type="text"
        placeholder="Enter article URL"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        className="border p-2 mr-2"
      />
      <button onClick={handleSummarize} className="bg-blue-500 text-white p-2">
        Summarize
      </button>

      {summary && (
        <div className="mt-4 p-4 bg-green-100 rounded">
          <h2 className="font-semibold">Tailored Summary:</h2>
          <p>{summary}</p>
        </div>
      )}

      <button
        onClick={() => setShowHistory(!showHistory)}
        className="mt-4 bg-gray-600 text-white p-2 rounded"
      >
        {showHistory ? "Hide History" : "View History"}
      </button>

      {showHistory && <History userId={userId} />}
    </div>
  );
}

export default App;
