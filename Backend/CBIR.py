from PIL import Image
import numpy as np
import time
import ast

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

    # rgb[cmax == cmin] = [0,0,cmax]
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
    return [h,s,v]


def RGBtoHSV(block):
    rgb = np.array(block)
    rgb = rgb.astype('float')
    hsv = np.zeros(rgb.shape, dtype='float') # Create array of zero

    Vmax = np.amax(rgb, axis=2) # Get Max value each pixel
    Vmin = np.amin(rgb, axis=2)
    Cmax = np.argmax(rgb, axis=2) # Get Index of max value (0 or 1 or 2)
    Cmin = np.argmin(rgb, axis=2)
    rgb[...,0] /= 255
    rgb[...,1] /= 255
    rgb[...,2] /= 255


    """Find H"""
    # Delta == 0
    hsv[Cmax == Cmin, 0] = np.zeros(hsv[Cmax == Cmin, 0].shape)
    # Cmax = R
    hsv[Cmax == 0, 0] = ((((rgb[..., 1] - rgb[..., 2]) / (Vmax - Vmin + np.spacing(1))) % 6) * 60)[Cmax == 0]
    # Cmax = G
    hsv[Cmax == 1, 0] = ((((rgb[..., 2] - rgb[..., 0]) / (Vmax - Vmin + np.spacing(1))) + 2) * 60)[Cmax == 1]
    # Cmax = B
    hsv[Cmax == 2, 0] = ((((rgb[..., 0] - rgb[..., 1]) / (Vmax - Vmin + np.spacing(1))) + 4) * 60)[Cmax == 2]

    """Find S"""
    # Vmax = 0
    hsv[Vmax == 0, 1] = np.zeros(hsv[Vmax == 0, 1].shape)
    # Vmax != 0
    hsv[Vmax != 0, 1] = ((Vmax - Vmin) / (Vmax + np.spacing(1)))[Vmax != 0]

    """Find V"""
    hsv[..., 2] = Vmax

    return(hsv)
    # print(rgb)
    # print(hsv)
    # print(hsv[0])
    # print(hsv[0][0])
    # print(hsv[0][0][0])
    # i = j = 0
    # r, g, b = rgb[i][j][0], rgb[i][j][1], rgb[i][j][2]
    # print(r,g,b)
    # hsv[i][j] = convertHSV(r,g,b)
    # print(hsv)


    
def decompose_block(img):
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
    return new2_array

def hsv_to_histogram(block):
    h, s, v = np.split(block, 3, axis=2)                     #Menyimpan masing masing H,S,V ke suatu array.
    #Mengubah masing masing array menjadi histogram.
    histH, binsH = np.histogram(h, bins = [0, 25, 40, 120, 190, 270, 295, 315, 360])
    histS, binsS = np.histogram(s, bins = [0, 0.2, 0.7, 1])
    histV, binsV = np.histogram(v, bins = [0, 0.2, 0.7, 1])

    # print(histH)
    # print(binsH)
    # print(histS)
    # print(binsS)
    # print(histV)
    # print(binsV)

    return [histH[7], histH[0], histH[1], histH[2], histH[3], histH[4], histH[5], histH[6], histS[0], histS[1], histS[2], histV[0], histV[1], histV[2]]

    # print(hist_array)
    #Mengembalikan hsv 3x3 dalam bentuk histogram
    # return hist

def range_histogram(filename, isUpload):
    img = Image.open(f"Backend/dataset/{filename}")
    block = decompose_block(img)
    hist = []
    for i in range(3):
        for j in range(3):
            block[i][j] = RGBtoHSV(block[i][j])
            hist.append(hsv_to_histogram(block[i][j]))
    if (isUpload):
        f = open('./Backend/cache.txt', 'a')
        f.writelines(f"{filename}|{hist}\n")
        f.close()
    else:
        return hist

def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)
    dot = np.dot(a, b)
    normA = np.linalg.norm(a)
    normB = np.linalg.norm(b)
    return dot / (normA * normB)

# def compare_blocks(h1, h2):
#     similarity = 0
#     for i in range(9):
#         for j in range(9):
#             similarity += cosine_similarity(h1[i], h2[j])

#     return 100 * similarity / (9 * 9)

def compare_blocks(h1, h2):
    sim = 0
    for i in range(9):
        similarity = []
        getfull = False
        for j in range(9):
            s = cosine_similarity(h1[i], h2[j])
            
            if (round(s*100000) == 100000):
                getfull = True
                break
            else:
                similarity.append(s)    
        if (getfull):
            sim += 1
        else:
            sim += np.mean(similarity)

    return (sim / 9)*100

def parseTXT(Line):
    r = Line.rstrip().split("|")
    r[1] = ast.literal_eval(r[1])

    return r

def compare(filename):
    img = Image.open(f"Backend/{filename}")
    img = range_histogram(img, False)
    ret = {}
    f = open('Backend/cache.txt', 'r')
    line = f.readlines()
    for i in range(len(line)):
        temp = parseTXT(line[i])
        sim = (compare_blocks(img, temp[1]))
        if (sim >= 60):
            print(i, sim)
            ret[f"{temp[0]}"] = sim

    return ret
