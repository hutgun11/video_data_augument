import cv2
import math
import numpy as np
import os
from PIL import Image 
from skimage.util import random_noise
from pathlib import Path
from read_video_in_folder import main
from read_augument import *
# path_video="WIN_20200618_14_03_31_Pro.mp4"


rootdir='video/'
img = Image.open("graylight.jpg")  
rootdata=r'data/'

li=[]
for subdir,dirs,files in os.walk(rootdir):
    for file in files:
        # print(file)
        li.append(os.path.join(subdir,file))

for path_video in li :
    # print(path_video)
    main(path_video)
main_data(rootdata)    