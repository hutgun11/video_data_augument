import cv2
import numpy as np
import os
import xml.etree.ElementTree as ET
import os
import shutil
import json
import fnmatch

import cv2



name_product='AQUAFINA_BIO'
# open cam 
cap = cv2.VideoCapture("cam1_"+name_product+".mp4")

#cam 2 
cap2 = cv2.VideoCapture("cam2_"+name_product+".mp4")

# create folder
try:
    if not os.path.exists('data'+'_'+name_product):
        os.makedirs('data'+'_'+name_product)
except OSError:
    print('Error: Creating dir of data')

try:
    if not os.path.exists('data2'+'_'+name_product):
        os.makedirs('data2'+'_'+name_product)
except OSError:
    print('Error: Creating dir of data')

currentFrame=0

while (True):
    ret,frame =cap.read()
    # print(frame)
    #cam2
    ret2,frame2 =cap2.read()

    #data_AQUAFINA_BIO
    name='./data_'+name_product+'/'+name_product+ str(currentFrame) +'_cam1'+'.jpg'

    #cam2
    name2='./data2_'+name_product+'/'+name_product+ str(currentFrame) +'_cam2'+'.jpg'


    print('Creating'+name)
    cv2.imwrite(name,frame)

    #cam2
    cv2.imwrite(name2,frame2)
    # #test delay
    # cv2.waitKey(3000)



    currentFrame +=1







cap.release()
cap2.release()
cv2.destroyAllWindows()
