import logo from './logo.svg';
import './App.css';
import React, { useState } from "react";



function App() {
  
  const [selectedFile, setSelectedFile] = useState(null);

  const filechangehandler = (e) => {
    setSelectedFile(e.target.files[0]);
    console.log(e.target.files[0]);
  }

  const handlesubmit = (e) => {
    const formData = new FormData();
    formData.append(
      "file",
      selectedFile,
      selectedFile.name
    );
    // formData.append(
    //   "namafile",
    //   selectedFile.target.files[0].name,
    // )

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
          <input onChange={filechangehandler} name="image" type="file" accept=".jpg, .jpeg, .png"></input>
        </fieldset>
        <button onClick={handlesubmit}>Upload</button>
      </form>
    </div>
  );
}

export default App;
