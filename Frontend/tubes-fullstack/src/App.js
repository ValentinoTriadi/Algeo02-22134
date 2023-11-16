import logo from './logo.svg';
import './App.css';
import React, { useState } from "react";
import axios from "axios";



function App() {
  
  const [selectedFile, setSelectedFile] = useState(null);
  const [namaFile, setNamaFile] = useState(null);
  const [formData, setFormData] = useState(new FormData());
  const [responsess, setResponsess] = useState(null)
  
  const downloadPDF = () => {
    axios.get('http://127.0.0.1:8000/pdf-download', { responseType: 'blob' })
      .then((response) => {
        const link = document.createElement('a');
        const blob = new Blob([response.data], { type: 'application/pdf' });
        const url = window.URL.createObjectURL(blob);
        link.href = url;
        link.setAttribute('download', 'PDFImageSearch.pdf');
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        window.URL.revokeObjectURL(url);
      })
      .catch((error) => {
        console.error(error);
      });
  };
  
  

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
  
  const processUpload = () => {
    const requestOptions = {
      method: "GET",
      headers:{'Content-Type': 'application/json'}
    }

    fetch("http://127.0.0.1:8000/proses-warna/", requestOptions)
    .then(response => response.json())
    .then(function(response){
      console.log(response);
      setResponsess(response);
    });
  }

  const handleUpload = () => {
    axios
      .post('http://127.0.0.1:8000/uploadfiles', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      })

    console.log("STARTTTTTTT");
  };


  const filechangehandler = (e) => {
    setSelectedFile(e.target.files[0]);
    setNamaFile(e.target.files[0].name);
    console.log(e.target.files[0]);
  }
  
  const getSimiliarity = () => {
    const requestOptions = {
      method: "GET",
      headers:{'Content-Type': 'application/json'}
    }

    fetch("http://127.0.0.1:8000/hasil/", requestOptions)
    .then(response => response.json())
    .then(function(response){
      console.log(response);
      setResponsess(response);
    });
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
      // headers:{'Content-Type': 'application/json'}
    }

    fetch("http://127.0.0.1:8000/search-warna/", requestOptions)
    .then(response => response.json())
    .then(function(response){
      console.log(response);
    });
    
  }
  
  const processUpload1 = () => {
    const requestOptions = {
      method: "GET",
      headers:{'Content-Type': 'application/json'}
    }

    fetch("http://127.0.0.1:8000/proses-tekstur/", requestOptions)
    .then(response => response.json())
    .then(function(response){
      console.log(response);
      setResponsess(response);
    });
  }

  const handlesubmit1 = (e) => {
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
      // headers:{'Content-Type': 'application/json'}
    }

    fetch("http://127.0.0.1:8000/search-tekstur/", requestOptions)
    .then(response => response.json())
    .then(function(response){
      console.log(response);
    });
    
  }

  getSimiliarity()
  
  return (
    <div className="App">
      <form>
        <fieldset>
          <input onChange={fileschangehandler} multiple name="image" type="file" accept=".jpg, .jpeg"></input>
        </fieldset>
        <button onClick={handleUpload}>Upload</button>
        <button onClick={processUpload}>Process</button>
      </form>
      <form>
        <fieldset>
          <input onChange={filechangehandler}  name="image" type="file" accept=".jpg, .jpeg"></input>
        </fieldset>
        <button onClick={handlesubmit}>Upload</button>
      </form>
      <p>_________________{responsess}_________________</p>
      <form>
        <fieldset>
          <input onChange={fileschangehandler} multiple name="image" type="file" accept=".jpg, .jpeg"></input>
        </fieldset>
        <button onClick={handleUpload}>Upload</button>
        <button onClick={processUpload1}>Process</button>
      </form>
      <form>
        <fieldset>
          <input onChange={filechangehandler} name="image" type="file" accept=".jpg, .jpeg"></input>
        </fieldset>
        <button onClick={handlesubmit1}>Upload</button>
      </form>
      <p>_________________{responsess}_________________</p>
      <div>
        <button onClick={downloadPDF}>Export PDF</button>
      </div>
    </div>

  );
}

export default App;
