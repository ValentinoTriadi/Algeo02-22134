from fastapi import FastAPI, HTTPException, status, File, Form
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import io
import os
import Backend.CBIR

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
    print(namafile)
    namaFile.append(namafile)
    image = Image.open(io.BytesIO(file))
    if (not os.path.exists(dir_path)):
        os.mkdir(dir_path)
    if (not os.path.exists(f"{dir_path}\{namafile}")):
        image = image.save(f"{dir_path}\{namafile}")

    RGBtoHSV(namafile)

    return {"uploadStatus": "Complete"}