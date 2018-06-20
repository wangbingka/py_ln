#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/20 23:30
# @Author  : bingka.wang 
# @Email   : wangbingka@126.com

import random

class Nums:
    def __init__(self,start=0,stop=100,count=10):
        self.start=start
        self.stop=stop
        self.count=count

    def numlist(self):
        i = 1
        a = []
        while True and i < int(self.count)+1:
            num1 = random.randint(self.start,self.stop)
            a.append(num1)
            i +=1
        return a



class Point:
    def __init__(self,list):
        self.list=list

    def x_y(self):
        while True:
            x1=self.re_num()
            x2=self.re_num()
            return '<point {}:{}>'.format(x1,x2)
    def re_num(self):
        i =random.choice(self.list)
        self.list.remove(i)
        return i



a = Nums(10,17,10)
print(a.numlist())

b= Point(a.numlist())
print(b.x_y())

