#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time :  2018/8/18 22:45
# @Author: Bingka.wang
# @Email:  wangbingka@126.com

import re

def re_pattern_syntax_meta_char():
    # \number，表示第number个正则类字符串后面是重复的
    print(re.search(r'(\d)(\d)(\d)\1\2\3','135135').groups())
    print(re.search(r'(\d{3})\1', '135135').group())
    r1= 'The Phone Number is 138-2231-2998'
    print(re.search(r'(\d{3}-\d{4}-\d{4})',r1).groups())

    # \b表示不匹配任何东西，但是匹配字符的开头和结尾
    # \D表示各种特殊符号，\s表示空格，\S表示非空格，广义的包括：[\t\n\r\f\v],\t回车，\n回车，\r制表符，\f换页,\v垂直制表符
    # \w表示[a-zA-Z0-9],\W表示之外非单词和数字字符
    # re.IGNORECASE,忽略匹配的大小写
    # 正则表达式太复杂，内部可以加注释
    # re.compile/re.VERBOSE,这是个类，类似re一样，有各种方法，可以大大提高效率
    # \d表示数字，+表示1-n多个个数，*表示0到多个所有符号，\.表示匹配.,？表示匹配0-1个，
    # .表示匹配任意字符
    # {}，表示这类字符的长度，{3表示长度为3，{3,8}表示长度3到8之间
    # |表示或者两种都行
    # [0-9]表示从0到9都可以，[125]表示只能是1或者2或者5
    telNo  = ['13774347721',
              '137-7434-7721',
              '+8613774347721',
              '+86137-7434-7721',
              '8613774347721']
    r = re.compile(r'''
                    \d+   # 整数部分
                    \.?   # 小数点，可能有也可能无
                    \d*   # 小数部分，可选
                    ''',re.VERBOSE)
    r_tel = re.compile(r'''
        1[35678]\d  # 前三位纯数字，第一位1，第二位35678，第三位随意
        \d{4}  # 四位纯数字
        \d{4}  # 四位纯数字1
    ''',re.VERBOSE)
    for i in telNo:
        # print(i)
        print(r_tel.search(i).group())

    # \+?  # +，可选一个
    # 86?  # 86，可选
    # 1[35678]\d  # 以1开头的三位数字，第二位只能是35678，第三位任意数字
    # \d{4}  # 四位纯数字
    # \d{4}  # 四位纯数字


    s = 'the number is 20.5'
    r = re.compile(r'''
                    \d+   # 整数部分
                    \.?   # 小数点，可能有也可能无
                    \d*   # 小数部分，可选
                    ''',re.VERBOSE)
    print('re:',end='')
    print(re.search(r,s).group())
    print('compile/re.VERBOSE:', end='')
    print(r.search(s).group())


    print('re.IGNORECASE:', end='')
    print(re.match(r'(Name)\s*:\s*(\w+)', 'NAME :  Joey',re.IGNORECASE).groups())

    print('\w\W:',end='')
    print(re.match(r'(\w+)\s*:\s*(\w+)', 'Name :  Joey').groups())


    print('\s:', end='')
    print(re.match(r'Name\s*:\s*([a-zA-Z]+)', 'Name: \t Joey').groups(),end='')
    print(re.search(r'Name*:\s*([a-zA-Z]+)', 'FirstName: \t Joey').groups())
    print('\S:', end='')
    print(re.search(r'\S*:\s*([a-zA-Z]+)', 'FirstName123: \t Joey').groups())

    r1 = 'The Phone Number is 138-2231-2998'
    print('\\b:', end='')
    print(re.search(r'\b(\d{3}\D\d{4}-\d{4})\b', r1).groups())


if __name__ == '__main__':
    re_pattern_syntax_meta_char()
