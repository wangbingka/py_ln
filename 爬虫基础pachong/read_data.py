#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/22  22:37
# @Author  : bingka.wang 
# @Email   : wangbingka@126.com

import os


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



def read_data(movie_name):
    with open('{}.txt'.format(movie_name),'r') as f1:
        f1.readlines()