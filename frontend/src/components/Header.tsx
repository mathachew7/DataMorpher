// src/components/Header.tsx
'use client'

import Link from "next/link"

export function Header() {
  return (
    <header className="w-full bg-blue-50 border-b border-blue-200 shadow-sm py-4 px-6 flex items-center justify-between">
      <Link href="/" className="text-2xl font-bold text-blue-900 hover:text-blue-700 transition-colors">
        Josla Tech
      </Link>
      <nav className="space-x-6 text-sm font-medium text-blue-600">
        <Link href="/">Home</Link>
        <Link href="/ingestion/connect">Connect</Link>
        <Link href="/ingestion/logs">Logs</Link>
        <Link href="/docs">Docs</Link>
      </nav>
    </header>
  )
}
