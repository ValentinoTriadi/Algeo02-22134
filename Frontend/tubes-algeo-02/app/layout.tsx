"use client"

import type { Metadata } from 'next'
import './globals.css'
import '@fontsource/poppins'
import Navbar from './(routes)/Navbar/Navbar'
import Footer from './(routes)/Footer/Footer'

const myStyle = {
  fontFamily: 'Poppins, sans-serif',
  fontSize: '16px'
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <title>Go Milk</title>
      <meta name="description" content="Dalam era digital, jumlah gambar yang dihasilkan dan disimpan semakin meningkat dengan pesat, baik dalam konteks pribadi maupun profesional. Peningkatan  ini mencakup berbagai jenis gambar, mulai dari foto pribadi, gambar medis, ilustrasi ilmiah, hingga gambar komersial. Terlepas dari keragaman sumber dan jenis gambar ini, sistem temu balik gambar (image retrieval system) menjadi sangat relevan dan penting dalam menghadapi tantangan ini. Dengan bantuan sistem temu balik gambar, pengguna dapat dengan mudah mencari, mengakses, dan mengelola koleksi gambar mereka. Sistem ini memungkinkan pengguna untuk menjelajahi informasi visual yang tersimpan di berbagai platform, baik itu dalam bentuk pencarian gambar pribadi, analisis gambar medis untuk diagnosis, pencarian ilustrasi ilmiah, hingga pencarian produk berdasarkan gambar komersial. Salah satu contoh penerapan sistem temu balik gambar yang mungkin kalian tahu adalah Google Lens." 
      />
      <meta name="keywords" content="Tubes 2 Algeo" />
        <Navbar />
          <body style={myStyle}>{children}</body>
        <Footer />     
    </html>
  )
}
