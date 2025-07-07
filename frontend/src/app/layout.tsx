// src/app/layout.tsx
import "./globals.css"
import { Inter } from "next/font/google"
import { Header } from "../components/Header"
import { Footer } from "../components/Footer"

const inter = Inter({ subsets: ["latin"] })

export const metadata = {
  title: "DataMorpher",
  description: "Upload your files directly to the database. Supports CSV, Excel, JSON, and XML.",
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className={`${inter.className} bg-gray-50 text-neutral-900`}>
        <Header />
        <main className="min-h-screen px-4 md:px-10 py-8">
          {children}
        </main>
        <Footer />
      </body>
    </html>
  )
}
