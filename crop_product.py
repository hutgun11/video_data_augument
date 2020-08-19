import xml.etree.ElementTree as ET
import os
import shutil
import numpy as np
# import cv2
from cv2 import cv2
from pathlib import Path
import glob
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

dest_path = "SKU"
img_path = os.path.join(dest_path, "img")
if not os.path.exists(img_path):
    os.makedirs(img_path)
    
dataset_dir = "data/"
path = "SKU/img/"
root_lists = glob.glob(dataset_dir+'*/')
for root_path in root_lists:
    # print('root_path:', root_path) #date
#    root_folder = os.path.basename(root_path)
    #folder_lists = glob.glob(root_path+'*/')

    file_lists = glob.glob(os.path.join(root_path, '*.jpg'))
    for file_path in file_lists:
        # print(file_path)
        shutil.move(file_path, path)

list_sku = {}
object_list = {}
#count_items = 0
yolo_list = {}
filename_list = {}

list_sku_det = {}
GEN_YOLO = True
classes = []
boxes = []


sku = ["PEPSI CREAM-CAN","MILINDA MELON-PET"]


wrong_path = os.path.join(dest_path, "wrong_label")
if not os.path.exists(wrong_path):
    os.makedirs(wrong_path)
    
    
for products in sku:

    # Create directory if not exist
    product_path = os.path.join(dest_path, products)
    if not os.path.exists(product_path):
        os.makedirs(product_path)


try:
    file_classes_name = "new_dataset/objects_latest.names"
    with open(file_classes_name) as f:
        #data = f.readlines()
        classes = f.read().splitlines()
        # Do something with the file
        #print (classes)
except IOError:
    print("File not accessible")

dataset_dir = "data/"
#folder date 01022020
root_lists = glob.glob(dataset_dir+'*/')
for root_path in root_lists:
    file_date = root_path.split('/')[-1]
    if file_date not in filename_list:
        filename_list[file_date] = []
    
    # print('root_path:', root_path) #date
    file_lists = glob.glob(os.path.join(root_path, '*.xml'))
    for file_path in file_lists:
        # print(file_path)
        tree = ET.parse(file_path)
        root = tree.getroot()
        for elem in root:
            if elem.tag == 'filename':
                filename = elem.text
                # print(filename)
                img = cv2.imread("SKU/img/"+filename)
                img_name = filename[:41]
               
            for subelem in elem:
                #print (subelem)
                for box in subelem:
                    if box.tag == 'xmin':
                        x1 = int(box.text)
                    elif box.tag == 'ymin':
                        y1 = int(box.text)
                    elif box.tag == 'xmax':
                        x2 = int(box.text)
                    elif box.tag == 'ymax':
                        y2 = int(box.text)
                        
                if subelem.tag == 'name':
                    #count_items += 1
                    key_name_det = subelem.text
                    # print(subelem.text)
                    result = [x.strip() for x in subelem.text.split(':')]
                    # print(result)
                    # print(result[:4])
                    s = "-"
                    key_name = s.join(result[0:2])
#                    print(key_name)

                elif subelem.tag == 'bndbox':
                    right = int(x2)
                    #print(right )
                    bottom = int(y2)
                    #print(bottom)
                    left = int(x1)
                    #print(left)
                    top = int(y1)
                    #print(top )
                    width = int(x2) - int(x1)
                    #print(width)
                    height = int(y2) - int(y1)
                    #print(height)
                    # print(left,top,width,height)
                    for l in range(len(sku)) :
                        if key_name == sku[l]: 
                            try:
                                crop = img[ top:top+height, left:left+width ]
                                height,width,channels = crop.shape
                                y = int(crop.shape[0]/2)
                                # print(y)
                                cv2.putText(crop,str(left), (0,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0, 0, 255), 2)
                                s = left+top+width+height
                                cv2.imwrite(os.path.join(dest_path+"/"+sku[l]+"/", root_path[29:32]+"_"+img_name +"_"+sku[l]+"_"+str(s)+".jpg"), crop)
                                print(os.path.join(dest_path+"/"+sku[l]+"/", root_path[29:32]+"_"+img_name +"_"+sku[l]+"_"+str(s)+".jpg"))
                            # print(os.path.join(dest_path+"/"+sku[l]+"/", root_path[24:32]+"_"+img_name +"_"+sku[l]+"_"+str(s)+".jpg"))
                            # print(root_path[29:32])
                            # print(os.path.join(dest_path+"/"+sku[l]+"/", root_path[29:32]+"_"+img_name +"_"+sku[l]+"_"+str(s)+".jpg"))
                            # print(os.path.join(dest_path+"/"+sku[l]+"/", root_path[0:32]+"_"+img_name +"_"+sku[l]+"_"+str(s)+".jpg"))
                            except :
                                print(file_path)
                                try:
                                    os.remove(file_path)
                                except:
                                    pass
                                pass
