#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/22  22:37
# @Author  : bingka.wang 
# @Email   : wangbingka@126.com

import os
import collections

def file_name(movie_name):
    L=[]
    file_dir = os.getcwd()
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            # L.append(file)
            if file.split('.')[-1] == 'py' and movie_name in file :
                L.append(file)
    return L
print(file_name('douban'))

c= Counter()

def read_data():
    with open('{}.txt'.format('邪不压正'),'r') as f1:
        lines=f1.readlines()

    for line in lines:
        # print(line)

        #split切片函数，切成列表，
        # strip是清洗字符串前后的空格、换行符、tab符等符号，lstrip只清洗字符串左边的字符，rstrip：清洗右边的字符
        name = line.split(':')[0].strip()
        num1  =int(line.split(':')[1].strip())
        print(name+':'+num1)

        c(name) = c(name)+num1
read_data()