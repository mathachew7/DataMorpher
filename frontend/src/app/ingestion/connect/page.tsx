'use client'

import DatabaseConnectionForm from "@/components/DatabaseConnectionForm"

export default function MySQLConnectionPage() {
  return (
    <div className="max-w-4xl mx-auto py-10 px-4">
      <h1 className="text-3xl font-bold mb-6">Connect to MySQL</h1>
      <DatabaseConnectionForm />
    </div>
  )
}
