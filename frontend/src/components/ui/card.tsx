// components/ui/card.tsx
import * as React from "react"

export function Card({ className = "", children }: React.PropsWithChildren<{ className?: string }>) {
  return (
    <div className={`rounded-2xl shadow-md bg-white p-6 ${className}`}>
      {children}
    </div>
  )
}

export function CardContent({ children }: React.PropsWithChildren<{}>) {
  return <div className="text-gray-700 text-sm"> {children} </div>
}
