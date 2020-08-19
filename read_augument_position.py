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
extensions=('.jpg','.png')
dir_path=['data_top','data_gaussian','data_bright','data_blur']

def position_pic(path,path_top):
#     img = Image.open("graylight.jpg")  

#     img2 = Image.open(path)  
#     img.paste(img2, (80, 50)) 
#     img.save(path_top.replace('.jpg','')+'_top.jpg') 
# #         print(path_top.replace('.jpg','')+'_top.jpg')
#     img = Image.open("graylight.jpg") 

    img = Image.open("graylight.jpg") 
    img2 = Image.open(path)  
    img.paste(img2, (80, 400)) 
    img.save(path) 
    img = Image.open("graylight.jpg") 
def adjust_gamma(image, gamma=1.0):
    # build a lookup table mapping the pixel values [0, 255] to
    # their adjusted gamma values
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
        for i in np.arange(0, 256)]).astype("uint8")
    # apply gamma correction using the lookup table
    return cv2.LUT(image, table)

def gaussian_blur(image_RGB,path_blur,path):
    img = Image.open("graylight.jpg")
    guassain_blur=cv2.GaussianBlur(image_RGB,(101,101),2)
    imsave(path_blur.replace('.jpg','')+'_blur.jpg', guassain_blur)

    guassain_blur_img = Image.open(path_blur.replace('.jpg','')+'_blur.jpg')  
    img.paste(guassain_blur_img, (80, 400)) 
    img.save(path.replace('.jpg','')+'_blur_2_floor.jpg') 
    img = Image.open("graylight.jpg")

def brightness(image_RGB,path_bright,path):
    img = Image.open("graylight.jpg")
    adjusted = adjust_gamma(image_RGB, gamma=2)
    imsave(path_bright.replace('.jpg','')+'_bright.jpg',adjusted)

    bright_img = Image.open(path_bright.replace('.jpg','')+'_bright.jpg')  
    img.paste(bright_img, (80, 400)) 
    img.save(path.replace('.jpg','')+'_bright_2_floor.jpg') 
    img = Image.open("graylight.jpg")

def gaussian_noise(image_RGB,path_gaussian,path):
    img = Image.open("graylight.jpg")  
    gauss_noise = random_noise(image_RGB, mode='gaussian', seed=None, clip=True)
    imsave(path_gaussian.replace('.jpg','')+'_gaussian.jpg', gauss_noise)

    gauss_img = Image.open(path_gaussian.replace('.jpg','')+'_gaussian.jpg')  
    img.paste(gauss_img, (80, 400)) 
    img.save(path.replace('.jpg','')+'_gaussian_2_floor.jpg') 
    img = Image.open("graylight.jpg")  

def rm_folder(dir_path):
    for folder in dir_path:
        try:
            shutil.rmtree(folder)
        except OSError as e:
            print ("Error: %s - %s." % (e.filename, e.strerror))


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
            if counter == 1:
                print('counter',counter,'path',path)
                position_pic(path,path_top)
                counter +=1
            elif counter==2:
                print('counter',counter,'path',path)
                gaussian_blur(image_RGB,path_blur,path)
                os.remove(path)
                counter +=1
            elif counter ==3:
                print('counter',counter,'path',path)
                gaussian_noise(image_RGB,path_gaussian,path)
                os.remove(path)
                counter +=1
            elif counter ==4:
                print('counter',counter,'path',path)
                brightness(image_RGB,path_bright,path)
                os.remove(path)
                counter =1
            # print(path)



            # img_first=cv2.imread(path)    
            # image_RGB=cv2.cvtColor(img_first,cv2.COLOR_BGR2RGB)
            # brightness(image_RGB,path_bright,path)
            # gaussian_blur(image_RGB,path_blur,path)
            # gaussian_noise(image_RGB,path_gaussian,path)
            # position_pic(path,path_top)
            

            # #bright
            # adjusted = adjust_gamma(image_RGB, gamma=2)
            # imsave(path_bright.replace('.jpg','')+'_bright.jpg',adjusted)

            # bright_img = Image.open(path_bright.replace('.jpg','')+'_bright.jpg')  
            # img.paste(bright_img, (80, 400)) 
            # img.save(path.replace('.jpg','')+'_bright_2_floor.jpg') 
            # img = Image.open("graylight.jpg")
            # #guassain_blur
            # guassain_blur=cv2.GaussianBlur(image_RGB,(101,101),2)
            # # cv2.imwrite(path_blur.replace('.jpg','')+'_blur.jpg', cv2.cvtColor(guassain_blur,cv2.COLOR_RGB2BGR))
            # imsave(path_blur.replace('.jpg','')+'_blur.jpg', guassain_blur)

            # guassain_blur_img = Image.open(path_blur.replace('.jpg','')+'_blur.jpg')  
            # img.paste(guassain_blur_img, (80, 400)) 
            # img.save(path.replace('.jpg','')+'_blur_2_floor.jpg') 
            # img = Image.open("graylight.jpg")

            # #guassain_noise
            # # img_gaussian=cv2.imread(path)    
            # # image_RGB=cv2.cvtColor(img_gaussian,cv2.COLOR_BGR2RGB)
            # gauss_noise = random_noise(image_RGB, mode='gaussian', seed=None, clip=True)
            # imsave(path_gaussian.replace('.jpg','')+'_gaussian.jpg', gauss_noise)

            # gauss_img = Image.open(path_gaussian.replace('.jpg','')+'_gaussian.jpg')  
            # img.paste(gauss_img, (80, 400)) 
            # img.save(path.replace('.jpg','')+'_gaussian_2_floor.jpg') 
            # img = Image.open("graylight.jpg")  
            
            # gauss_img = Image.open(path_gaussian.replace('.jpg','')+'_gaussian.jpg')  
            # img.paste(gauss_img, (80, 50)) 
            # img.save(path_top.replace('.jpg','')+'_gaussian_top_floor.jpg') 
            # img = Image.open("graylight.jpg") 

    #         cv2.imwrite(path_gaussian.replace('.jpg','')+'_gaussian.jpg', gauss) 
            # position_pic(path,path_top)
            
            # print(path)
        else:
            path = os.path.join(subdir,file)
            os.remove(path)
            print(path)
rm_folder(dir_path)
