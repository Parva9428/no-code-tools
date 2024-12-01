import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import './globals.css'
import ThemeWrapper from '../components/ThemeWrapper'

const inter = Inter({
  subsets: ['latin'],
  display: 'swap',
  variable: '--font-inter',
})

export const metadata: Metadata = {
  title: 'No-Code Tools Directory',
  description: 'A comprehensive directory of no-code development tools',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" className={inter.variable}>
      <body>
        <ThemeWrapper>
          {children}
        </ThemeWrapper>
      </body>
    </html>
  )
}
