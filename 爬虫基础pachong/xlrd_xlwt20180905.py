#!usr/bin/python
#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time :  2018/9/5 16:19
# @Author: Bingka.wang
# @Email:  wangbingka@126.com

import xlrd


data = xlrd.open_workbook(filename)#文件名以及路径，如果路径或者文件名有中文给前面加一个r转化原生字符。