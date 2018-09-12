#!usr/bin/python
#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time :  2018/9/5 16:19
# @Author: Bingka.wang
# @Email:  wangbingka@126.com

import xlrd
import os

filepath = os.getcwd()
print(filepath)


filename = r'元数据与戴明中英文表名和字段名对应_schema371_20180802.xlsx'

filename1 = filepath+'\\'+filename

print(filename1)

data = xlrd.open_workbook(filename)#文件名以及路径，如果路径或者文件名有中文给前面加一个r转化原生字符。

print(data)