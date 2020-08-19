import cv2
import math
import numpy as np
import os
from PIL import Image 
from skimage.util import random_noise

#################### Setting up the file ################
videoFile = "WIN_20200618_12_04_30_Pro.mp4"
name_product = videoFile.replace('.mp4','')
name_product = name_product.replace('.MOV','')
name_product = name_product.replace('.avi','')

# print(name)
li=[]
#for cam 1
# top=374#y1
# left=374#x1
# width=1200
# height=1074

# # for cam 2
# top=52#y1
# left=150#x1
# width=700
# height=550

# # defual
# top=1#y1
# left=640#x1
# width=768#x2-x1 = 768
# height=1080#y2-y1= 1024


# # # for mix cam1 1 product
top=1#y1
left=306#x1
width=385
height=555

# # # for mix cam2 1 product
top=1#y1
left=144#x1
width=217
height=396
# # # for mix cam2 1 product
top=70#y1
left=313#x1
width=406
height=472

#for cam1 2-3 product


#cam1 1 product
# top=1#y1
# left=148#x1
# width=361
# height=378
# # cam2 1 product
# top=1#y1
# left=300#x1
# width=600
# height=594

# #cam1 mix  product
# top=1#y1
# left=100#x1
# width=600
# height=594
# #cam2 mix  product
# top=1#y1
# left=1#x1
# width=600
# height=594
#config
top=1#y1
left=130#x1
width=489
height=504


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
    # print(frameId)
    success, image = vidcap.read()
    scale_percent = 35 # percent of original size # for 1920*1280
    scale_percent = 70 # percent of original size # for 960*720


    width_bg = int(image.shape[1] * scale_percent / 100)
    height_bg = int(image.shape[0] * scale_percent / 100)
    dim = (width_bg, height_bg)
    # image = image[ top:top+height, left:left+width ]
    image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    # image = image[ top:top+height, left:left+width ]
    path= "data/data_"+name_product+"/frame"+str(frameId)+"_"+name_product+".jpg" 
    #gaussian pic
    # gauss = random_noise(image, mode='gaussian', seed=None, clip=True)
    # path_gaussian="data_gaussian/data_gaussian_"+name_product+"/frame"+str(frameId)+"_"+name_product+"_gaussian.jpg" 
    # print(path)
    if frameId % multiplier == 0:
        cv2.imwrite(path, image)
        print(frameId,path)


