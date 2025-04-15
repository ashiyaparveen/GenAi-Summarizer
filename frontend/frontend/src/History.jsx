import React, { useEffect, useState } from "react";

const API_BASE_URL = "http://localhost:5000";

function History({ userId }) {
  const [history, setHistory] = useState([]);

  useEffect(() => {
    if (!userId) return;

    const fetchHistory = async () => {
      const response = await fetch(`${API_BASE_URL}/history?user_id=${userId}`);
      const data = await response.json();
      setHistory(data.history);
    };

    fetchHistory();
  }, [userId]);

  return (
    <div className="mt-4">
      <h2 className="text-lg font-bold mb-2">Summary History</h2>
      {history.map((entry, index) => (
        <div key={index} className="mb-4 p-4 bg-gray-100 rounded">
          <p className="text-sm text-gray-600">
            <strong>Date:</strong> {new Date(entry.created_at).toLocaleString()}
          </p>
          <p><strong>Summary:</strong> {entry.summary}</p>
        </div>
      ))}
    </div>
  );
}

export default History;
