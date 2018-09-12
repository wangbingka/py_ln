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

# 打开excel文件
data = xlrd.open_workbook(filename)#文件名以及路径，如果路径或者文件名有中文给前面加一个r转化原生字符。

# 获取所有sheet的名字，返回一个列表
sheets = data.sheet_names()
print(sheets)

#  通过sheet的索引，获取对应的sheet表内容，返回的是一个类，
#  对应的方法有多个，name指sheet的名称，ncols，列数，nrows，行数

sheet1 = data.sheet_by_index(0)
sheet2 = data.sheet_by_index(1)
sheet3 = data.sheet_by_index(2)
print(sheet1.name,sheet1.ncols,sheet1.nrows)
print(sheet2.name,sheet2.ncols,sheet2.nrows)
print(sheet3.name,sheet3.ncols,sheet3.nrows)


print(sheet1.cell(1,0))
print(sheet1.cell(1,0).value)
rows = sheet1.row_values(1)
cols = sheet2.col_values(2)

print(rows)
print(cols)