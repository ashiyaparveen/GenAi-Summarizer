import React, { useState } from "react";

const API_BASE_URL = "http://127.0.0.1:5000";


function SummaryForm() {
  const [url, setUrl] = useState("");
  const [summary, setSummary] = useState("");

  const handleSummarize = async () => {
    const response = await fetch(`${API_BASE_URL}/summarize`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        user_id: "nafi123",
        url: url
      })
    });

    const data = await response.json();
    setSummary(data.summary); // set state to show on UI
  };

  return (
    <div className="p-4">
      <input
        type="text"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        placeholder="Enter article URL"
        className="p-2 border rounded w-full mb-2"
      />
      <button onClick={handleSummarize} className="bg-blue-500 text-white px-4 py-2 rounded">
        Summarize
      </button>
      {summary && (
        <div className="mt-4 p-4 bg-gray-100 rounded">
          <h2 className="font-bold">Tailored Summary:</h2>
          <p>{summary}</p>
        </div>
      )}
    </div>
  );
}

export default SummaryForm;
