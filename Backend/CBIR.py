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
    


