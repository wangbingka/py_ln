#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/13 22:32
# @Author  : bingka.wang 
# @Email   : wangbingka@126.com

print(str(abs(-1))+str(abs(5))) #abs，取绝对值

print(divmod(10,3)) #divmod(a,b)，返回一个整除数，一个余数的元组

#如果iterable的所有元素不为0、''、False或者iterable为空，all(iterable)返回True，否则返回False；
#注意：空元组、空列表返回值为True，这里要特别注意。
b=['1','a','c','-3+c']
c=[]
d=[0,'-1']
print(all(b))
print(all(c))
print(all(d))