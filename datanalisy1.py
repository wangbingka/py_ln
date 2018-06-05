#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/5 20:06
# @Author  : bingka.wang 
# @Email   : wangbingka@126.com

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,10,1000)
y = np.sin(x)+1
z = np.cos(x**2)+1
plt.figure(figsize=(8,4))
