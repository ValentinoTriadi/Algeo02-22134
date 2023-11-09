import Image from "next/image"
import WebBG from '@/public/WebBG.jpg'
import { ChevronRight } from 'lucide-react'
import Link from "next/link"

export default function Home() {
  return (
    <main className='w-full h-full p-12 flex flex-col items-center justify-center'>
      <Image src={WebBG} alt="Background Website" className="h-full w-full fixed top-0 left-0 z-[-100] text-[#2F3238]"/>
      <div className='mt-[150px]' />
      <h1 className="text-center font-semibold text-4xl">Tugas Besar 2 IF2123</h1>
      <h1 className="text-center font-semibold text-4xl mt-6">Aljabar Linier dan Geometri</h1>
      <h1 className="text-center font-semibold text-3xl mt-6">Aplikasi Aljabar Vektor dalam Sistem Temu Balik Gambar</h1>
      <Link href='/about-tubes'>
        <button className="py-4 px-8 border-[#2F3238] border-2 rounded-full w-[250px] mt-12 bg-[#2F3238] text-white flex justify-center transition-all hover:justify-around hover:scale-105">
          Let's Get Started!
          <ChevronRight />
        </button>
      </Link>

      <div className="mt-[200px]"/>
      <div className="flex flex-col items-center gap-y-4 mt-[50px] mb-[250px]">
        <h3 className="text-3xl font-bold">Developed By:</h3>
        <div className="flex flex-col gap-y-2 text-center">
          <p>Shabrina Maharani 13522134</p>
          <p>Atqiya Haydar Luqman 13522163</p>
          <p>Valentino Chryslie Triadi 13522164</p>
        </div>
      </div>
    </main>
  )
}
