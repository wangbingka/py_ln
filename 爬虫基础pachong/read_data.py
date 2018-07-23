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
            #文件后缀是".py"，并且文本中包含movie_name
            if file.split('.')[-1] == 'py' and movie_name in file :
                L.append(file)
    return L

#打印后缀是'.py'，并且名称中包含'douban'的文件名称
# print(file_name('douban'))




def similar_movie_count(input_movie):
    dict_movie = {}
    with open('{}.txt'.format(input_movie),'r') as f1:
        lines=f1.readlines()

    for line in lines:
        # print(line)
        #split切片函数，切成列表，
        # strip是清洗字符串前后的空格、换行符、tab符等符号，lstrip只清洗字符串左边的字符，rstrip：清洗右边的字符
        name = line.split(':')[0].strip()
        num1  = int(line.split(':')[1].strip())
        # print(name+':'+str(num1))

        #dict.get(key,0),表现字典中如果没有这个keyName，则默认值为0
        dict_movie[name] = dict_movie.get(name,0)+num1
    #将字典按照值进行降序排列形成新的字典，第一个是，最后一个是排序方式，默认是顺序False，True是降序
    dict_movie1 = sorted(dict_movie.items(), key=lambda x : x[1],reverse=True)

    return (dict_movie1)

# print(similar_movie_count('蛮荒故事'))
# for i in similar_movie_count('蛮荒故事'):
#     print(str(i))