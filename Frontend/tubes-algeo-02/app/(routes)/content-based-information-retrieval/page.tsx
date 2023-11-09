"use client"

import Image, { StaticImageData } from 'next/image'
import { useState, useRef, ChangeEvent } from 'react'

import WebBG from '@/public/WebBG.jpg'
import ImagePlaceholder from '@/public/ddummy.png'
import { Button } from '@/components/ui/button'
import { Switch } from '@/components/ui/switch'
import ReactPaginate from 'react-paginate'

const page: React.FC = () => {
  const [displayed, setDisplayed] = useState<StaticImageData>(ImagePlaceholder)
  const [displayedName, setDisplayedName] = useState<String>('')
  const [textureEnabled, setTextureEnabled] = useState(false)
  const [uploadedFiles, setUploadedFiles] = useState<FileList | null>(null);
  const [currentPage, setCurrentPage] = useState(0); // Menyimpan halaman saat ini

  const itemsPerPage = 6; // Jumlah gambar per halaman (diubah menjadi 6)

  const fileInputRef = useRef<HTMLInputElement | null>(null);
  const folderInputRef = useRef<HTMLInputElement | null>(null);

  const imageHandler = () => {
    if (fileInputRef.current) {
      fileInputRef.current.click();
    }
  }
  
  const inputImageHandler = (e: ChangeEvent<HTMLInputElement>) => {
    if (e.target.files) {
      const file = e.target.files[0];
      if (file) {
        const imgUrl = URL.createObjectURL(file);
        setDisplayed(imgUrl);
        setDisplayedName(file.name.substring(0, 15));
      }
    }
  }

  const uploadFile = async (file: File) => {
    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch("/api/upload/", {
        method: "POST",
        body: formData,
      });

      if (response.ok) {
        const data = await response.json();
        console.log("Berhasil mengunggah file:", data);
        // Di sini, Anda dapat menangani respons dari backend, misalnya, menampilkan hasil perhitungan kemiripan gambar.
      } else {
        console.error("Gagal mengunggah file.");
      }
    } catch (error) {
      console.error("Terjadi kesalahan:", error);
    }
  }

  const uploadDatasetHandler = () => {
    const fileInput = document.createElement('input');
    fileInput.type = 'file';
    fileInput.accept = 'image/*'; // Hanya menerima file gambar
    fileInput.multiple = true; // Memungkinkan pengguna memilih beberapa file
    fileInput.addEventListener('change', handleFileUpload);
    fileInput.click();
  };

  const handleFileUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    const selectedFiles = e.target.files;

    if (selectedFiles) {
      // Lakukan apa pun yang Anda inginkan dengan file yang diunggah di sini
      setUploadedFiles(selectedFiles);
      setCurrentPage(0);

      Array.from(selectedFiles).forEach((file) => {
        uploadFile(file);
      });
    }
  };

  const pageCount = Math.ceil((uploadedFiles?.length || 0) / itemsPerPage);

  const displayedFiles = uploadedFiles
    ? Array.from(uploadedFiles).slice(
        currentPage * itemsPerPage,
        (currentPage + 1) * itemsPerPage
      )
    : [];

  const handlePageClick = (data: { selected: number }) => {
    setCurrentPage(data.selected);
  };

  const searchHandler = () => {

  }

  return (
    <section className='w-full h-full p-12 flex flex-col items-center justify-center'>
      <Image src={WebBG} alt="Background Website" className="h-full w-full fixed top-0 left-0 z-[-100] text-[#2F3238]"/>
      <div className='mt-[75px]' />

      {/* INPUT IMAGE */}
      <div className='shadow-xl h-[400px] w-[800px] rounded-xl bg-[#F5F6F9] bg-opacity-10 border-2 border-black border-opacity-5 backdrop-blur-sm p-8 flex justify-between'>
        <Image src={displayed} alt="Place Image Here" height={325} width={325} className='border-black border-2 border-opacity-5 rounded-xl h-[325px] w-[325px]' />
        <div className='flex flex-col justify-between'>
          <div className='flex flex-col gap-y-4 items-center'>
            <p>Image Input</p>
            <Button className='w-[200px]' onClick={imageHandler}>
              Insert an Image
            </Button>
            <p>{displayedName}</p>
            <div className='hidden'>
              <input 
                id='picture'
                type='file'
                
                ref={fileInputRef}
                onChange={inputImageHandler} 
              />
            </div>
          </div>
          <div className='flex flex-col gap-y-4 items-center'>
            <div className='flex gap-x-4'>
              <p>Color</p>
                <Switch onChange={() => setTextureEnabled(!textureEnabled)} />
              <p>Texture</p>
            </div>
            <Button className='w-[200px]' onClick={searchHandler}>
              Search
            </Button>
          </div>
        </div>
      </div>

      {/* RESULT IMAGE */}
      <Button className='mt-12 px-12 py-6' onClick={uploadDatasetHandler}>
        Upload Dataset
      </Button>
      <div className='shadow-xl h-[550px] w-[800px] rounded-xl bg-[#F5F6F9] bg-opacity-10 border-2 border-black border-opacity-5 p-8 flex justify-between mt-12 backdrop-blur-sm'>
      {displayedFiles.length > 0 && (
          <div className='grid grid-cols-3 items-center justify-center'>
            {displayedFiles.map((file, index) => (
              <Image
                key={index}
                src={URL.createObjectURL(file)}
                alt={`Uploaded Image ${index}`}
                width={225}
                height={225}
                className='h-[225px] w-[225px] mx-4 rounded-xl'
              />
            ))}
          </div>
        )}
      </div>
      {uploadedFiles && pageCount > 1 && (
        <div className='flex justify-center space-x-2 mt-4'>
          <ReactPaginate
            previousLabel={'Previous'}
            nextLabel={'Next'}
            pageCount={pageCount}
            marginPagesDisplayed={2}
            pageRangeDisplayed={5}
            onPageChange={handlePageClick}
            containerClassName={'pagination'}
            subContainerClassName={'pages pagination'}
            activeClassName={'active'}
            pageClassName={'w-[50px] flex items-center justify-center bg-[#F5F6F9] bg-opacity-10 border-2 border-black border-opacity-5 p-2 rounded-xl font-bold'} // Kelas untuk nomor halaman
            previousClassName={'w-[150px] flex items-center justify-center bg-[#F5F6F9] bg-opacity-10 border-2 border-black border-opacity-5 p-2 rounded-xl font-bold'} // Kelas untuk tombol "Previous"
            nextClassName={'w-[150px] flex items-center justify-center bg-[#F5F6F9] bg-opacity-10 border-2 border-black border-opacity-5 p-2 rounded-xl font-bold'} // Kelas untuk tombol "Next"
          />
        </div> 
      )}
    </section>
  )
}

export default page