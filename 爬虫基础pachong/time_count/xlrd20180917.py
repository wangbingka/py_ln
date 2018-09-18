#!usr/bin/python
#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time :  2018/9/17 15:31
# @Author: Bingka.wang
# @Email:  wangbingka@126.com


# !/usr/bin/python
# -*- coding:utf-8 -*-
# @Time :  2018/9/13 22:01
# @Author: Bingka.wang
# @Email:  wangbingka@126.com


import xlrd
import os

filepath = os.getcwd()
print(filepath)


filename = r'天津血液病检验时间分布.xlsx'

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
# sheet2 = data.sheet_by_index(1)
# sheet3 = data.sheet_by_index(2)

sheet1_rows = sheet1.nrows
# sheet2_rows = sheet2.nrows
# sheet3_rows = sheet3.nrows

sheet1_list = []
# sheet2_list = []
# sheet3_list = []

for i in range(0, sheet1.nrows):
    cols = sheet1.row_values(i)
    if isinstance(cols[-1],int) or isinstance(cols[-1],float):
        sheet1_list.append(cols)
    else:
        pass
print(sheet1_list)

visit_type = set()
for i in sheet1_list:
    visit_type.add(i[1])
table_type = set()
for i in sheet1_list:
    table_type.add(i[2])


def avarage_month(self):
    counts = []
    result_list = []
    for i in self:
        # print(i)
        # print(i[-1])
        counts.append(i[-1])
    sum = 0
    for a in counts:
        sum +=a

    avarage = sum/len(counts)
    print(sum)
    print(len(counts))
    print(avarage)

    normal_list = []
    wrong_list = []
    for i in self:
        if i[-1] < avarage*5 and i[-1] > avarage/5:
            normal_list.append(i)
        else:
            wrong_list.append(i)
    result_list.append(normal_list)
    result_list.append(wrong_list)
    return result_list

def near_month(self):
    mouth_list = []
    list1 = []
    for i in range(0,len(self)-1):
        if i ==0:
            list2 = []
            list2.append(self[i])
            list2.append(self[i+1])
            print(list2)
            list1.append(list2)
        if i == len(self)-2:
            list3 = []
            list3.append(self[i])
            list3.append(self[i + 1])
            print(list3)
            list1.append(list3)
        else:
            list4 = []
            list4.append(self[i])
            list4.append(self[i + 1])
            list4.append(self[i+2])
            print(list4)
            list1.append(list4)
    print(list1)



a = [1,2,3,4,5,6]
near_month(a)



for a in visit_type:
    for b in table_type:
        print(a, b)
        type_list = []
        for i in sheet1_list:
            if i[1] == a and i[2] == b:
                type_list.append(i)
        c = avarage_month(type_list)
        print(c[0])
        print(c[1])

'''
1、算出所有月份的平均值
2、判断当前月份对应的值是否是大于平均值的五分之一，并小于平均值的五倍，如果是则记录，如果不是则正常并且新的纪录
3、排列顺序，取出最大的月份，和最小的月份，并且判断最小的月份和后一个月份是连续的，如果不是则继续
'''

# for i in range(0, sheet2.nrows):
#     cols = sheet2.row_values(i)
#     cols_list = []
#     # 1,2,3,4,6,12,14
#     cols_list.append(cols[0])
#     cols_list.append(cols[1])
#     cols_list.append(cols[2])
#     cols_list.append(cols[3])
#     cols_list.append(cols[5])
#     cols_list.append(cols[11])
#     cols_list.append(cols[13])
#     sheet2_list.append(cols_list)
# for i in range(0, sheet3.nrows):
#     cols = sheet3.row_values(i)
#     cols_list = []
#     # 1,2,3,4,5,6
#     cols_list.append(cols[0])
#     cols_list.append(cols[1])
#     cols_list.append(cols[2])
#     cols_list.append(cols[3])
#     cols_list.append(cols[4])
#     cols_list.append(cols[5])
#     sheet3_list.append(cols_list)


'''
1、表1有100行，每行是一个每列数据组成的列表，再把每行的列表组成一个新的列表

'''


def union_list(self1, self2):
    newsheet_list = []
    cols = 0
    while cols < len(self1):
        for i in range(0, len(self2)):

            if self2[i][0] == self1[cols][0] and self2[i][2] == self1[cols][2]:
                newcols = self1[cols] + self2[i]
                newsheet_list.append(newcols)
            else:
                continue
        cols += 1
    # print(newsheet_list)
    # print(len(newsheet_list))

    cols = 0
    del_list = []
    while cols < len(newsheet_list):
        for i in range(0, len(sheet1_list)):
            if self1[i][0] == newsheet_list[cols][0] and self1[i][2] == newsheet_list[cols][2]:
                # newsheet_list.append(newcols)
                del_list.append(self1[i])
            else:
                continue
        cols += 1
    print(len(self1))
    print(len(del_list))
    ret = [i for i in self1 if i not in del_list]
    # print(len(ret))
    newsheet_list += ret
    # print(newsheet_list)
    # print(len(newsheet_list))
    return newsheet_list


def write_data(self,txt_name):
    with open('{}.txt'.format(txt_name),'a+',encoding='utf8') as f:
        f.write(self)




# if __name__ == '__main__':

    # newsheet_list = union_list(sheet1_list, sheet2_list)
    # newsheet_list = union_list(newsheet_list,sheet3_list)
    # for i in newsheet_list:
    #     for a in i:
    #         write_data(str(a) + '\t', 'diff_count')
    #     write_data('\n', 'diff_count')
