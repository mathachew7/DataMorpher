"use client";

import { useState } from "react";

export default function UploadPanel() {
  const [ip, setIp] = useState("sql_server");
  const [db, setDb] = useState("datamorpher");
  const [status, setStatus] = useState("");

  const handleConnect = async () => {
    setStatus("Connecting...");
    const res = await fetch("http://localhost:5050/connect", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ ip, db_name: db }),
    });
    const data = await res.json();
    setStatus(data.message || data.error);
  };

  const uploadCSV = async () => {
    setStatus("Uploading...");
    const res = await fetch("http://localhost:5050/upload/csv", {
      method: "POST",
    });
    const data = await res.json();
    setStatus(data.message || data.error);
  };

  return (
    <div className="space-y-4 bg-white p-6 rounded shadow">
      <div className="space-y-2">
        <input
          className="border px-2 py-1 w-full"
          placeholder="DB IP"
          value={ip}
          onChange={(e) => setIp(e.target.value)}
        />
        <input
          className="border px-2 py-1 w-full"
          placeholder="Database Name"
          value={db}
          onChange={(e) => setDb(e.target.value)}
        />
      </div>
      <button onClick={handleConnect} className="bg-blue-600 text-white px-4 py-2 rounded">
        Connect to DB
      </button>
      <button onClick={uploadCSV} className="bg-green-600 text-white px-4 py-2 rounded">
        Upload CSVs
      </button>
      <div className="text-sm mt-2 text-gray-700">{status}</div>
    </div>
  );
}
