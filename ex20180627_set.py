#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/27 23:02
# @Author  : bingka.wang 
# @Email   : wangbingka@126.com

import random
import string

# 写一个函数，
# 输入：一个数字，例如4
# 输出：四位不同的随机a到z的字母，例如
# 'jsdc'
#set用法

#set，是一个无序的，不重复的集合，如果添加了去重复的元素会自动去重复
# a = set([1,3,9,10,11,8,1])
# print(a) #展示顺序是从小到大，并且自动去重复
# a.add(4) #增加一个元素4
# print(a)
# a.remove(1) #删除一个元素1
# print(a)
# b=a.pop() #随机弹出一个元素，并且a中会删掉这个元素，默认是第一个
# print(a)
# print(b)
# a.remove(4) #有的话会删除，没有这个元素会报错，a.remove(6)
# print(a)
# a.discard(2) #有元素2就删除，没有也不会报错
# print(a)
# a.update(['a','g']) #给元素增加多个元素
# print(a)

# #关系测试
# #交集(两个列表里面都有的值，这里是4、6)：
# print(list_1.intersection(list_2))
#
# #并集（把两个列别合并起来，然后去重）：
# print(list_1.union(list_2))
#
# #差集（把list_1里面有的而list_2里面没有的取出来）：
# print(list_1.difference(list_2))
# #对称差集（两个列表里面，互相没有的取出来，也就是只去掉那些互相都有的值）
# print(list_1.symmetric_difference(list_2))
#
# #子集（判断list_1是否包含了list_3里面的所有值）
# print(list_3.issubset(list_1))
# #父集（判断list_1是否为list_3的父集）
# print(list_1.issuperset(list_3))
#
# #无交集（判断list_3和list_4是否完全没有任何交集）
# list_4 = set([5,6,8])
# print(list_3.isdisjoint(list_4))
#
# #-----------------------关系测试的另一种写法：
# '''
# s = set([3,5,9,10])      #创建一个数值集合
#
# t = set("Hello")         #创建一个唯一字符的集合
#
#
# a = t | s          # t 和 s的并集
#
# b = t & s          # t 和 s的交集
#
# c = t – s          # 求差集（项在t中，但不在s中）
#
# d = t ^ s          # 对称差集（项在t或s中，但不会同时出现在二者中）

#
# len(s)
# set 的长度
#
# x in s
# 测试 x 是否是 s 的成员
#
# x not in s
# 测试 x 是否不是 s 的成员
#
# s.issubset(t)
# s <= t
# 测试是否 s 中的每一个元素都在 t 中
#
# s.issuperset(t)
# s >= t
# 测试是否 t 中的每一个元素都在 s 中
#
# s.union(t)
# s | t
# 返回一个新的 set 包含 s 和 t 中的每一个元素
#
# s.intersection(t)
# s & t
# 返回一个新的 set 包含 s 和 t 中的公共元素
#
# s.difference(t)
# s - t
# 返回一个新的 set 包含 s 中有但是 t 中没有的元素
#
# s.symmetric_difference(t)
# s ^ t
# 返回一个新的 set 包含 s 和 t 中不重复的元素
#
# s.copy()
# 返回 set “s”的一个浅复制
# '''




def func(num):
    need = set()
    az = string.ascii_lowercase
    for i in range(num):
        need.add(random.choice(az))
    return need
print(func(6))

print(func(15))
#发现问题，输出的数据量不到15个，原因是因为set不能保存重复的数据，会自动去重复。

def func(num):
    need = set()
    az = string.ascii_lowercase
    while len(need) < num:
        need.add(random.choice(az))
    return need
print(func(15))