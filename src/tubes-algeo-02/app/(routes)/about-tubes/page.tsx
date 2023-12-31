import React from 'react'
import Image from 'next/image'
import WebBG from '@/public/WebBG.jpg'
import Link from 'next/link'
import { ChevronRight } from 'lucide-react'

const page = () => {
  return (
    <section className='w-full h-full p-12 flex flex-col items-center justify-center text-center'>
      <Image src={WebBG} alt="Background Website" className="h-full w-full fixed top-0 left-0 z-[-100] text-[#2F3238]"/>
      <div className='mt-[125px]' />

      <h1 className='font-bold text-4xl'>About This Tugas Besar</h1>
      <p className='mt-8 w-[800px]'>
        Dalam Tugas Besar 2, Anda diminta untuk mengimplementasikan sistem temu balik gambar dalam bentuk website dengan menggunakan aljabar vektor dan CBIR. Ini memungkinkan pengguna untuk mencari gambar berdasarkan kesamaan nilai citra visual, bukan kata kunci. Dalam konteks ini, Anda akan mengimplementasikan 2 parameter CBIR yang populer. Ini adalah pendekatan penting dalam dunia pemrosesan data dan pencarian informasi. Salah satu contoh aplikasi CBIR yang dikenal adalah Google Lens.
      </p>

      <h1 className='font-bold text-4xl mt-28'>Our Feature</h1>
      <div className='w-[800px]'>
        <h5 className='mt-16 font-bold text-xl text-left'>Content Based Information Retrieval</h5>
        <p className='text-left mt-4'>
          Content-Based Image Retrieval (CBIR) adalah proses untuk mencari dan mengambil gambar berdasarkan kontennya. Ini melibatkan ekstraksi fitur-fitur penting dari gambar, seperti warna, tekstur, dan bentuk. Fitur-fitur ini direpresentasikan sebagai vektor numerik, yang dibandingkan dengan gambar lain dalam dataset. CBIR menggunakan algoritma pencocokan untuk membandingkan vektor-fitur, dan mengurutkan gambar dalam dataset berdasarkan kesamaan dengan gambar yang dicari. CBIR memungkinkan eksplorasi dan akses yang efisien ke koleksi gambar tanpa mengandalkan teks atau kata kunci. Dalam tugas besar ini, Anda akan mengimplementasikan dua parameter CBIR yang populer.
        </p>
        <h5 className='mt-16 font-bold text-xl text-right'>Camera</h5>
        <p className='text-right mt-4'>
          Fitur kamera memungkinkan pengguna menangkap gambar secara real-time menggunakan webcam tanpa tombol pemicu. Ini melibatkan penangkapan gambar dengan interval waktu.
        </p>
        <h5 className='mt-16 font-bold text-xl text-left'>Image Scrapper</h5>
        <p className='text-left mt-4'>
          Fitur scraping memungkinkan ekstraksi gambar dari situs web tertentu untuk digunakan sebagai bagian dari dataset gambar dalam aplikasi.
        </p>
      </div> 

      <h1 className='font-bold text-4xl mt-28'>How To Use</h1>
      <div className='flex mt-16 gap-x-8'>
        <div className='shadow-xl bg-[#F5F6F9] bg-opacity-10 border-opacity-5 p-4 flex flex-col items-center h-[300px] w-[350px] border-2 border-black rounded-xl hover:scale-110 transition-all cursor-pointer'>
          <div className='rounded-full border-black border-opacity-10 border-2 bg-opacity-25 bg-[#F5F6F9] text-black font-bold h-[50px] w-[50px] flex items-center justify-center'>
            1
          </div>
          <p className='mt-12'>
            Mengunggah sebuah gambar dengan format <span className='font-semibold'>.jpg</span> atau <span className='font-semibold'>.jpeg</span> untuk dicari kemiripannya
          </p>
        </div>
        <div className='shadow-xl bg-[#F5F6F9] bg-opacity-10 border-opacity-5 p-4 flex flex-col items-center h-[300px] w-[350px] border-2 border-black rounded-xl hover:scale-110 transition-all cursor-pointer'>
          <div className='rounded-full border-black border-opacity-10 border-2 bg-opacity-25 bg-[#F5F6F9] text-black font-bold h-[50px] w-[50px] flex items-center justify-center'>
            2
          </div>
          <p className='mt-12'>
            Mengunggah <i className='font-semibold'>dataset</i> gambar dalam bentuk folder untuk dijadikan sebagai acuan pencarian
          </p>
        </div> 
        <div className='shadow-xl bg-[#F5F6F9] bg-opacity-10 border-opacity-5 p-4 flex flex-col items-center h-[300px] w-[350px] border-2 border-black rounded-xl hover:scale-110 transition-all cursor-pointer'>
          <div className='rounded-full border-black border-opacity-10 border-2 bg-opacity-25 bg-[#F5F6F9] text-black font-bold h-[50px] w-[50px] flex items-center justify-center'>
            3
          </div>
          <p className='mt-4'>
            Memilih metode pencarian yang diinginkan, yaitu <span className='font-semibold'>pencarian dengan parameter gambar</span> atau <span className='font-semibold'>pencarian dengan parameter tekstur</span>, kemudian menekan tombol <i>Search</i>
          </p>
        </div>       
      </div>

      <Link href='/content-based-information-retrieval'>
        <button className="py-4 px-8 border-[#2F3238] border-2 rounded-full w-[250px] mt-20 bg-[#2F3238] text-white flex justify-center transition-all hover:justify-around hover:scale-105">
          Start Demo!
          <ChevronRight />
        </button>
      </Link>

      <div className='mt-36' />
    </section>
  )
}

export default page