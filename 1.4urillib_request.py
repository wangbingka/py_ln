#!usr/bin/python
#coding:utf-8
#author:bingka.wang




from urllib import request
from urllib import error
import time



def demo():

    #打开这个网站，返回类文件句柄
    s = request.urlopen('http://blog.kamidox.com')

    #响应类型
    print(s.getcode())

    #打印前3的所有字符
    # redaline：逐行打印，readlines：打印所有行，close():关闭，getcode:返回相应类型
    # print(s.read(3))

    # 打印前10行，并标记行数
    #     for i in range(0,3):
    #         print('line %d:%s'%(i+1,s.readline()))

    lines = s.readlines()
    print(lines)
    print_list(lines)

    #设置sleep()等待一段时间后继续下面的操作,防止被认为时攻击无法获取数据
    time.sleep(1)


    # try:
    #     lines = s.readlines()
    #     print(lines)
    #     print_list(lines)
    #
    # except error.URLError as e:
    #     print(e.reason)
    # time.sleep(1)


def print_list(list):
    for i in list:
        print(i)

if __name__ == '__main__':
    demo()