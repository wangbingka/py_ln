#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time :  2018/9/13 22:01
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

sheet1_rows = sheet1.nrows
sheet2_rows = sheet2.nrows
sheet3_rows = sheet3.nrows

'''
1、表1有100行，每行是一个每列数据组成的列表，再把每行的列表组成一个新的列表

'''


sheet1_list = []
sheet2_list = []
sheet3_list = []
newsheet_list = []
for i in range(0,sheet1.nrows):
    cols = sheet1.row_values(i)
    sheet1_list.append(cols)
for i in range(0,sheet2.nrows):
    cols = sheet2.row_values(i)
    sheet2_list.append(cols)
for i in range(0,sheet3.nrows):
    cols = sheet3.row_values(i)
    sheet3_list.append(cols)

cols = 0
while cols <sheet1.nrows:
    for i in range(0,sheet2.nrows):
        # print(sheet2.nrows)
        # print(len(sheet2_list))
        if sheet2_list[i][0] == sheet1_list[cols][0] and sheet2_list[i][2] == sheet1_list[cols][2]:
            newcols = sheet1_list[cols] +sheet2_list[i]
            print(newcols)
            newsheet_list.append(newcols)
            # sheet1_list.remove(sheet1_list[cols])
            newcols = []
        else:
            continue
    cols += 1
print(newsheet_list)
print(len(newsheet_list))

cols = 0
while cols <len(newsheet_list):
    for i in range(0,len(sheet1_list)):
        print(len(sheet1_list))
        if sheet1_list[i][0] == newsheet_list[cols][0] and sheet1_list[i][2] == newsheet_list[cols][2]:
            # newsheet_list.append(newcols)
            sheet1_list.remove(sheet1_list[i])
        else:
            continue
    cols += 1
newsheet_list +=sheet1_list
print(newsheet_list)
print(len(newsheet_list))






print(sheet1.name,sheet1.ncols,sheet1.nrows)
print(sheet2.name,sheet2.ncols,sheet2.nrows)
print(sheet3.name,sheet3.ncols,sheet3.nrows)

rows = sheet1.row_values(1)
cols = sheet2.col_values(2)

print(rows)
print(cols)
