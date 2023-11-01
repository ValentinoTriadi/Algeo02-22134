"use client"

import { ChangeEvent, useState, useEffect, useRef } from "react"
import Image from "next/image"
import { Button } from "@/components/ui/button"
import { Switch } from "@/components/ui/switch"
import { Input } from "@/components/ui/input"
import { StaticImageData } from "next/image"
import dummy from '@/public/dummy.png'

const CBIR: React.FC = () => {
  const [imageUrl, setImageUrl] = useState<StaticImageData>(dummy);
  const [imageName, setImageName] = useState('');
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [namaFile, setNamaFile] = useState<string | null>(null);

  const fileInputRef = useRef<HTMLInputElement | null>(null);

  const handleButtonClick = () => {
    if (fileInputRef.current) {
      fileInputRef.current.click();
    }
  }

  const inputImageHandler = (e: ChangeEvent<HTMLInputElement>) => {
    if (e.target.files) {
      const file = e.target.files[0];
      if (file) {
        setImageName(file.name);
        const imgUrl = URL.createObjectURL(file);
        setImageUrl(imgUrl); // Hiraukan ini
      }
    }
  }
  
  const switchHandler = () => {
    return;
  }
  
  const searchHandler = () => {
    return;
  }

  const fileChangeHandler = (e: ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files.length > 0) {
      const file = e.target.files[0];
      setSelectedFile(file);
      setNamaFile(file.name);
      console.log(file);
    }
  }
  
  const uploadDatasetHandler = (e: ChangeEvent<HTMLInputElement>) => {
    e.preventDefault();
    console.log(namaFile);

    if (!selectedFile) {
      console.error("No file selected");
      return;
    }

    const formData = new FormData();
    formData.append("file", selectedFile, selectedFile.name);
    formData.append("namafile", namaFile);

    const requestOptions: RequestInit = {
      method: "POST",
      body: formData,
    }

    fetch("http://127.0.0.1:8000/upload/", requestOptions)
    .then(response => response.json())
    .then(function(response){
      console.log(response);
    })
    .catch(error => {
      console.error("Error:", error);
    });
  }

  return (
    <section className='w-full flex flex-col items-center py-8 justify-center'>
      <h1 className='text-2xl md:text-3xl py-4 font-semibold text-center'>Reverse Image Search</h1>

      <div className="flex flex-col md:flex-row gap-x-[50px] mt-[75px] justify-between gap-y-8 px-4">

        {/* IMAGE */}
        <div className="border-2 border-black rounded-md h-400 w-400object-fill">
          <Image alt="Gambar masukan" src={imageUrl} height={400} width={400}/>
        </div>
        <div className="flex flex-col justify-between md:px-4 md:mt-0 gap-y-12 md:gap-y-0">

          {/* INPUT IMAGE */}
          <div className="flex flex-col gap-y-2">
            <p className="font-semibold">Image Input</p>
            <Button 
              size='lg' 
              onClick={handleButtonClick} 
              className="border-2 border-white hover:bg-white hover:text-black hover:border-2 hover:border-black"
            >
              <p>Upload File</p>
            </Button>
            <div className="hidden">
              <Input 
                id='picture' 
                type='file' 
                className="border-2 border-black bg-white hover:bg-white hover:text-black hover:border-2 hover:border-black" onChange={inputImageHandler} 
                accept=".png, .jpg, .jpeg" 
                ref={fileInputRef}  
              />
            </div>
            
            <p>{imageName}</p>
          </div>

          <div className="flex flex-col gap-y-2">
            <div className="flex gap-x-2">
              <p>Color</p>
              <Switch onClick={switchHandler}/>
              <p>Texture</p>
            </div>
            <Button size='lg' className="border-2 border-white hover:bg-white hover:text-black hover:border-2 hover:border-black" onClick={searchHandler}>
              Search
            </Button>
          </div>
        </div>
      </div>

      <div className="w-[400px] md:w-[750px] mt-[75px] border-t border-1 border-black py-4">
        <div className="flex justify-between">
          <p>Result</p>
          <p>20 Result in 20 Seconds</p>
        </div>
        {/* PAGINATION */}
      </div>

      <div className="w-[400px] md:w-[750px] mt-[75px] border-t border-1 border-black py-4 flex flex-col items-center gap-y-4">
        <p className="font-semibold">Upload Dataset</p>
        <Input 
          type='file' 
          id='picture' 
          className="max-w-[300px] rounded-full border-2 border-black bg-white hover:bg-white hover:text-black hover:border-2 hover:border-black" 
          onChange={uploadDatasetHandler} />
      </div>
    </section>
  )
}

export default CBIR