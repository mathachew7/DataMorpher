"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";

export default function DatabaseConnectionForm() {
  const router = useRouter();
  const [form, setForm] = useState({
    host: "",
    port: "",
    user: "",
    password: "",
    database: "",
    dbType: "",
  });

  const [loading, setLoading] = useState(false);
  const [status, setStatus] = useState<null | string>(null);
  const [showSuccess, setShowSuccess] = useState(false);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async () => {
    if (!form.dbType) {
      setStatus("❌ Please select a database type.");
      return;
    }

    setLoading(true);
    setStatus(null);
    try {
      const res = await fetch("http://localhost:5050/connect", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(form),
      });

      const data = await res.json();
      if (data.message?.toLowerCase().includes("success")) {
        setStatus("✅ Connection successful!");
        localStorage.setItem("db_connection", JSON.stringify(form));
        setShowSuccess(true);
        setTimeout(() => {
          router.push("/ingestion/upload");
        }, 1500);
      } else {
        setStatus("❌ Connection failed: " + (data.message || "Check credentials"));
      }
    } catch (error) {
      setStatus("❌ Error: " + error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-xl mx-auto space-y-6 bg-white p-6 rounded-xl shadow-md border relative">
      <h2 className="text-xl font-semibold text-neutral-800">Connect to Your Database</h2>

      <div className="space-y-4">
        <select
          name="dbType"
          value={form.dbType}
          onChange={handleChange}
          className="w-full border p-2 rounded"
        >
          <option value="">Select DB Type</option>
          <option value="mysql">MySQL Server</option>
          <option value="mssql">SQL Server</option>
        </select>

        {form.dbType && (
          <p className="text-sm text-gray-500">
            Selected DB Type: <strong>{form.dbType === "mysql" ? "MySQL" : "SQL Server"}</strong>
          </p>
        )}

        <input
          name="host"
          placeholder="Host (e.g. localhost)"
          value={form.host}
          onChange={handleChange}
          className="w-full border p-2 rounded"
        />
        <input
          name="port"
          placeholder="Port (e.g. 1433 or 3306)"
          value={form.port}
          onChange={handleChange}
          className="w-full border p-2 rounded"
        />
        <input
          name="user"
          placeholder="Username"
          value={form.user}
          onChange={handleChange}
          className="w-full border p-2 rounded"
        />
        <input
          name="password"
          type="password"
          placeholder="Password"
          value={form.password}
          onChange={handleChange}
          className="w-full border p-2 rounded"
        />
        <input
          name="database"
          placeholder="Database Name"
          value={form.database}
          onChange={handleChange}
          className="w-full border p-2 rounded"
        />
      </div>

      <button
        onClick={handleSubmit}
        disabled={loading}
        className="bg-black text-white px-6 py-2 rounded hover:bg-neutral-800 transition"
      >
        {loading ? "Connecting..." : "Connect"}
      </button>

      {status && !showSuccess && <p className="text-sm mt-2">{status}</p>}

      {showSuccess && (
        <div className="absolute inset-0 flex items-center justify-center bg-white bg-opacity-90 transition-opacity duration-700">
          <div className="text-green-600 text-lg font-medium">✅ Connected Successfully! Redirecting...</div>
        </div>
      )}
    </div>
  );
}
