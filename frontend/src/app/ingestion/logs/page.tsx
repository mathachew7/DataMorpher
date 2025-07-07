"use client"

import { useEffect, useState } from "react"

export default function LogsPage() {
  const [logs, setLogs] = useState<string[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetch(`${process.env.NEXT_PUBLIC_API_BASE_URL}/logs`)
      .then((res) => res.json())
      .then((data) => {
        const reversedLogs = data.logs?.map((l: any) => l.line).reverse().slice(0, 50)
        setLogs(reversedLogs || [])
      })
      .catch(() => setLogs([]))
      .finally(() => setLoading(false))
  }, [])

  return (
    <div className="max-w-5xl mx-auto px-4 py-10">
      <h1 className="text-3xl font-bold mb-6 text-neutral-800 text-center">📜 System Logs</h1>

      {loading ? (
        <p className="text-center text-sm text-gray-500">Loading logs...</p>
      ) : logs.length === 0 ? (
        <p className="text-center text-red-500">❌ No logs found.</p>
      ) : (
        <div className="bg-white border rounded-lg shadow p-4 space-y-2 max-h-[600px] overflow-y-auto text-sm font-mono">
          {logs.map((line, i) => (
            <div key={i} className="text-gray-700">
              {line}
            </div>
          ))}
        </div>
      )}
    </div>
  )
}
