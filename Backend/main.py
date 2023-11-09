from fastapi import FastAPI, HTTPException, status, File, Form, UploadFile
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import io
import os
import time
from Backend.CBIR import range_histogram, compare

app = FastAPI()

# origins = ["http://localhost:3000/"]    

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

dir_path = 'Backend\dataset'
namaFile = []



@app.get("/u/")
async def asdfsad():
    return "blabsss"
@app.get("/")
async def bro():
    return "hALO"

@app.post("/upload/")
async def receiveFile(file: bytes = File(...), namafile: str = Form(...)):
# async def receiveFile(file: bytes = File(...)):
    start = time.time()
    image = Image.open(io.BytesIO(file))
    image = image.save(f"Backend/{namafile}")

    if (not os.path.exists(dir_path)):
        return {"Status": "Fail"}
    result = compare(namafile)

    end = time.time()
    print("Execution Time:", end-start,'s')
    return result

@app.post("/uploadfiles/")
async def upload_files(files: List[UploadFile] = File(...)):
    print("Start")
    start = time.time()
    count = 0
    if (not os.path.exists(dir_path)):
        os.mkdir(dir_path)
    for file in files:
        count += 1
        # print(file.filename)
        contents = await file.read()
        img = Image.open(io.BytesIO(contents))
        # img.show()
        if (not os.path.exists(f"{dir_path}\{file.filename}")):
            img = img.save(f"{dir_path}\{file.filename}")
        range_histogram(file.filename, True)

    end = time.time()
    print("Uploaded", count, "Files in", end-start,'s')
    return {"uploadStatus": "Complete"}