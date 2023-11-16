"use client"

import Image, { StaticImageData } from 'next/image'
import { useState, useRef, ChangeEvent, useEffect } from 'react'
import WebBG from '@/public/WebBG.jpg'
import ImagePlaceholder from '@/public/ddummy.png'
import { Button } from '@/components/ui/button'
import { Switch } from '@/components/ui/switch'
import ReactPaginate from 'react-paginate'
import Webcam from 'react-webcam'
import { Input } from '@/components/ui/input'
import axios from "axios"

const page: React.FC = () => {
  const [displayed, setDisplayed] = useState<StaticImageData>(ImagePlaceholder)
  const [displayedName, setDisplayedName] = useState<String>('')
  const [textureEnabled, setTextureEnabled] = useState(false)
  const [uploadedFiles, setUploadedFiles] = useState<FileList | null>(null);
  const [currentPage, setCurrentPage] = useState(0); // Menyimpan halaman saat ini
  const [tools, setTools] = useState('Lens')
  const [formData, setFormData] = useState(new FormData());
  const [fileImage, setFileImage] = useState<File | null>(null);
  const [isProcessed, setIsProcessed] = useState(false);
  const [timeProcess, setTimeProcess] = useState(0.0);

  const itemsPerPage = 9; // Jumlah gambar per halaman (diubah menjadi 6)

  const fileInputRef = useRef<HTMLInputElement | null>(null);
  const folderInputRef = useRef<HTMLInputElement | null>(null);

  // Paginasi
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

  // Mengunggah gambar
  const imageHandler = () => {
    if (fileInputRef.current) {
      fileInputRef.current.click();
    }
  }
  
  const inputImageHandler = async (e: ChangeEvent<HTMLInputElement>) => {
    if (e.target.files) {
      const file = e.target.files[0];
      if (file) {
        const imgUrl = URL.createObjectURL(file);
        setDisplayed(imgUrl);
        setDisplayedName(file.name.substring(0, 15));
        setFileImage(file);
      }
    }
  }

  // Mengunggah dataset ke FastAPI
  const uploadDatasetHandler = async () => {
    if (folderInputRef.current) {
      folderInputRef.current.click();
    }
  };

  // Mengunggah dataset
  const handleDatasetInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files) {
      // setUploadedFiles(e.target.files);
      setIsProcessed(false);
    }

    if (e.target.files) {
      const formData = new FormData();
      const files  = e.target.files;

      for (let i = 0; i < files.length; i++) {
        formData.append('files', files[i]);
      }

      console.log(formData);

      axios.post('http://localhost:8000/uploadfiles', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      })
    }
  };

  // Fungsi mencari
  const searchHandler = async () => {
    if (fileImage) {
      console.log("SEARCHING");
      
      const requests = {
        method: "GET",
        headers:{'Content-Type': 'application/json'}
      }
      
      if (!isProcessed) {
        let response;
        if (!textureEnabled) {
          response = await fetch("http://127.0.0.1:8000/proses-warna/", requests);
        } else {
          response = await fetch("http://127.0.0.1:8000/proses-tekstur/", requests);
        }

        const data = await response.json();
        const keysdata = Object.keys(data)[0];
        const value = data[keysdata]

        if (value == "Complete") {
          console.log("PROCESSED");
          setIsProcessed(true);
        }

        // const fileList = Object.keys(response).map((key) => {
        //   // const url = `localhost:8000/static/dataset/${key}`
        //   const url = `../../api/static/dataset/${key}`
        //   const file = new File(url, key, { type: "image/jpeg" });
        //   return file;
        // });

        // console.log(fileList);
        // setUploadedFiles(fileList);
      }

      const formData = new FormData();
      const file = fileImage;

      formData.append(
        'file', 
        file,
        file.name,
      );
      formData.append(
        'namafile', 
        file.name,
      );

      const requestOptions = {
        method: "POST",
        body: formData,
        // headers:{'Content-Type': 'application/json'}
      }

      try {
        if (!textureEnabled) {
          const response = await axios.post("http://localhost:8000/search-warna", formData, requestOptions);

          console.log(response);
          console.log("CBIR WITH COLOR");
        } else {
          const response = await axios.post("http://localhost:8000/search-tekstur", formData, requestOptions);

          console.log(response);
          console.log("CBIR WITH TEXTURE");
        }
      } catch (error) {
        console.error(error);
      }
      const hasil = await fetch("http://127.0.0.1:8000/hasil/", requests)
      const cek = await hasil.json();
      const cekJson = JSON.parse(cek);
      const b = Object.keys(cekJson);
      console.log(b);
      console.log(cekJson);
      console.log("SEARCHED");
     
      const fileList = [];
      for (const key of Object.keys(cekJson)) {
        if (key == "Time"){
          setTimeProcess(cekJson[key]);
        } else {
          const url = `http://localhost:8000/static/dataset/${key}`;
          const response = await fetch(url);
          const blob = await response.blob();
          const file = new File([blob], key, { type: "image/jpeg" });
          fileList.push(file);
        }
      }

      console.log(fileList);
      setUploadedFiles(fileList);
    }
  }

  return (
    <section className='w-full h-full p-12 flex flex-col items-center justify-center'>
      <Image src={WebBG} alt="Background Website" className="h-full w-full fixed top-0 left-0 z-[-100] text-[#2F3238]"/>
      <div className='mt-[75px]' />

      <div className='flex gap-x-20 text-xl font-bold mb-8'>
        <p onClick={() => setTools('Lens')} className='cursor-pointer hover:scale-125 transition-all'>Lens</p>
        <p onClick={() => setTools('Camera')} className='cursor-pointer hover:scale-125 transition-all'>Camera</p>
        <p onClick={() => setTools('Scrapper')} className='cursor-pointer hover:scale-125 transition-all'>Scrapper</p>
      </div>

      {/* LENS INPUT */}
      {
        tools == 'Lens' && (
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
        )
      }
      
      {/* RESULT IMAGE */}
      <Button className='mt-12 px-12 py-6' onClick={uploadDatasetHandler}>
        Upload Dataset
      </Button>
      <div>
        <input
          className='hidden'
          type="file"
          multiple
          onChange={handleDatasetInputChange}
          ref={folderInputRef}
        />
      </div>
      <div className='shadow-xl h-[800px] w-[800px] rounded-xl bg-[#F5F6F9] bg-opacity-10 border-2 border-black border-opacity-5 p-8 flex justify-between mt-12 backdrop-blur-sm'>
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

export default page;