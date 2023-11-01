"use client"

import type { Metadata } from 'next'
import './globals.css'
import '@fontsource/poppins'

// Use Popping Font
const myStyle = {
  fontFamily: 'Poppins, sans-serif',
  fontSize: '16px'
}

// Import Components
import Navbar from './(routes)/Navbar/Navbar'
import Footer from './(routes)/Footer/Footer'
import { useEffect, useState } from 'react'
import Loader from 'react-spinners/RingLoader'

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  const [loading, setLoading] = useState(false)
  useEffect(() => {
    setLoading(true);
    setTimeout(() => {
      setLoading(false);
    }, 1250)
  }, [])

  return (
    <html lang="en">
      {
        loading ? (
          <div style={myStyle} className='bg-black flex flex-col items-center justify-center w-full h-screen'>
            <Loader loading={loading} color='#FFFFFF' size='250' />
            <h1 className='text-4xl mt-[50px] text-white font-semibold'>Loading...</h1>
          </div>
        ) : (
          <body style={myStyle}>{children}</body>
        )
      }
    </html>
  )
}
