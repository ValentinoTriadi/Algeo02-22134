from fastapi import FastAPI, HTTPException, status, File, Form, UploadFile
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from typing import List
from PIL import Image
import io, os, shutil, time, json, requests
from CBIRWarna import colorSimiliarity, compareWarna
from CBIRTekstur import pictureToTextureVector, compareTekstur
from Bonus import imageScraper, exportPDF

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
        if (not os.path.exists(f"{dir_path}\{file.filename.split('/')[-1]}")):
            img.save(f"{dir_path}\{file.filename.split('/')[-1]}")

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
    return {"processStatus": "Complete", "TimeProcess": round(end-start, 2)}

@app.post("/search-warna/")
async def searchWarna(file: bytes = File(...), namafile: str = Form(...)):
    if os.path.isfile("./hasil.json"):
        os.remove("./hasil.json")
    if os.path.isfile(f"static/search.jpg"):
        os.remove(f"static/search.jpg")
    start = time.time()
    image = Image.open(io.BytesIO(file))
    image = image.save(f"static/search.jpg")

    if (not os.path.exists(dir_path)):
        return {"Status": "Fail"}
    result = compareWarna(namafile)
    end = time.time()
    print("Execution Time:", end-start,'s')
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
    return {"processStatus": "Complete", "TimeProcess": round(end-start,2)}

@app.post("/search-tekstur/")
async def searchTekstur(file: bytes = File(...), namafile: str = Form(...)):
    if os.path.isfile("./hasil.json"):
        os.remove("./hasil.json")
    if os.path.isfile("static/search.jpg"):
        os.remove("static/search.jpg")
    start = time.time()
    image = Image.open(io.BytesIO(file))
    image = image.save(f"static/search.jpg")

    if (not os.path.exists(dir_path)):
        return {"Status": "Fail"}
    result = compareTekstur(namafile)
    end = time.time()
    print("Execution Time:", end-start,'s')
    return {"Status":"Success"}


@app.post("/image-scrape/")
async def imageScrape(url: str = Form(...)):
    print(url)
    await deleteDataSet()
    if (not os.path.exists(dir_path)):
        os.mkdir(dir_path)
    count = imageScraper(url)
    if (count != 0):
        return {"scrapeStatus":"Complete"}
    return {"scrapeStatus":"Fail"}

@app.get("/pdf-download/")
async def downloadPDF():
    file_path = "./static/PDFResult.pdf"
    return FileResponse(file_path, content_disposition_type="attachment", filename="PDFImageSearch.pdf")

@app.get("/create-pdf/")
async def createPDF():
    start = time.time()
    exportPDF()
    end = time.time()
    print("Created PDF File in", end - start, "s")