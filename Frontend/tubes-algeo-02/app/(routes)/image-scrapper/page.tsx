"use client"

import React, { ChangeEventHandler, useState } from 'react'
import Image from 'next/image'
import WebBG from '@/public/WebBG.jpg'
import { Input } from '@/components/ui/input'
import { Button } from '@/components/ui/button'
import { StaticImageData } from 'next/image'
import ImagePlaceholder from '@/public/ddummy.png'

const page: React.FC = () => {
  const [imageURL, setImageURL] = useState<string>('');
  const [confirmedImageURL, setConfirmedImageURL] = useState<string | null>(null);

  const handleImageInput = (e: React.ChangeEvent<HTMLInputElement>) => {
    setImageURL(e.target.value);
  };

  const confirmImage = () => {
    setConfirmedImageURL(imageURL);
  };

  return (
    <section className='w-full h-full p-12 flex flex-col items-center justify-center'>
      <Image src={WebBG} alt="Background Website" className="h-full w-full fixed top-0 left-0 z-[-100] text-[#2F3238]"/>
      <div className='mt-[75px]' />

      {/* IMAGE SCRAPPER */}
      <div className="shadow-xl h-[400px] w-[800px] rounded-xl bg-[#F5F6F9] bg-opacity-10 border-2 border-black border-opacity-5 p-8 flex items-center backdrop-blur-sm flex-row justify-between">
        <Image src={imageURL} alt="Place Image Here" height={325} width={325} className='border-black border-2 border-opacity-5 rounded-xl h-[325px] w-[325px]' />
        <div className='flex flex-col gap-y-4'>
          <Input
            type='text'
            placeholder='Masukkan URL gambar'
            value={imageURL}
            onChange={handleImageInput}
          />
          <Button onClick={confirmImage}>
            Tambahkan Gambar
          </Button>
        </div>
      </div>
      {/* RESULT */}
    </section>
  )
}

export default page