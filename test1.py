#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/9 21:26
# @Author  : bingka.wang 
# @Email   : wangbingka@126.com

# def recursion(i):   #定义函数
#     print(i)
#     if i/2 > 1:   #判断递归条件，退出
#         re = recursion(i/2)  #递归函数自身
#         print('返回值:',re)
#     print('上层递归值：',i)
#     return i     #返回值
#
# recursion(10)
# recursion(3)

# def foo(arg1,arg2,stop):
#     if arg1 == 0:
#         print(arg1,arg2)
#     arg3 = arg1 + arg2
#     print(arg1,arg2,arg3)
#     if arg3 < stop:      #判断套件不满足时退出递归
#         foo(arg2,arg3,stop)
#
# foo(1,10,100)

def foo(stop):
    list1 = [0,1]
    if list1[0] ==0:
        print(list1[0],list1[1])
    num3 = list1[0]+list1[1]

    arg3 = arg1 + arg2
    print(arg1,arg2,arg3)
    if arg3 < stop:      #判断套件不满足时退出递归
        foo(stop)

foo(1000)