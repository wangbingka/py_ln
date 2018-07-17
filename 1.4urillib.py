#!usr/bin/python
#coding:utf-8
#author:bingka.wang




from urllib import request
from urllib import error
import time
import urllib



def demo():

    #打开这个网站，返回类文件句柄
    s = request.urlopen('http://blog.kamidox.com')

    #响应类型
    print(s.getcode())

    msg = s.info()
    # print_list(dir(msg))

    time.sleep(1)


def retrive():
\
    fname,msg=urllib.urlretrieve('http://blog.kamidox.com','./index.html')
    print(fname)
    print_list(msg.items())




def print_list(list):
    for i in list:
        print(i)

if __name__ == '__main__':
    retrive()