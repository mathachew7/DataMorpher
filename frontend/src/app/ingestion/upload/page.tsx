"use client"

import { useEffect, useState } from "react"
import { useRouter } from "next/navigation"

const API_BASE = process.env.NEXT_PUBLIC_API_BASE_URL

export default function UploadPage() {
  const [connection, setConnection] = useState<any>(null)
  const [files, setFiles] = useState<FileList | null>(null)
  const [fileType, setFileType] = useState("csv")
  const [status, setStatus] = useState<string | null>(null)
  const [fadeOut, setFadeOut] = useState(false)
  const [showCard, setShowCard] = useState(false)
  const router = useRouter()

  useEffect(() => {
    const conn = localStorage.getItem("db_connection")
    if (conn) {
      try {
        const parsed = JSON.parse(conn)
        const ageSeconds = (Date.now() - parsed.timestamp) / 1000
        if (ageSeconds > 3600) {
          localStorage.removeItem("db_connection")
          router.push("/ingestion")
        } else {
          setConnection(parsed)
        }
      } catch (err) {
        localStorage.removeItem("db_connection")
        router.push("/ingestion")
      }
    } else {
      setTimeout(() => router.push("/ingestion"), 2000)
    }
  }, [router])

  const handleUpload = async () => {
    if (!files || files.length === 0) return setStatus("❌ No files selected")

    const formData = new FormData()
    Array.from(files).forEach(file => {
      formData.append("file", file)
    })

    formData.append("db_connection", JSON.stringify({
      host: connection.host,
      port: connection.port,
      user: connection.user,
      password: connection.password,
      database: connection.database,
      dbType: connection.dbType
    }))

    setStatus("⏳ Uploading...")

    try {
      const res = await fetch(`${API_BASE}/upload/${fileType}`, {
        method: "POST",
        body: formData,
      })
      const data = await res.json()

      if (res.ok) {
        setStatus(null)
        setShowCard(true)
        setTimeout(() => {
          setFadeOut(true)
          router.push("/")
        }, 2000)
      } else {
        setStatus(`❌ Upload failed: ${data?.error || "Unknown error"}`)
      }
    } catch (err: any) {
      setStatus(`❌ Error: ${err.message || err}`)
    }
  }

  if (!connection) {
    return (
      <div className="max-w-lg mx-auto text-center mt-20 space-y-4">
        <p className="text-red-600 text-lg">❌ No valid database connection. Redirecting...</p>
      </div>
    )
  }

  return (
    <div className="max-w-6xl mx-auto p-6 grid grid-cols-1 md:grid-cols-4 gap-6 relative">
      <div className="md:col-span-1 bg-white shadow rounded-lg p-4 space-y-2 border">
        <h2 className="text-lg font-semibold">Connected Database</h2>
        <p><strong>Type:</strong> {connection.dbType}</p>
        <p><strong>Host:</strong> {connection.host}</p>
        <p><strong>Port:</strong> {connection.port}</p>
        <p><strong>User:</strong> {connection.user}</p>
        <p><strong>Database:</strong> {connection.database}</p>
      </div>

      <div className="md:col-span-3 bg-white shadow rounded-lg p-6 space-y-4 border">
        <h2 className="text-xl font-bold text-neutral-800">Upload Files to Database</h2>

        <select
          value={fileType}
          onChange={(e) => setFileType(e.target.value)}
          className="w-full border p-2 rounded"
        >
          <option value="csv">CSV</option>
          <option value="json">JSON</option>
          <option value="xml">XML</option>
          <option value="excel">Excel</option>
        </select>

        <input
          type="file"
          multiple
          accept={
            fileType === "csv"
              ? ".csv"
              : fileType === "json"
              ? ".json"
              : fileType === "xml"
              ? ".xml"
              : ".xls,.xlsx"
          }
          onChange={(e) => setFiles(e.target.files)}
          className="w-full border p-2 rounded"
        />

        <button
          onClick={handleUpload}
          className="bg-black text-white px-6 py-2 rounded hover:bg-neutral-800 transition"
        >
          Upload
        </button>

        {status && (
          <p
            className={`text-sm mt-2 transition-opacity duration-500 ${
              fadeOut ? "opacity-0" : "opacity-100"
            }`}
          >
            {status}
          </p>
        )}
      </div>

      {showCard && (
        <div className="absolute top-10 left-1/2 -translate-x-1/2 bg-green-500 text-white px-6 py-3 rounded-xl shadow-lg transition-opacity duration-500">
          ✅ Upload successful! Redirecting...
        </div>
      )}
    </div>
  )
}
