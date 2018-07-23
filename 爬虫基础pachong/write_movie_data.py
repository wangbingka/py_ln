#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/22  21:54
# @Author  : bingka.wang 
# @Email   : wangbingka@126.com

import datetime

#获取当前的时间
a=datetime.datetime.now()
b=a.strftime("%Y%m%d_%H%M%S")


def create_write_data(input_movie):
    with open('{}.txt'.format(input_movie),'w+') as name:
        name.truncate()

def write_data(input_movie,movie_name):
    with open('{}.txt'.format(input_movie),'a+') as f:
        f.writelines(movie_name+'\n')

