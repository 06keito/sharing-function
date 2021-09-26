#!/usr/bin/env python
# -*- coding: utf-8 -*-

# run command
# -> pip install natsort opencv-python
# -> python create_page.py [-d pic]

import os,glob
import argparse
from natsort import natsorted
import cv2

CONSOLE_ARGUMENTS = None

class FormatText:
    def __init__(self):
        self.html_text_header =(
            '''<!DOCTYPE html>\n'''
            '''<header>\n'''
            '''\t<link rel="stylesheet" href="style.css">\n'''
            '''</header>\n''')
        
        self.html_text_heading = (
            '''<h1 class="heading"> {category} {img_count}imgs</h1>\n"'''
        )

        self.html_text_div = (
            '''<div class="img">\n'''
            '''\t<img src="{img_path}" height="{height}" width="{width}">\n'''
            '''\t<div class="over_number">Pic{iteration}</div>\n'''
            '''</div>\n''')

        self.css_text = (
            '''.heading{\n'''
            '''\tclear :both;\n'''
            '''}\n'''
            '''.img{\n'''
            '''\tfloat : left;\n'''
            '''\tposition: relative;\n'''
            '''}\n'''
            '''.over_number{\n'''
            '''\tposition: absolute;\n'''
            '''\tcolor: rgb(255, 255, 255);\n'''
            '''\ttext-align : center;\n'''
            '''\ttop: 0%;\n'''
            '''\tfont-size: 10px;\n'''
            '''}''')

def Get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dir', help='saving picture directory')
    args = parser.parse_args()
    return args

def Input_img_data():
    data = []
    for i in natsorted(glob.glob(os.path.join\
        (CONSOLE_ARGUMENTS.dir,'*'),recursive=True)):
        base = os.path.basename(i)
        for path in natsorted(glob.glob(os.path.join\
            (CONSOLE_ARGUMENTS.dir,base,'*.jpg'),recursive=True)):
            data.append([path,base])
    return data

def Generate_css_stylesheet():
    code = FormatText().css_text
    with open('style.css',mode='w',encoding='utf_8') as f:
        f.write(code)

def Writing_heading_and_img_div(file,datas,ctgr):
    file.write(FormatText().html_text_heading\
        .format(category=ctgr,img_count=len(datas)))
    for stor in datas:
        file.write(stor)

def Writing_html_page(datas):
    storing_datas = []
    category_checker = category_change_checker = None

    with open("preview.html",mode='w',encoding='utf_8') as f:
        f.write(FormatText().html_text_header) #header
        for ite,array in enumerate(datas,1):
            flag = False
            array_path,array_title = array[0],array[1]
            category_change_checker = array_title
            
            h,w,_ = cv2.imread(array_path).shape
            div_text = (FormatText().html_text_div)\
                .format(img_path=array_path,height=h,width=w,iteration=ite)
            
            # You can set the conditions for changing the heading
            # ex conditions) When the title is changed 
            if (category_checker!=category_change_checker and category_checker!=None) and ite!=len(datas):
                Writing_heading_and_img_div(f,storing_datas,category_checker)
                flag = True
                storing_datas = []
            
            category_checker = category_change_checker
            storing_datas.append(div_text)

            if flag: continue

            if ite==len(datas):
                Writing_heading_and_img_div(f,storing_datas,category_checker)

def main():
    global CONSOLE_ARGUMENTS
    CONSOLE_ARGUMENTS = Get_args()
    Generate_css_stylesheet()
    # example) datas = [[xxx.jpg,(category_name_a)],
    #                   [xxy.jpg,(category_name_b)],
    #                   [xyy.jpg,(category_name_c)]...]
    data = Input_img_data()
    Writing_html_page(data)

if __name__ == '__main__':
    main()