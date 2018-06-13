#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/13 22:06
# @Author  : bingka.wang 
# @Email   : wangbingka@126.com

import operator
#tuple
a = (1,2,3)
b = ('a','b','c')
b1 = ('a','b','c','d')
print(a+b)
print(max(b))
print(list(b1))
print(tuple(list(b1)))
#dic,key键是不可以改变，但可以删除也可以增加，值可以改变
d ={'a':1,'b':2,'c':3}
print(d['c'])
d['c']=4 #修改字典中具体键对应的值
d['i']=10 #如果字典中没有这个key，就直接在增加对应的key键和值
print(d)
print(d['c'])
del d['c']
# print(d['c']) 'c'键已被删除，所以会报错
print(str(d))


e = d.get('a', None) #返回字典d中key为'a'对应的值，如果没有就返回后面的值
print(e)
f = d.get('e', None)
print(f)
g = d.get('g','g')
print(g)

h =d #浅拷贝，d变化，h也会跟着变，类似别名
h =d.copy() #深拷贝，d变化，h不会跟着变，复制字典d，并赋值给h,和 h=d的区别，
print(d)
print(h)

print(d.__contains__('a')) #查看字典中是否有'a'这个键，有的话是True，没有False
print(a.__contains__('j'))
