#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/22  21:54
# @Author  : bingka.wang 
# @Email   : wangbingka@126.com

import datetime

#获取当前的时间
a=datetime.datetime.now()
b=a.strftime("%Y%m%d_%H%M%S")


def create_write_data():
    with open('{}.txt'.format('邪不压正'),'w+') as name:
        name.truncate()

def write_data(movie_name):
    with open('{}.txt'.format('邪不压正'),'a+') as f:
        f.writelines(movie_name+'\n')

create_write_data()
write_data('222')