import xml.etree.ElementTree as ET
import os
import shutil
import json
import fnmatch

import cv2
path =r'data/'
li=[]
for subdir,dirs,files in os.walk(path):        
        test=subdir.replace('data/data_','')
#         test=test.replace('data/data','')
#         test=subdir.replace('data/','')
        print(test)
        li.append(test)
del li[0]
for name in li :
    name_product=name
    print(name)
    rootdir=r'data/data_'+name_product+'/'
    for subdir,dirs,files in os.walk(rootdir):
        for file in files:
            if fnmatch.fnmatch(file, '*.xml'):
                file_path=os.path.join(subdir,file)
                tree = ET.parse(file_path)
                root = tree.getroot()
                for elem in root:
                    if elem.tag == 'filename':
                        elem.text = file.replace('.xml','')+'.jpg'
                tree.write(file_path, xml_declaration=True)
    for subdir,dirs,files in os.walk(rootdir):
        for file in files:
            if fnmatch.fnmatch(file, '*.jpg'):
                file_path_jpg=os.path.join(subdir,file)
                path_write=file_path_jpg.replace('.jpg','')+'.xml'
                print(path_write)
                tree.write(path_write, xml_declaration=True)
    for subdir,dirs,files in os.walk(rootdir):
        for file in files:
            if fnmatch.fnmatch(file, '*.xml'):
                file_path_xml=os.path.join(subdir,file)
                tree2 = ET.parse(file_path_xml)
                root2 = tree2.getroot()
                for elem2 in root2:
                    if elem2.tag == 'filename':
                        elem2.text = file.replace('.xml','')+'.jpg'
                tree2.write(file_path_xml, xml_declaration=True)

