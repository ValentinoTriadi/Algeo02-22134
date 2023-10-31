from fastapi import FastAPI, HTTPException, status, File, Form
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import io
import os

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
def countFile():
    count = 0
    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1
    return count

namaFile = []



@app.get("/u/")
async def asdfsad():
    return "blabsss"
@app.get("/")
async def bro():
    return "hALO"

@app.post("/upload/")
# async def receiveFile(file: bytes = File(...), namafile: str = Form(...)):
async def receiveFile(file: bytes = File(...)):

    # print(namafile)
    image = Image.open(io.BytesIO(file))
    if (os.path.exists("Backend\dataset")):
        print("TRUE")
    else:
        print("FALSE")
        os.mkdir("Backend\dataset")
    i = countFile()
    image = image.save(f"Backend\dataset\img{i}.jpg")

    return {"uploadStatus": "Complete"}