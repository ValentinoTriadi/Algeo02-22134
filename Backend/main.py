from fastapi import FastAPI, HTTPException, status, File, Form, UploadFile, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from typing import List
from PIL import Image
import io, os, shutil, time, json
from CBIRWarna import colorSimiliarity, compareWarna
from CBIRTekstur import pictureToTextureVector, compareTekstur
from IMGScraper import imageScraper

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

app.mount("/static/", StaticFiles(directory="static"), name="static")

@app.get("/hasil/")
async def asdfsad():
    if (os.path.exists("hasil.json")):
        f = open("hasil.json", 'r', encoding='utf-8')
        ret = f.read()
        f.close()
        return (ret)
    return json.dumps({})

@app.get("/")
async def bro():
    return "hALO"

@app.post("/uploadfiles/")
async def upload_files(files: List[UploadFile] = File(...)):
    if os.path.isfile("./hasil.json"):
        os.remove("./hasil.json")
    if os.path.isdir("./static/dataset"):
        shutil.rmtree("./static/dataset")
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

    end = time.time()
    print("Uploaded", count, "Files in", end-start,'s')
    return {"uploadStatus": "Complete"}

@app.get("/delete-dataset/")
async def deleteDataSet():
    if os.path.isfile("./hasil.json"):
        os.remove("./hasil.json")
    if os.path.isdir("static/dataset"):
        shutil.rmtree("static/dataset")
    if os.path.isfile("cache.txt"):
        os.remove("cache.txt")
    return {"deleteStatus":"Complete"}

@app.get("/proses-warna/")
async def prosesWarna():
    print("Start")
    if os.path.isfile("./hasil.json"):
        os.remove("./hasil.json")
    if os.path.isfile("./cache.txt"):
        os.remove("./cache.txt")
    start = time.time()
    count = 0
    if (not os.path.isdir(dir_path)):
        return {"proccessStatus":"Fail"}
    for filename in os.listdir(dir_path):
        count += 1
        if filename.endswith('.jpg') or filename.endswith('.jpeg'):
            img = Image.open(f"{dir_path}/{filename}")
            colorSimiliarity(img, True, filename)

    end = time.time()
    print("Process", count, "Files in", end-start,'s')
    return {"processStatus": "Complete"}

@app.post("/search-warna/")
async def searchWarna(file: bytes = File(...), namafile: str = Form(...)):
    if os.path.isfile("./hasil.json"):
        os.remove("./hasil.json")
    start = time.time()
    image = Image.open(io.BytesIO(file))
    image = image.save(f"static/{namafile}")

    if (not os.path.exists(dir_path)):
        return {"Status": "Fail"}
    result = compareWarna(namafile)
    os.remove(f"static/{namafile}")
    end = time.time()
    print("Execution Time:", end-start,'s')
    if os.path.isfile(f"static/{namafile}"):
        os.remove(f"static/{namafile}")
    return {"Status":"Success"}

@app.get("/proses-tekstur/")
async def prosesTekstur():
    if os.path.isfile("./hasil.json"):
        os.remove("./hasil.json")   
    print("Start")
    if os.path.isfile("./cache.txt"):
        os.remove("./cache.txt")
    start = time.time()
    count = 0
    if (not os.path.isdir(dir_path)):
        return {"proccessStatus":"Fail"}
    for filename in os.listdir(dir_path):
        count += 1
        if filename.endswith('.jpg') or filename.endswith('.jpeg'):
            img = Image.open(f"./static/dataset/{filename}")
            pictureToTextureVector(img, True, filename)

    end = time.time()
    print("Process", count, "Files in", end-start,'s')
    return {"processStatus": "Complete"}

@app.post("/search-tekstur/")
async def searchTekstur(file: bytes = File(...), namafile: str = Form(...)):
    if os.path.isfile("./hasil.json"):
        os.remove("./hasil.json")
    start = time.time()
    image = Image.open(io.BytesIO(file))
    image = image.save(f"./static/{namafile}")

    if (not os.path.exists(dir_path)):
        return {"Status": "Fail"}
    result = compareTekstur(namafile)
    os.remove(f"./static/{namafile}")
    end = time.time()
    print("Execution Time:", end-start,'s')
    return {"Status":"Success"}


@app.get("/image-scarpe/")
def imageScrape(url: str = Form(...)):
    deleteDataSet()
    count = imageScraper()
    if (count != 0):
        return {"scrapeStatus":"Complete"}
    return {"scrapeStatus":"Fail"}