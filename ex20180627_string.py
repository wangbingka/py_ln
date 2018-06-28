#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/27 23:32
# @Author  : bingka.wang 
# @Email   : wangbingka@126.com


import string

# string.ascii_letters,返回一个从a到z+从A到Z的52个字母的顺序字符串
print(string.ascii_letters)

# string.ascii_lowercase,返回从a到z的26个字母的顺序字符串
print(string.ascii_lowercase)
print(string.ascii_uppercase)  # 从A到Z的26个字母组成的字串串

print(string.digits)  # 返回字符串'0123456789'

print(string.hexdigits)  # 返回'0123456789abcdefABCDEF'

print(string.octdigits)  # 返回'01234567'

a = 'aBcd EFGh'
print(a.upper())  # 将字符a里面的字母都转为大写
print(a.lower())  # 将字符a里面的字母都转为小写
print(a.capitalize())  # 首字母大写，其它小写
print(a.swapcase())  # 大小写对换
print(a.title())  # 分隔符为标记，每个单词的首字母大写，其他小写

b = 'abcd'
c = '1234'
d = '12ac'
print(str(b.isalnum()) + str(c.isalnum()) + str(d.isalnum()))  # 是否全是字母和数字，并至少有一个字符
print(str(b.isdigit()) + str(c.isdigit()) + str(d.isdigit()))  # 判断是否全是数字，并至少有一个字符
print(str(b.isalpha()) + str(c.isalpha()) + str(d.isalpha()))  # 判断是否全是字母，并至少有一个字符
print(str(b.startswith('a')) + str(c.startswith('a')) + str(d.startswith('a')))  # 判断是否以字符a开头
print(str(b.endswith('4')) + str(c.endswith('4')) + str(d.endswith('4')))  # 判断是否以字符4结尾

# >> > str = 'string lEARn'
# >> > str.find('z')  # 查找字符串，没有则返回-1，有则返回查到到第一个匹配的索引
#
# -1
#
# >> > str.find('n')  # 返回查到到第一个匹配的索引
#
# 4
#
# >> > str.rfind('n')  # 返回的索引是最后一次匹配的
#
# 11
#
# >> > str.index('a')  # 如果没有匹配则报错

# >> > str.index("n")  # 同find类似,返回第一次匹配的索引值
#
# 4
#
# >> > str.rindex("n")  # 返回最后一次匹配的索引值
#
# 11
#
# >> > str.count('a')  # 字符串中匹配的次数
#
# 0
#
# >> > str.count('n')  # 同上
#
# 2
#
# >> > str.replace('EAR', 'ear')  # 匹配替换
#
# 'string learn'
#
# >> > str.replace('n', 'N')
#
# 'striNg lEARN'
#
# >> > str.replace('n', 'N', 1)
#
# 'striNg lEARn'


class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return 'Point(%s,%s)'%(self.x,self.y)

a = Point(3,4)
print(str(a))

