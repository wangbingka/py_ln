#!usr/bin/python
#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time :  2018/9/5 16:19
# @Author: Bingka.wang
# @Email:  wangbingka@126.com

names = locals()
for i in range(1,2):
    names['a%i'%i] = input('Abss %d:'%i)
for i in range(1,2):
    print(names['a%i'%i])