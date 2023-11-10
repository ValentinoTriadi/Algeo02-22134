from PIL import Image
import numpy as np

def imageToArray(filename):
    img = Image.open(f"Backend/dataset/{filename}")
    array = np.array(img)
    print(array.shape[0])
    print(array.shape[1])
    return array

def convertHSV(r,g,b):
    r,g,b = r/255, g/255, b/255
    Cmax = max(r,g,b)
    Cmin = min(r,g,b)
    d = Cmax - Cmin

    # Find H
    if d == 0:
        h = 0
    elif Cmax == r:
        h = 60 * (((g-b)/d) % 6)
    elif Cmax == g:
        h = 60 * (((b-r)/d)+2)
    elif Cmax == b:
        h = 60 * (((r-g)/d)+4)

    # Find S
    if Cmax == 0:
        s = 0
    else:
        s = d/Cmax

    # Find V
    v = Cmax
    return (h,s,v)


def RGBtoHSV(filename):
    f1 = open("rgb.txt", "a")
    f2 = open("hsv.txt", "a")
    rgb = imageToArray(filename)
    hsv = []
    for i in range(rgb.shape[0]):
        for j in range(rgb.shape[1]):
            r, g, b = rgb[i][j][0], rgb[i][j][1], rgb[i][j][2]
            f1.write(f"{r, g, b} | ")
            hsv = convertHSV(r,g,b)
            f2.write(f"{hsv[0], hsv[1], hsv[2]} | ")
            # print(r,g,b)
        f1.write("\n")
        f2.write("\n")
    f1.close()
    f2.close()
    # i = j = 0
    # r, g, b = rgb[i][j][0], rgb[i][j][1], rgb[i][j][2]
    # print(r,g,b)
    # print(rgb)
    # hsv = convertHSV(r,g,b)


    
def decompose_block(filename):
    img = Image.open(f"Backend/dataset/{filename}")
    array = np.array(img)
    new_array = np.array_split(array,3)
    
    # Menampilkan setiap blok secara terpisah
    #for i, block in enumerate(new_array):
        #image = Image.fromarray(block.astype('uint8'))
        #image.show()

    
    new2_array = [np.array_split(part, 3, axis=1) for part in new_array]

    # Menampilkan setiap blok secara terpisah
    #for i, part in enumerate(new2_array):
        #for j, block in enumerate(part):
            #image = Image.fromarray(block.astype('uint8'))
            #image.show()

def hsv_to_histogram(block):
    h, s, v = np.split(block, 3, axis=2)                     #Menyimpan masing masing H,S,V ke suatu array.
    #Mengubah masing masing array menjadi histogram.
    hist = np.histogram(h, bins=256, range=(0, 255))[0]
    hist += np.histogram(s, bins=256, range=(0, 255))[0]
    hist += np.histogram(v, bins=256, range=(0, 255))[0]

    #Mengembalikan hsv 3x3 dalam bentuk histogram
    return hist

def histogram_block(filename):
    block = decompose_block(filename)
    return hsv_to_histogram(block)

def range_histogram(filename):
    block = decompose_block(filename)
    histogram = hsv_to_histogram(block)

    h_min = np.min(hist[:, 0])
    h_max = np.max(hist[:, 0])
    s_min = np.min(hist[:, 1])
    s_max = np.max(hist[:, 1])
    v_min = np.min(hist[:, 2])
    v_max = np.max(hist[:, 2])

    h_range = h_max - h_min
    s_range = s_max - s_min
    v_range = v_max - v_min

    return h_range, s_range, v_range

def cosine_similarity(a, b):
    return np.dot(a, b) / np.linalg.norm(a) * np.linalg.norm(b)

def compare_blocks(filename_a, filename_b):
    ranges_a = []
    ranges_b = []
    for i in range(9):
        ranges_a.append(range_histogram(filename_a))
        ranges_b.append(range_histogram(filename_b))

    similarity = 0
    for i in range(9):
        for j in range(9):
            similarity += cosine_similarity(ranges_a[i], ranges_b[j])

    return similarity / (9 * 9)


#Konsep CBIR dengan parameter tekstur
#1. ubah jadi greyscale pakai rumus Y
#2. diquantifikasi dengan quantisasi level 256
#3. dibuat jadi GCLM/co-occurance(ada referensinya dalam bentuk medium)
    -step 1 buat framework matrix
    -step 2 symmetic matrix
    -dinormalisasi
    -jadi glcm_matrix
#4. cari nilai contrast, entropy dan homogeneity dibuat jadi vektor
#5. bandingin
#6. pictureToTextureVector ada fungsi ini buat kalo baca langsung dapet vektor tekstur

def convertToGrayscale(imageArray):
    rgb = np.array(imageArray);
    newShape = (rgb.shape[0],rgb.shape[1])
    new = np.zeros(newShape,dtype='float')
    new[...]=rgb[...0]+rgb[...1]+rgb[..2]
    return new


def normalize_brightness(grayscale_matrix):
    min_val = np.min(grayscale_matrix)
    max_val = np.max(grayscale_matrix)
    
    # Normalisasi kecerahan ke rentang 0-255
    normalized_matrix = 255 * (grayscale_matrix - min_val) / (max_val - min_val)
    
    return normalized_matrix

def quantization(grayscale_matrix):
    num_levels= 256
    # Menentukan rentang tingkat keabuan
    quantization_range = np.linspace(0, 255, num_levels)
    
    # Menetapkan nilai tengah rentang tingkat keabuan yang sesuai
    quantized_matrix = np.digitize(grayscale_matrix, quantization_range) - 1
    
    return quantized_matrix

def create_framework_matrix(quantization_level):
    # Menentukan dimensi matriks
    dimensions = (quantization_level, quantization_level)

    # Menentukan tingkat keabuan untuk setiap elemen matriks
    quantization_step = quantization_level // np.prod(dimensions)

    # Membuat framework matrix menggunakan broadcasting NumPy
    row_indices, col_indices = np.indices(dimensions)
    framework_matrix = row_indices * dimensions[1] * quantization_step + col_indices * quantization_step

    return framework_matrix

def create_co_occurrence_matrix(input_matrix, quantization_level):
    # Membuat framework matrix
    framework_matrix = np.arange(quantization_level * quantization_level).reshape((quantization_level, quantization_level))

    # Mengambil pasangan pixel secara horizontal
    horizontal_pairs = input_matrix[:, :-1] * quantization_level + input_matrix[:, 1:]

    # Membagi matriks horizontal_pairs menjadi 256 matriks berukuran 1x2
    horizontal_pairs_split = np.array_split(horizontal_pairs, quantization_level)

    # Menghitung frekuensi kemunculan pasangan pixel
    unique_pairs, counts = np.unique(horizontal_pairs_split, axis=1, return_counts=True)

    # Mencari koordinat pasangan pixel pada framework matrix
    row_indices = unique_pairs // quantization_level
    col_indices = unique_pairs % quantization_level

    # Inisialisasi GLCM matrix dengan zeros
    glcm_matrix = np.zeros((quantization_level, quantization_level))

    # Menambahkan frekuensi ke GLCM matrix
    glcm_matrix[row_indices, col_indices] = counts

    # Membuat matriks simetris
    glcm_matrix = glcm_matrix + glcm_matrix.T

    return glcm_matrix



def calculate_contrast_from_glcm(glcm_matrix):
    return np.sum(glcm_matrix * (glcm_matrix - np.mean(glcm_matrix))**2)

def calculate_homogeneity_from_glcm(glcm_matrix):
    return np.sum(glcm_matrix / (1 + (glcm_matrix - np.mean(glcm_matrix))**2))

def calculate_entropy_from_glcm(glcm_matrix):
    epsilon = 1e-15  # untuk menghindari log(0)
    return -np.sum(glcm_matrix * np.log(glcm_matrix + epsilon))


def create_texture_vector(glcm_matrix):
    contrast = calculate_contrast(glcm_matrix)
    homogeneity = calculate_homogeneity(glcm_matrix)
    entropy = calculate_entropy(glcm_matrix)
    texture_vector = np.array([contrast, homogeneity, entropy])
    return texture_vector

def pictureToTextureVector(filename):
    rgb = imageToArray(filename)
    grayscale_matrix = convertToGrayscale(rgb)
    quantized_matrix = quantization(grayscale_matrix)
    glcm_matrix = create_co_occurrence_matrix(quantized_matrix, 256)
    texture_vector = create_texture_vector(glcm_matrix)


    with open("vector.txt", "a") as f:
        f.write(str(texture_vector) + "\n")

    return texture_vector

def cosine_similarity(vector_a, vector_b):
    dot_product = np.dot(vector_a, vector_b)
    magnitude_a = np.linalg.norm(vector_a)
    magnitude_b = np.linalg.norm(vector_b)
    similarity = dot_product / (magnitude_a * magnitude_b)
    return similarity



