"use client"

import React, { useState, useEffect } from 'react';
import Image from 'next/image';
import Webcam from 'react-webcam';
import WebBG from '@/public/WebBG.jpg'

const page = () => {
  const webcamRef = React.useRef(null);
  const [displayed, setDisplayed] = useState('');
  const [countdown, setCountdown] = useState(5);

  useEffect(() => {
    const captureInterval = setInterval(() => {
      if (webcamRef.current) {
        const imageSrc = webcamRef.current.getScreenshot();
        setDisplayed(imageSrc);
        setCountdown(6)
      }
    }, 5000);

    const countdownInterval = setInterval(() => {
      if (countdown > 0) {
        setCountdown((prevCountdown) => prevCountdown - 1); // Menggunakan updater untuk memastikan pembaruan nilai yang benar
      }
    }, 1000);

    return () => {
      clearInterval(captureInterval);
      clearInterval(countdownInterval);
    };
  }, []);

  return (
    <section className='w-full h-full p-12 flex flex-col items-center justify-center'>
      <Image src={WebBG} alt="Background Website" className="h-full w-full fixed top-0 left-0 z-[-100] text-[#2F3238]"/>
      <div className='mt-[75px]' />

      {/* CAMERA */}
      <div className="shadow-xl h-[350px] w-[800px] rounded-xl bg-[#F5F6F9] bg-opacity-10 border-2 border-black border-opacity-5 p-8 flex justify-between items-center backdrop-blur-sm">
        <div className='flex flex-col items-center gap-y-4'>
          <p  className='font-bold text-2xl'>Camera</p>
          {
            <div className='text-4xl font-bold text-white absolute top-[175px]'>
              {countdown}
            </div>
          }
          <Webcam
            audio={false}
            ref={webcamRef}
            height={325}
            width={325}
            className='rounded-xl h-[250px] w-[325px]'
          />
          
        </div>
        <div className='flex flex-col items-center gap-y-4'>
          <p className='font-bold text-2xl'>Result</p>
          <Image
          src={displayed}
          alt="Captured Image"
          height={325}
          width={325}
          className='border-black border-2 border-opacity-5 rounded-xl h-[250px] w-[325px]'
        />
        </div>
      </div>
    </section>
  )
}

export default page