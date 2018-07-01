#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/29 23:02
# @Author  : bingka.wang 
# @Email   : wangbingka@126.com


def method1(self):
    fbnq_list = [1,1]
    if self == 1:
        return [1]
    elif self == 2:
        return [1,1]
    else:
        i = 0
        while i < int(self)-2:
            a = fbnq_list[i]+fbnq_list[i+1]
            fbnq_list.append(a)
            i +=1
        return fbnq_list

def method2(self):
    fbnq_list = [1,1]
    if self == 1:
        return [1]
    elif self == 2:
        return [1,1]
    else:
        for i in  range(int(self)-2):
            a = fbnq_list[i]+fbnq_list[i+1]
            fbnq_list.append(a)
        return fbnq_list

print(method1(1))
print(method1(2))
print(method1(4))

print(method2(1))
print(method2(2))
print(method2(4))


#此方法严重缺陷，递归层数有限制：
#不断查询，也会非常慢
def fibo(self):
    if self == 1:
        return 1
    elif self == 2:
        return 1
    else:
        return fibo(self-1)+fibo(self-2)
def method3(self):
    fbnq_list = []
    for i in range(1,int(self)+1):
        fbnq_list.append(fibo(i))
    return fbnq_list

print(method3(20))