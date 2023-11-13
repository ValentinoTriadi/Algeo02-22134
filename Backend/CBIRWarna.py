from PIL import Image
import numpy as np
import time
import ast
import json 

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

    
def decompose_block(img):
    array = np.array(img)
    new_array = np.array_split(array,3)
    new2_array = [np.array_split(part, 3, axis=1) for part in new_array]
    return new2_array

def hsv_to_histogram(block):
    h, s, v = np.split(block, 3, axis=2) # Menyimpan masing masing H,S,V ke suatu array.
    # Mengubah masing masing array menjadi histogram.
    histH, binsH = np.histogram(h, bins = [0, 25, 40, 120, 190, 270, 295, 315, 360])
    histS, binsS = np.histogram(s, bins = [0, 0.2, 0.7, 1])
    histV, binsV = np.histogram(v, bins = [0, 0.2, 0.7, 1])
    return [histH[7], histH[0], histH[1], histH[2], histH[3], histH[4], histH[5], histH[6], histS[0], histS[1], histS[2], histV[0], histV[1], histV[2]]


def colorSimiliarity(img, isUpload, filename):
    block = decompose_block(img)
    hist = []
    for i in range(3):
        for j in range(3):
            block[i][j] = RGBtoHSV(block[i][j])
            hist.append(hsv_to_histogram(block[i][j]))
    if (isUpload):
        f = open('./cache.txt', 'a')
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

def compare_blocks(h1, h2):
    sim = 0
    for i in range(9):
        sim += cosine_similarity(h1[i], h2[i])

    return (sim / 9)*100

def parseTXT(Line):
    r = Line.rstrip().split("|")
    r[1] = ast.literal_eval(r[1])

    return r

def compareWarna(filename):
    start = time.time()
    img = Image.open(f"static/{filename}")
    img = colorSimiliarity(img, False, filename)
    ret = {}
    f = open('./cache.txt', 'r')
    line = f.readlines()
    for i in range(len(line)):
        temp = parseTXT(line[i])
        sim = (compare_blocks(img, temp[1]))
        if (sim >= 60):
            ret[f"{temp[0]}"] = round(sim, 2)

    end = time.time()
    ret = {key: val for key, val in sorted(ret.items(), key = lambda ele: ele[1], reverse = True)}
    ret["Time"] = round(end-start,2)
    f = open("hasil.json", 'w', encoding='utf-8')
    f.write(json.dumps(ret))
    f.close
    return ret


