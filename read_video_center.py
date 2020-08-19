import cv2
import math
import numpy as np
import os
import xml.etree.ElementTree as ET

#################### Setting up the file ################
videoFile = "veda_4.mp4"
file_path = r'data_veda_4/frame102_veda_4.xml'

name_product = videoFile.replace('.mp4','')
name_product = name_product.replace('.MOV','')
name_product = name_product.replace('.avi','')

# print(name)
top=1#y1
left=640#x1
width=768#x2-x1 = 768
height=1024#y2-y1= 1024
#size height=1080
# top=0
# height=1080
try:
    if not os.path.exists('data_'+name_product):
        os.makedirs('data_'+name_product)
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
tree = ET.parse(file_path)
root = tree.getroot()
for elem in root:
    for subelem in elem:
        for box in subelem:
            if box.tag == 'xmin':
                x1 = int(box.text)
            elif box.tag == 'xmax':
                x2 = int(box.text)
                center_x = (x2+x1)/2
                left = int(center_x-392)
                width = int(left+392)
                print(left,width,center_x)
                top=1
                height=1024
                seconds = 0.2
                vidcap = cv2.VideoCapture(videoFile)
                success,image = vidcap.read()
                fps = vidcap.get(cv2.CAP_PROP_FPS) # Gets the frames per second
                # print
                multiplier = int(fps * seconds)
                while success:
                    frameId = int(round(vidcap.get(1))) #current frame number, rounded b/c sometimes you get frame intervals which aren't integers...this adds a little imprecision but is likely good enough
                    # print(frameId)
                    success, image = vidcap.read()
                    image = image[ top:top+height, left:left+width ]

                    # print(success)
                    # image=cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
                    path= "data_"+name_product+"/frame"+str(frameId)+"_"+name_product+"5.jpg" 
                    # print(path)
                    if frameId % multiplier == 0:
                        # print('cola',frameId)
                        cv2.imwrite(path, image)
                        print(frameId)

                vidcap.release()