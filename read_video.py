import cv2
import numpy as np
import os
import xml.etree.ElementTree as ET
import os
import shutil
import json
import fnmatch
from scipy import ndimage
from scipy.ndimage.interpolation import rotate

import cv2
frame_no= 0
# open cam 
cap = cv2.VideoCapture("pepsi_30.mp4")
cap.set(1,frame_no) # frame_no : frame you want persec

#cam 2 

# create folder
try:
    if not os.path.exists('test1'):
        os.makedirs('test1')
except OSError:
    print('Error: Creating dir of data')

currentFrame=0
li=[]
while (True):
    ret,frame =cap.read()
    frame=cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)

    # frame = cv2.flip(frame,2)
    # frame = rotate(frame, angle=45)
    # frame=cv2.resize(frame,(1080 , 1920)) 
    name='./test1/frame'+ str(currentFrame) +'.png'
    print('Creating'+name)
    cv2.imwrite(name,frame)
    currentFrame +=1



cap.release()
cv2.destroyAllWindows()
