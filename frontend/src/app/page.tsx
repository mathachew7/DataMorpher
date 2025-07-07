"use client";

import { useRouter } from "next/navigation";

export default function Home() {
  const router = useRouter();

  return (
    <div className="max-w-7xl mx-auto px-4 py-12 space-y-16">
      {/* Hero Section */}
      <section className="text-center">
        <h1 className="text-5xl font-extrabold text-slate-800">Welcome to DataMorpher</h1>
        <p className="mt-4 text-lg text-gray-600 max-w-2xl mx-auto">
          A powerful data ingestion tool by Josla Tech to upload your files directly into a database.
        </p>
        <button
          onClick={() => router.push("/ingestion")}
          className="mt-6 bg-teal-600 hover:bg-teal-700 text-white px-8 py-3 rounded-lg text-lg shadow"
        >
          Get Started
        </button>
      </section>

      {/* Feature Cards */}
      <section className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
        {[
          {
            title: "Upload Files",
            desc: "Send CSV, JSON, Excel, or XML files directly to SQL Server or MySQL.",
            link: "/ingestion/upload",
          },
          {
            title: "View Logs",
            desc: "Monitor upload activity and status in real-time.",
            link: "/ingestion/logs",
          },
          {
            title: "Ask Anything",
            desc: "AI-powered query assistant (coming soon).",
            link: "/ask",
          },
        ].map((f, i) => (
          <div
            key={i}
            onClick={() => router.push(f.link)}
            className="cursor-pointer bg-slate-50 hover:bg-slate-100 rounded-xl shadow-md p-6 transition-all"
          >
            <h3 className="text-xl font-semibold text-teal-700">{f.title}</h3>
            <p className="text-gray-600 mt-2">{f.desc}</p>
          </div>
        ))}
      </section>

      {/* How It Works */}
      <section className="bg-white border rounded-xl shadow p-8 text-center space-y-6">
        <h2 className="text-3xl font-bold text-slate-800">⚙️ How It Works</h2>
        <div className="flex flex-col md:flex-row justify-center items-center gap-6 mt-4">
          <Step title="1️⃣ Connect Your Database" />
          <Arrow />
          <Step title="2️⃣ Choose File Type (CSV, JSON, Excel, XML)" />
          <Arrow />
          <Step title="3️⃣ Upload & Confirm" />
          <Arrow />
          <Step title="✅ Data Goes Straight Into Your DB" />
        </div>
        <p className="text-sm text-gray-500">No bullshit. Just connect and dump data into your database 🔥</p>
      </section>
    </div>
  );
}

function Step({ title }: { title: string }) {
  return (
    <div className="bg-teal-50 text-teal-800 px-4 py-3 rounded-lg w-60 shadow border border-teal-200">
      <p className="font-semibold">{title}</p>
    </div>
  );
}

function Arrow() {
  return <span className="text-2xl hidden md:inline">➡️</span>;
}
