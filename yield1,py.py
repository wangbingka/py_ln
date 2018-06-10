#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/10 22:22
# @Author  : bingka.wang 
# @Email   : wangbingka@126.com

def yield_test(n):
    for i in range(n):
        yield call(i)
        print("i=",i)
    #做一些其它的事情
    print("do something.")
    print("end.")

def call(i):
    return i*2

#使用for循环
for i in yield_test(5):
    print(i,",")
