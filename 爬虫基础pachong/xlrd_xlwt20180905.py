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


# 以上三个函数都会返回一个xlrd.sheet.Sheet()对象
'''
table = data.sheets()[0]          #通过索引顺序获取
table = data.sheet_by_index(sheet_indx)) #通过索引顺序获取
table = data.sheet_by_name(sheet_name)#通过名称获取


行的操作
nrows = table.nrows  #获取该sheet中的有效行数
table.row(rowx)  #返回由该行中所有的单元格对象组成的列表
table.row_slice(rowx)  #返回由该列中所有的单元格对象组成的列表
table.row_types(rowx, start_colx=0, end_colx=None)    #返回由该行中所有单元格的数据类型组成的列表
table.row_values(rowx, start_colx=0, end_colx=None)   #返回由该行中所有单元格的数据组成的列表
table.row_len(rowx) #返回该列的有效单元格长度

列(colnum)的操作
ncols = table.ncols   #获取列表的有效列数
table.col(colx, start_rowx=0, end_rowx=None)  #返回由该列中所有的单元格对象组成的列表
table.col_slice(colx, start_rowx=0, end_rowx=None)  #返回由该列中所有的单元格对象组成的列表
table.col_types(colx, start_rowx=0, end_rowx=None)    #返回由该列中所有单元格的数据类型组成的列表
table.col_values(colx, start_rowx=0, end_rowx=None)   #返回由该列中所有单元格的数据组成的列表


excel数据类型：
ctype : 0 empty,1 string, 2 number，包括int和float, 3 date, 4 boolean,False, 5 error,例如：#DIV/0!

sheet2.cell(1,0).ctype 
sheet2.cell_type(1,0).ctype 
'''


'''
1.xlrd.Book类
•nsheets----->sheet_by_index(sheet index)
•sheet_names---->sheet_by_name(sheet name)
•sheets

2.xlrd.Sheet类
•name
•nrows
•ncols
•row(row index)
•col(col index)
•row_types(start index,optional end index)
•col_types(start index,optional end index)
•row_slice(start index,optional end index)
•col_slice(start index,optional end index)


3.xlrd.Sheet.Cell类
•value=sheet.cell_value
•ctype=sheet.cell_type

4.Cell Type
•Text:xlrd.XL_CELL_TEXT

•Number:xlrd.XL_CELL_NUMBER
•Date: xlrd.XL_CELL_DATE
•Booleanxlrd.XL_CELL_BOOLEAN
•Errorxlrd.XL_CELL_ERROR
•Empty/Blank

             xlrd.XL_CELL_EMPTY
              xlrd.XL_CELL_BLANK 
'''



#  通过sheet的索引，获取对应的sheet表内容，返回的是一个类，
#  对应的方法有多个，name指sheet的名称，ncols，列数，nrows，行数

sheet1 = data.sheet_by_index(0)
sheet2 = data.sheet_by_index(1)
sheet3 = data.sheet_by_index(2)
print(sheet1.name,sheet1.ncols,sheet1.nrows)
print(sheet2.name,sheet2.ncols,sheet2.nrows)
print(sheet3.name,sheet3.ncols,sheet3.nrows)


r1,c1=2,2
print('第%s行第%s列的值'%(r1,c1),sheet1.cell(r1-1,c1-1))
print('第%s行第%s列的值的数据类型ctype:'%(r1,c1),sheet1.cell(r1-1,c1-1).ctype)
print('第%s行第%s列的值的数据类型cell_type:'%(r1,c1),sheet1.cell_type(r1-1,c1-1))
r1,c1=2,3
print('第%s行第%s列的值'%(r1,c1),sheet1.cell(r1-1,c1-1))
print('第%s行第%s列的值的数据类型ctype:'%(r1,c1),sheet1.cell(r1-1,c1-1).ctype)
print('第%s行第%s列的值的数据类型cell_type:'%(r1,c1),sheet1.cell_type(r1-1,c1-1))
r1,c1=2,4
print('第%s行第%s列的值'%(r1,c1),sheet1.cell(r1-1,c1-1))
print('第%s行第%s列的值的数据类型ctype:'%(r1,c1),sheet1.cell(r1-1,c1-1).ctype)
print('第%s行第%s列的值的数据类型cell_type:'%(r1,c1),sheet1.cell_type(r1-1,c1-1))
r1,c1=2,7
print('第%s行第%s列的值'%(r1,c1),sheet1.cell(r1-1,c1-1))
print('第%s行第%s列的值的数据类型ctype:'%(r1,c1),sheet1.cell(r1-1,c1-1).ctype)
print('第%s行第%s列的值的数据类型cell_type:'%(r1,c1),sheet1.cell_type(r1-1,c1-1))
r1,c1=3,7
print('第%s行第%s列的值'%(r1,c1),sheet1.cell(r1-1,c1-1))
print('第%s行第%s列的值的数据类型ctype:'%(r1,c1),sheet1.cell(r1-1,c1-1).ctype)
print('第%s行第%s列的值的数据类型cell_type:'%(r1,c1),sheet1.cell_type(r1-1,c1-1))
r1,c1=4,7
print('第%s行第%s列的值'%(r1,c1),sheet1.cell(r1-1,c1-1))
print('第%s行第%s列的值的数据类型ctype:'%(r1,c1),sheet1.cell(r1-1,c1-1).ctype)
print('第%s行第%s列的值的数据类型cell_type:'%(r1,c1),sheet1.cell_type(r1-1,c1-1))
r1,c1=5,7
print('第%s行第%s列的值'%(r1,c1),sheet1.cell(r1-1,c1-1))
print('第%s行第%s列的值的数据类型ctype:'%(r1,c1),sheet1.cell(r1-1,c1-1).ctype)
print('第%s行第%s列的值的数据类型cell_type:'%(r1,c1),sheet1.cell_type(r1-1,c1-1))
r1,c1=6,7
print('第%s行第%s列的值'%(r1,c1),sheet1.cell(r1-1,c1-1))
print('第%s行第%s列的值的数据类型ctype:'%(r1,c1),sheet1.cell(r1-1,c1-1).ctype)
print('第%s行第%s列的值的数据类型cell_type:'%(r1,c1),sheet1.cell_type(r1-1,c1-1))
r1,c1=7,7
print('第%s行第%s列的值'%(r1,c1),sheet1.cell(r1-1,c1-1))
print('第%s行第%s列的值的数据类型ctype:'%(r1,c1),sheet1.cell(r1-1,c1-1).ctype)
print('第%s行第%s列的值的数据类型cell_type:'%(r1,c1),sheet1.cell_type(r1-1,c1-1))


rows = sheet1.row_values(1)
cols = sheet2.col_values(2)

print(rows)
print(cols)