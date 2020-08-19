import xml.etree.ElementTree as ET
import os
import shutil
import json
import fnmatch

import cv2

name_product='AQUAFINA_BIO'
rootdir=r'data_'+name_product+'/'
rootdir2=r'data2_'+name_product+'/'
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

#cam2
for subdir,dirs,files in os.walk(rootdir2):
    for file in files:
        if fnmatch.fnmatch(file, '*.xml'):
            file_path=os.path.join(subdir,file)
            tree = ET.parse(file_path)
            root = tree.getroot()
            for elem in root:
                if elem.tag == 'filename':
                    elem.text = file.replace('.xml','')+'.jpg'
            tree.write(file_path, xml_declaration=True)
for subdir,dirs,files in os.walk(rootdir2):
    for file in files:
        if fnmatch.fnmatch(file, '*.jpg'):
            file_path_jpg=os.path.join(subdir,file)
            path_write=file_path_jpg.replace('.jpg','')+'.xml'
            print(path_write)
            tree.write(path_write, xml_declaration=True)
for subdir,dirs,files in os.walk(rootdir2):
    for file in files:
        if fnmatch.fnmatch(file, '*.xml'):
            file_path_xml=os.path.join(subdir,file)
            tree2 = ET.parse(file_path_xml)
            root2 = tree2.getroot()
            for elem2 in root2:
                if elem2.tag == 'filename':
                    elem2.text = file.replace('.xml','')+'.jpg'
            tree2.write(file_path_xml, xml_declaration=True)