import cv2
import math
import numpy as np
import os
from PIL import Image 
img = Image.open("graylight.jpg")  
rootdir=r'data/'
extensions=('.jpg','.png')
for subdir,dirs,files in os.walk(rootdir):
    for file in files:
        ext =os.path.splitext(file)[-1].lower()
        if ext in extensions:
            path = os.path.join(subdir,file)
            img2 = cv2.imread(path, cv2.IMREAD_UNCHANGED)
            scale_percent = 70 # percent of original size
            width_bg = int(img2.shape[1] * scale_percent / 100)
            height_bg = int(img2.shape[0] * scale_percent / 100)
            dim = (width_bg, height_bg)
            img2 = cv2.resize(img2, dim, interpolation = cv2.INTER_AREA)
            # img.paste(img2, (80, 500)) 
            cv2.imwrite(path, img2)
            print(path)

