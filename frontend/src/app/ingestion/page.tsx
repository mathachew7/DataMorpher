"use client"

import { useRouter } from "next/navigation"

export default function IngestionPage() {
  const router = useRouter()

  const features = [
    {
      title: "Connect MySQL or MSSQL",
      desc: "Securely connect your local or remote SQL database",
      link: "/ingestion/connect", // connection form is here
    },
    {
      title: "Upload Data",
      desc: "Upload CSV, JSON, Excel, or XML files into your connected DB",
      link: "/ingestion/upload",
    },
  ]

  return (
    <div className="max-w-5xl mx-auto py-12 px-4 space-y-10">
      <h1 className="text-4xl font-bold text-center text-slate-800">Data Ingestion</h1>
      <p className="text-center text-gray-600">Start by connecting your database, then upload any supported file type.</p>

      <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
        {features.map((item, i) => (
          <div
            key={i}
            onClick={() => router.push(item.link)}
            className="cursor-pointer border border-slate-200 bg-white hover:bg-slate-50 shadow-sm rounded-xl p-6 transition"
          >
            <h3 className="text-xl font-semibold text-indigo-700">{item.title}</h3>
            <p className="text-gray-600 mt-2 text-sm">{item.desc}</p>
          </div>
        ))}
      </div>
    </div>
  )
}
