from PIL import Image
import numpy as np
import ast, json, time

#Konsep CBIR dengan parameter tekstur
#1. ubah jadi greyscale pakai rumus Y
#2. diquantifikasi dengan quantisasi level 256
#3. dibuat jadi GCLM/co-occurance(ada referensinya dalam bentuk medium)
    # -step 1 buat framework matrix
    # -step 2 symmetic matrix
    # -dinormalisasi
    # -jadi glcm_matrix
#4. cari nilai contrast, entropy dan homogeneity dibuat jadi vektor
#5. bandingin
#6. pictureToTextureVector ada fungsi ini buat kalo baca langsung dapet vektor tekstur

def convertToGrayscale(imageArray):
    rgb = np.array(imageArray)
    newShape = (rgb.shape[0],rgb.shape[1])
    new = np.zeros(newShape,dtype='float')
    new[...] = (rgb[...,0] * 0.29) + (rgb[...,1] * 0.587) + (rgb[...,2] * 0.114)
    return new

def create_co_occurrence_matrix(input_matrix, quantization_level):
    framework_matrix = np.zeros((quantization_level, quantization_level), dtype=int)
    input = input_matrix.astype("int")
    np.add.at(framework_matrix, (input[:, :-1], input[:, 1:]), 1)
    glcm_matrix = np.add(framework_matrix, np.transpose(framework_matrix))
    return glcm_matrix

def calculate_contrast_from_glcm(glcm_matrix):
    i, j = np.indices(glcm_matrix.shape)
    return np.sum(glcm_matrix * (i - j)**2)

def calculate_homogeneity_from_glcm(glcm_matrix):
    i, j = np.indices(glcm_matrix.shape)
    return np.sum(glcm_matrix / (1 + (i - j)**2))

def calculate_entropy_from_glcm(glcm_matrix):
    return -np.sum(glcm_matrix * np.log(glcm_matrix + np.spacing(1)))

def create_texture_vector(glcm_matrix):
    contrast = calculate_contrast_from_glcm(glcm_matrix)
    homogeneity = calculate_homogeneity_from_glcm(glcm_matrix)
    entropy = calculate_entropy_from_glcm(glcm_matrix)
    texture_vector = np.array([contrast, homogeneity, entropy])
    return texture_vector

def pictureToTextureVector(img, isUpload, filename):
    rgb = np.array(img)
    grayscale_matrix = convertToGrayscale(rgb)
    glcm_matrix = create_co_occurrence_matrix(grayscale_matrix, 256)
    norm_glcm_matrix = glcm_matrix / np.sum(glcm_matrix)
    texture_vector = create_texture_vector(norm_glcm_matrix)
    if (isUpload):
        with open("./cache.txt", "a") as f:
            f.write(filename + "|[" + str(texture_vector[0]) + "," + str(texture_vector[1]) + "," +str(texture_vector[2]) + "]\n")
    return texture_vector

def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)
    dot = np.dot(a, b)
    normA = np.linalg.norm(a)
    normB = np.linalg.norm(b)
    return dot / (normA * normB) * 100

def parseTXT(Line):
    r = Line.rstrip().split("|")
    r[1] = ast.literal_eval(r[1])
    return r

def compareTekstur(filename):
    start = time.time()
    img = Image.open(f"static/{filename}")
    img = pictureToTextureVector(img, False, filename)
    ret = {}
    f = open('./cache.txt', 'r')
    line = f.readlines()
    count = 0
    for i in range(len(line)):
        temp = parseTXT(line[i])
        sim = (cosine_similarity(img, temp[1]))
        print(sim, temp[0])
        if (sim >= 60):
            count += 1
            ret[f"{temp[0]}"] = round(sim, 2)

    ret = {key: val for key, val in sorted(ret.items(), key = lambda ele: ele[1], reverse = True)}
    end = time.time()
    ret["Time"] = round(end-start,2)
    f = open("hasil.json", 'w', encoding='utf-8')
    f.write(json.dumps(ret))
    f.close
    print(count)
    return ret
