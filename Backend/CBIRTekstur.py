from PIL import Image
import numpy as np
import ast
import json 

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

#def quantization(grayscale_matrix, num_levels=256):
    #quantization_range = np.linspace(0, 255, num_levels)
    #quantized_matrix = np.digitize(grayscale_matrix, quantization_range) - 1
    # metode bilinear interpolation supaya jadi 256x256
    # resized_matrix = np.array(Image.fromarray(quantized_matrix.astype('int')).resize((256, 256), Image.BILINEAR))
    # return resized_matrix
    #return quantized_matrix

# def create_co_occurrence_matrix(input_matrix, quantization_level):
    # Membuat framework matrix
    # framework_matrix = np.zeros((quantization_level, quantization_level), dtype=int)

    # # Mengambil pasangan pixel secara horizontal
    # x = input_matrix[:, :-1].flatten()
    # y = input_matrix[:, 1:].flatten()

    # # Increment element di framework_matrix[x][y]
    # np.add.at(framework_matrix, (x, y), 1)

    # # Membuat matriks simetris
    # return np.add(framework_matrix, np.transpose(framework_matrix))

def create_co_occurrence_matrix(input_matrix, quantization_level):
    framework_matrix = np.zeros((quantization_level, quantization_level), dtype=int)

    np.add.at(framework_matrix, (input_matrix[:, :-1], input_matrix[:, 1:]), 1)

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

# def calculate_contrast_from_glcm(glcm_matrix):
#     contrast = 0
#     row, col = glcm_matrix.shape
#     for i in range(row):
#         for j in range(col):
#             contrast += glcm_matrix[i, j] * (i - j)**2
#     return contrast

# def calculate_homogeneity_from_glcm(glcm_matrix):
#     homogeneity = 0
#     row, col = glcm_matrix.shape
#     for i in range(row):
#         for j in range(col):
#             homogeneity += glcm_matrix[i, j] / (1 + (i - j)**2)
#     return homogeneity

# def calculate_entropy_from_glcm(glcm_matrix):
#     entropy = 0
#     row, col = glcm_matrix.shape
#     for i in range(row):
#         for j in range(col):
#             entropy -= glcm_matrix[i, j] * np.log(glcm_matrix[i, j] + np.spacing(1))
#     return entropy

def create_texture_vector(glcm_matrix):
    contrast = calculate_contrast_from_glcm(glcm_matrix)
    homogeneity = calculate_homogeneity_from_glcm(glcm_matrix)
    entropy = calculate_entropy_from_glcm(glcm_matrix)
    texture_vector = np.array([contrast, homogeneity, entropy])
    return texture_vector

def pictureToTextureVector(img, isUpload, filename):
    rgb = np.array(img)
    # print("RGB",rgb)
    grayscale_matrix = convertToGrayscale(rgb)
    # print("G",grayscale_matrix)
    #quantized_matrix = quantization(grayscale_matrix)
    # print("q",quantized_matrix)
    #glcm_matrix = create_co_occurrence_matrix(quantized_matrix, 256)
    glcm_matrix = create_co_occurrence_matrix(grayscale_matrix, 256)
    print("GLCM",glcm_matrix)
    sum_glcm_matrix = np.sum(glcm_matrix)
    norm_glcm_matrix = glcm_matrix[...] / sum_glcm_matrix 
    # print("NORM",norm_glcm_matrix)
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
    f = open("hasil.json", 'w', encoding='utf-8')
    f.write(json.dumps(ret))
    f.close
    print(count)
    return ret
