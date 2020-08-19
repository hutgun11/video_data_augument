import cv2
from PIL import Image 
import os
from skimage.util import random_noise
from skimage.io import imsave, imread
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image 
import sys
import shutil


img = Image.open("graylight.jpg")  
rootdir=r'data/'
# extensions=('.jpg','.png')
# dir_path=['data_top','data_gaussian','data_bright','data_blur']

def position_pic(path,path_top):

    img2 = Image.open(path)  
    img2.save(path) 
def adjust_gamma(image, gamma=1.0):
    # build a lookup table mapping the pixel values [0, 255] to
    # their adjusted gamma values
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
        for i in np.arange(0, 256)]).astype("uint8")
    # apply gamma correction using the lookup table
    return cv2.LUT(image, table)

def gaussian_blur(image_RGB,path_blur,path,v_blur=2.0):
    guassain_blur=cv2.GaussianBlur(image_RGB,(101,101),v_blur)
    imsave(path_blur.replace('.jpg','')+'_blur.jpg', guassain_blur)

    guassain_blur_img = Image.open(path_blur.replace('.jpg','')+'_blur.jpg')  
    guassain_blur_img.save(path.replace('.jpg','')+'_'+str(v_blur)+'_blur'+'.jpg') 

def brightness(image_RGB,path_bright,path,v_bright=2.0):
    adjusted = adjust_gamma(image_RGB, gamma=v_bright)
    imsave(path_bright.replace('.jpg','')+'_bright.jpg',adjusted)
    # global level_bright

    # if v_bright == 0.5 :
    #     level_bright='dark'
    # elif v_bright == 1 :
    #     level_bright ='normal'
    # elif v_bright == 2 : 
    #     level_bright = 'high'

    bright_img = Image.open(path_bright.replace('.jpg','')+'_bright.jpg')  
    bright_img.save(path.replace('.jpg','')+'_'+str(v_bright)+'_bright'+'.jpg') 

def gaussian_noise(image_RGB,path_gaussian,path):
    gauss_noise = random_noise(image_RGB, mode='gaussian', seed=None, clip=True)
    imsave(path_gaussian.replace('.jpg','')+'_gaussian.jpg', gauss_noise)

    gauss_img = Image.open(path_gaussian.replace('.jpg','')+'_gaussian.jpg')  
    gauss_img.save(path.replace('.jpg','')+'_gaussian.jpg') 

def rm_folder(dir_path):
    for folder in dir_path:
        try:
            shutil.rmtree(folder)
        except OSError as e:
            print ("Error: %s - %s." % (e.filename, e.strerror))
def main_data(rootdir):
    img = Image.open("graylight.jpg")  
    extensions=('.jpg','.png')
    dir_path=['data_top','data_gaussian','data_bright','data_blur']
    # v_blur=0.25
    # v_bright=0.5
    v_blur=1.0
    v_bright=2.0
    counter=1
    for subdir,dirs,files in os.walk(rootdir):
        for file in files:
            ext=os.path.splitext(file)[-1].lower()
            if ext in extensions:
                path = os.path.join(subdir,file)

                folder_path=os.path.dirname(path).replace('data','data_top')+'_top_floor'
                path_top=os.path.join(folder_path,file)

                folder_gaussian=os.path.dirname(path).replace('data','data_gaussian')+'_gaussian'
                path_gaussian=os.path.join(folder_gaussian,file)

                folder_blur=os.path.dirname(path).replace('data','data_blur')+'_blur'
                path_blur=os.path.join(folder_blur,file)

                folder_bright=os.path.dirname(path).replace('data','data_bright')+'_bright'
                path_bright=os.path.join(folder_bright,file)    
            
                try:
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)
                except OSError:
                    print('Error: Creating dir of data')

                try:
                    if not os.path.exists(folder_gaussian):
                        os.makedirs(folder_gaussian)
                except OSError:
                    print('Error: Creating dir of data') 

                try:
                    if not os.path.exists(folder_blur):
                        os.makedirs(folder_blur)
                except OSError:
                    print('Error: Creating dir of data') 
                try:    
                    if not os.path.exists(folder_bright):
                        os.makedirs(folder_bright)
                except OSError:
                    print('Error: Creating dir of data') 

                
                img_first=cv2.imread(path)    
                image_RGB=cv2.cvtColor(img_first,cv2.COLOR_BGR2RGB)   
                position_pic(path,path_top)
                # gaussian_noise(image_RGB,path_gaussian,path)
                gaussian_blur(image_RGB,path_blur,path,v_blur)#1.0
                brightness(image_RGB,path_bright,path,v_bright) #0.5
                v_bright =2
                brightness(image_RGB,path_bright,path,v_bright)#2
                v_bright=0.5 #0.5

                # if counter == 1:
                #     print('counter',counter,'path',path)
                #     # position_pic(path,path_top)
                #     counter +=1
                # elif counter==2:
                #     print('counter',counter,'path',path)
                #     gaussian_blur(image_RGB,path_blur,path,v_blur)#1.0
                #     v_blur *=float(2)
                #     gaussian_blur(image_RGB,path_blur,path,v_blur)#2.0
                #     v_blur = 1.0

                #     # if v_blur > 2:
                #     #     v_blur = 0.25
                #     os.remove(path)
                #     counter +=1
                # elif counter ==3:
                #     print('counter',counter,'path',path)
                #     gaussian_noise(image_RGB,path_gaussian,path)
                #     os.remove(path)
                #     counter +=1
                # elif counter ==4:
                #     print('counter',counter,'path',path)
                #     brightness(image_RGB,path_bright,path,v_bright) #0.5
                #     v_bright *=float(2)
                #     brightness(image_RGB,path_bright,path,v_bright)# 1 
                #     v_bright *=float(2)
                #     brightness(image_RGB,path_bright,path,v_bright)#2
                #     v_bright=0.5 #0.5

                #     os.remove(path)
                #     counter =1
            else:
                path = os.path.join(subdir,file)
                os.remove(path)
                print(path)
    rm_folder(dir_path)
