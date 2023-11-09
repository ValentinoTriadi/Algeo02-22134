from fastapi import FastAPI, File, UploadFile

app = FastAPI()

class SimilarImage(BaseModel):
    filename: str
    similarity: float

# Fungsi untuk menghitung kemiripan gambar dengan parameter tekstur
def calculate_similarity(input_image):
    # Lakukan perhitungan CBIR dengan parameter tekstur di sini
    # Kembalikan daftar gambar yang mirip dan nilai persentase kemiripan
    
    similar_images = []  # Contoh daftar gambar yang mirip
    similar_images.append(SimilarImage(filename="image1.jpg", similarity=85.0))
    similar_images.append(SimilarImage(filename="image2.jpg", similarity=75.0))
    
    return similar_images

@app.post("/upload/")
async def upload_file(file: UploadFile):
  # Simpan file yang diunggah (file = gambar input)
  with open("input_image.jpg", "wb") as f:
      f.write(file.file.read())
  
  # Hitung kemiripan gambar dengan parameter tekstur
  similar_images = calculate_similarity("input_image.jpg")
  
  # Kembalikan hasil CBIR dalam bentuk metadata
  return similar_images
