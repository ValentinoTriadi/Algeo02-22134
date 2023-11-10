from fastapi import FastAPI, HTTPException, status, File, Form, UploadFile, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from typing import List
from PIL import Image
import json
import io
import os, shutil
import time
from CBIR import colorSimiliarity, compare

app = FastAPI()

# origins = ["http://localhost:3000/"]    

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

dir_path = 'static/dataset'
namaFile = []

app.mount("/static/", StaticFiles(directory="static"), name="static")

@app.get("/hasil/")
async def asdfsad():
    f = open("hasil.json", 'r', encoding='utf-8')
    ret = f.read()
    f.close()
    print(ret)
    return (ret)
@app.get("/")
async def bro():
    return "hALO"

@app.post("/upload/")
async def receiveFile(file: bytes = File(...), namafile: str = Form(...)):
# async def receiveFile(file: bytes = File(...)):
    start = time.time()
    image = Image.open(io.BytesIO(file))
    image = image.save(f"static/{namafile}")

    if (not os.path.exists(dir_path)):
        return {"Status": "Fail"}
    result = compare(namafile)
    os.remove(f"static/{namafile}")
    end = time.time()
    print("Execution Time:", end-start,'s')
    # result = json.dumps(result)
    # print((result))
    return result

@app.post("/uploadfiles/")
async def upload_files(files: List[UploadFile] = File(...)):
    print("Start")
    if os.path.isdir("static/dataset"):
        shutil.rmtree("static/dataset")
    if os.path.isfile("cache.txt"):
        os.remove("cache.txt")
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
            img.save(f"{dir_path}\{file.filename}")
        colorSimiliarity(img, True, file.filename)

    end = time.time()
    print("Uploaded", count, "Files in", end-start,'s')
    return {"uploadStatus": "Complete"}