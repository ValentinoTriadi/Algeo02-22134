from PIL import Image
import numpy as np

def imageToArray(filename):
    img = Image.open(f"Backend/dataset/{filename}")
    array = np.array(img)
    # print(array.shape[0])
    # print(array.shape[1])
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


# First Call Function
def RGBtoHSV(filename):
    # f1 = open("rgb.txt", "a")
    # f2 = open("hsv.txt", "a")
    rgb = imageToArray(filename)
    hsv = []
    # for i in range(rgb.shape[0]):
    #     for j in range(rgb.shape[1]):
    #         r, g, b = rgb[i][j][0], rgb[i][j][1], rgb[i][j][2]
    #         print(convertHSV(r,g,b))
    #         # hsv.apppend(convertHSV(r,g,b))
    i = j = 0
    r, g, b = rgb[i][j][0], rgb[i][j][1], rgb[i][j][2]
    print(r,g,b)
    print(rgb)
    print(convertHSV(r,g,b))
    hsv = convertHSV(r,g,b)
    print(hsv)


    
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





