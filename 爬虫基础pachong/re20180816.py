#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time :  2018/8/16 22:55
# @Author: Bingka.wang
# @Email:  wangbingka@126.com

import re

'''
1、re.search，搜索字符串，返回搜索到的第一个字符串，返回一个对象MatchObject
2、re.match，匹配开头，如果匹配不到就无
3、re.split,正则表达式来分割字符串
4、re.findall,根据正则表达式，从左到右搜索匹配项，返回匹配的字符串列别
5、re.finditer,根据正则表达式，从左到右搜索匹配项，返回一个迭代器迭代返回MatchObject: 
6、sub:字符串替换
    patten,将要使用的正则表达式
    repl，新的替换项内容，字符串或函数
    string，待处理的字符串
7、subn,与sub类似，返回值多了替换的字符串个数
8、MatchObject,两个常用的方法：
    group不带索引表示自身项，0同样表示自身第一个，1表示第一个子项，
    groups表示从1之后的所有子项
'''

def re_demo():
    # 解析价格
    txt = 'If you purchase more than 100 sets, the price of product A is $9.90.'
    m = re.search(r'(\d+).*\$(\d+\.?\d*)',txt)

    print(type(m))
    # \d表示数字，+表示1-n多个个数，.表示匹配所有的字符，*表示0到多个所有符号，\$表示匹配$,\.表示匹配.,？表示匹配0-1个，
    print(m.groups())

# search vs match
def re_method():
    s = 'abcd'
    print(re.search(r'c',s))  # 全文搜索'c'
    print(re.search(r'^c',s)) # 开头匹配‘c’
    print(re.search(r'^abc', s))  # 开头匹配'abc'，有值
    print(re.match(r'c',s))  # 开头匹配‘c’
    print(re.match(r'abc', s)) # 开头匹配'abc'
    print(re.match(r'.*c', s))  # 任意位置匹配‘c’

#split
def re_split():
    s = 'This is Joey Huang.'
    # 注意是大写的‘W’，‘\W’表示非字母
    print(re.split(r'\W',s))
    s1 = 'This | is Joey - Huang.'
    print(re.split(r'\W', s1))

def re_findall():
    s1 = 'Hello,this is Kaka.'
    s2 = 'The first price is $9.90,and the second price is $100.'

    # \w，表示任意字符，注意是小写
    print(re.findall(r'\w+',s1))
    print(re.findall(r'\d+\.?\d+',s2))

def re_finditer():
    s2 = 'The first price is $9.90,and the second price is $100.'
    i = re.finditer(r'\d+\.?\d+',s2)
    # 此处不能写成r'\d+\.?\d*，否则如果最后一个数字跟着句号，会把句号带出来。

    # i是个迭代器，里面的每个一个元素都是M
    for m in i:
        print(m.group())

# sub vs subn
def re_subn():
    s2 = 'The first price is $9.90,and the second price is $100.'

    # sub直接返回一个字符串
    print(re.sub(r'\d+\.?\d+','<number>',s2))

    # subn返回一个集合，包括新的字符串，和替换的字符串的个数
    print(re.subn(r'\d+\.?\d+', '<number>', s2))

# MatchObject
def re_match_object():
    s1 = 'Joey Wang'
    m = re.match(r'(\w+) (\w+)',s1)
    # group不带索引表示自身项，0同样表示自身第一个，1表示第一个子项，groups表示从1之后的所有子项
    print(m.group())
    print(m.group(0))
    print(m.group(1))
    print(m.group(0,1,2))
    print(m.groups())

if __name__ == '__main__':
    # re_demo()
    # re_method()
    # re_split()
    # re_findall()
    # re_finditer()
    # re_subn()
    re_match_object()