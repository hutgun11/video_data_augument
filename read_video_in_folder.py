import cv2
import math
import numpy as np
import os
from PIL import Image 
from skimage.util import random_noise
from pathlib import Path
# path_video="WIN_20200618_14_03_31_Pro.mp4"
def main(path_video):
    #################### Setting up the file ################
    videoFile = path_video
    video_save_name=Path(path_video).stem
    name_product = video_save_name.replace('.mp4','')
    name_product = name_product.replace('.MOV','')
    name_product = name_product.replace('.avi','')
    # print(name_product)

    # # # defual
    # top=1#y1
    # left=640#x1
    # width=768#x2-x1 = 768
    # height=1080#y2-y1= 1024
    # # defual
    top=1#y1
    left=640#x1
    width=768#x2-x1 = 768
    height=1024#y2-y1= 1024



    try:
        if not os.path.exists('data/data_'+name_product):
            os.makedirs('data/data_'+name_product)
    except OSError:
        print('Error: Creating dir of data')

    try:
        if not os.path.exists('data_gaussian'):
            os.makedirs('data_gaussian')
    except OSError:
        print('Error: Creating dir of data')
    vidcap = cv2.VideoCapture(videoFile)
    success,image = vidcap.read()

    #################### Setting up parameters ################

    seconds = 0.2
    fps = vidcap.get(cv2.CAP_PROP_FPS) # Gets the frames per second
    # print
    multiplier = int(fps * seconds)
    # print(multiplier)

    #################### Initiate Process ################

    while success:
        frameId = int(round(vidcap.get(1))) #current frame number, rounded b/c sometimes you get frame intervals which aren't integers...this adds a little imprecision but is likely good enough
        success, image = vidcap.read()

        try:
            image = image[ top:top+height, left:left+width ]
            path= "data/data_"+name_product+"/frame"+str(frameId)+"_"+name_product+".jpg"
            # print(path)
            if frameId % multiplier == 0:
                cv2.imwrite(path, image)
                print(frameId,path) 
        except :
            pass


rootdir='video/'
# li=['WIN_20200618_14_06_07_Pro.mp4','WIN_20200618_14_03_31_Pro.mp4']
# print(type(li))
li=[]
for subdir,dirs,files in os.walk(rootdir):
    for file in files:
        # print(file)
        li.append(os.path.join(subdir,file))

for path_video in li :
    # print(path_video)
    main(path_video)    