import React from 'react'
import Image from 'next/image'
import WebBG from '@/public/WebBG.jpg'

const page = () => {
  return (
    <section className='w-full h-full p-12 flex flex-col items-center justify-center'>
      <Image src={WebBG} alt="Background Website" className="h-full w-full fixed top-0 left-0 z-[-100] text-[#2F3238]"/>
    </section>
  )
}

export default page