import logo from './logo.svg';
import './App.css';
import React, { useState } from "react";
import axios from "axios";



function App() {
  
  const [selectedFile, setSelectedFile] = useState(null);
  const [namaFile, setNamaFile] = useState(null);
  const [formData, setFormData] = useState(new FormData());
  

  const fileschangehandler = (e) => {
    const newformData = new FormData();
    const files = e.target.files;

    for (let i = 0; i < files.length; i++) {
      newformData.append('files', files[i]);
      // setSelectedFile(files[i]);
      // setNamaFile(files[i].name);
      // console.log(files[i]);
    }
    setFormData(newformData);
    // formData.forEach((e)=>{
    //   console.log(e);
    // });
  }
  
  const handleUpload = () => {
    axios.post('http://127.0.0.1:8000/uploadfiles', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    console.log("STARTTTTTTT");
  };


  const filechangehandler = (e) => {
    setSelectedFile(e.target.files[0]);
    setNamaFile(e.target.files[0].name);
    console.log(e.target.files[0]);
  }
  
  const handlesubmit = (e) => {
    console.log(namaFile);
    const formData = new FormData();
    formData.append(
      "file",
      selectedFile,
      selectedFile.name
    );
    formData.append(
      "namafile",
      namaFile,
    )

    const requestOptions = {
      method: "POST",
      body: formData,
    }

    fetch("http://127.0.0.1:8000/upload/", requestOptions)
    .then(response => response.json())
    .then(function(response){
      console.log(response);
    })
  }

  return (
    <div className="App">
      <form>
        <fieldset>
          <input onChange={fileschangehandler} multiple name="image" type="file" accept=".jpg, .jpeg"></input>
        </fieldset>
        <button onClick={handleUpload}>Upload</button>
      </form>
      <form>
        <fieldset>
          <input onChange={filechangehandler} multiple name="image" type="file" accept=".jpg, .jpeg"></input>
        </fieldset>
        <button onClick={handlesubmit}>Upload</button>
      </form>
    </div>
  );
}

export default App;
