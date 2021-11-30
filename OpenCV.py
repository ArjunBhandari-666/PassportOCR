import cv2
import numpy as np
import pytesseract
from PIL import Image

#src_path ="D:/python'/practice"

def get_string(img_path):
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    cv2.imwrite("removed_noise.png", img)
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    cv2.imwrite("thres.png", img)
    result = pytesseract.image_to_string(Image.open("thres.png"))

    return result


print ('------------TEXT------------')

print (get_string("imag1.png"))