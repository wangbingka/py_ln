#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/21  23:18
# @Author  : bingka.wang
# @Email   : wangbingka@126.com

import random

a = random.uniform(1, 3)
#控制随机数的精度round(数值，精度)
print(a)

b= str(random.uniform(1, 3))+'成功啦'
print(b)
b= '成功啦'+str(round(random.uniform(1, 1000),0))
print(b)