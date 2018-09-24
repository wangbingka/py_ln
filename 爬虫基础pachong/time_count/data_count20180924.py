#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time :  2018/9/24 17:29
# @Author: Bingka.wang
# @Email:  wangbingka@126.com


class dataCount():
    def __init__(self,filename=''):
        self.filename = filename
    def __int_list(self):
        int_list_str = []
        for i in self:
            if isinstance(i, int) or isinstance(i, float) or i.isdigit():
                a = int(i)
                # print(a)
                int_list_str.append(a)
            else:
                int_list_str.append(i)
        return int_list_str

    def datelist(self):
        with open('self', 'r+') as f:
            sheet1_list = []
            for line in f:
                # print(line)
                # print(type(line))
                conts = line.split('\t')
                conts1 = []
                for i in conts:
                    b = i.replace('\n', '')
                    conts1.append(b)
                conts2 = __int_list(conts1)
                if isinstance(conts2[-1], int):
                    sheet1_list.append(conts2)
                else:
                    pass
        return sheet1_list


import xlrd
import os

filepath = os.getcwd()
print(filepath)



filename = 'R0019_pris.sql_chinablood_371_1_schema.txt'

filename1 = filepath+'\\'+filename


def int_list(self):
    int_list_str = []
    for i in self:
        if isinstance(i, int) or isinstance(i, float) or i.isdigit():
            a = int(i)
            # print(a)
            int_list_str.append(a)
        else:
            int_list_str.append(i)
    return int_list_str

def datelist(self):
    with open('self','r+') as f:
        sheet1_list = []
        for line in f:
            # print(line)
            # print(type(line))
            conts = line.split('\t')
            conts1 = []
            for i in conts:
                b = i.replace('\n','')
                conts1.append(b)
            conts2 = int_list(conts1)
            if  isinstance(conts2[-1], int):
                sheet1_list.append(conts2)
            else:
                pass
    print(sheet1_list)
    print(len(sheet1_list))
    return sheet1_list

def typelist(self):
    type_list = []
    for i in self:
        visit_type = []
        visit_type.append(i[1])
        visit_type.append(i[2])
        if visit_type not in type_list:
            type_list.append(visit_type)
    return type_list


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

    normal_list = []
    for i in self:
        if i[-1] < avarage*5 and i[-1] > avarage/5 and i[3] in range(1990, 2019) and i[4] in range(0, 13):
            normal_list.append(i)
        else:
            pass

    result_list.append(sum)
    result_list.append(avarage)
    result_list.append(normal_list)
    return result_list

def near_twolist(self):
    list1 = []
    for i in range(0,len(self)-1):
            list5 = []
            list5.append(self[i])
            list5.append(self[i+1])
            list1.append(list5)
    return list1


def near_month(self):

    list2 = list(reversed(near_twolist(self)))

    # 相邻月份，相互差距应小于3倍
    common_month = []
    while list2 != []:
        # print('list2:%s'%list2)
        now_list = list2.pop()
        # print('now_list:%s' % now_list)
        if now_list[0][-1] >  (now_list[1][-1])/3 and now_list[0][-1] <  (now_list[1][-1])*3:
            if now_list[0] not in common_month:
                common_month.append(now_list[0])
            if now_list[1] not in common_month:
                common_month.append(now_list[1])
        else:
            pass
    year_month1 = list(reversed(near_twolist(common_month)))


    num = 0
    start_num =1
    start_year_month = {}
    while year_month1 != []:
        start_end_year_month = year_month1.pop()
        # print('start_end_year_month:%s'%start_end_year_month)
        if num==0:
            # print('num:0')
            current_list = []
            current_list.append(start_end_year_month[0][3])
            current_list.append(start_end_year_month[0][4])
            start_year_month['start%s_year_month'%start_num] = '%s_%s'%(start_end_year_month[0][3],start_end_year_month[0][4])
            start_year_month['start%s_year_month' % start_num] = current_list
            current_list = []
            current_list.append(start_end_year_month[1][3])
            current_list.append(start_end_year_month[1][4])
            start_year_month['end%s_year_month' % start_num] = current_list


        else:
            if (start_end_year_month[0][3] == start_end_year_month[1][3] and start_end_year_month[0][4]+1 == start_end_year_month[1][4]) or (start_end_year_month[0][3]+1 == start_end_year_month[1][3] and start_end_year_month[0][4]-11 == start_end_year_month[1][4]):
                start_year_month['end%s_year_month'%start_num] = '%s_%s' % (start_end_year_month[1][3],start_end_year_month[1][4])
                current_list = []
                current_list.append(start_end_year_month[1][3])
                current_list.append(start_end_year_month[1][4])
                start_year_month['end%s_year_month' % start_num] = current_list


            else:
                start_num +=1
                start_year_month['start%s_year_month'%start_num] = '%s_%s' % (start_end_year_month[1][3],start_end_year_month[1][4])

                current_list = []
                current_list.append(start_end_year_month[1][3])
                current_list.append(start_end_year_month[1][4])
                start_year_month['start%s_year_month' % start_num] = current_list
        num +=1

    # 标记出各个正常数据量的起始月份阶段
    start_end_year_month_list = []
    for a in start_year_month.keys():
        start_end_year_month = []
        start_end_year_month.append(a)
        start_end_year_month.append(start_year_month[a])
        start_end_year_month_list.append(start_end_year_month)


    print('start_end_year_month_list,长度:%s,内容:%s' % (len(start_end_year_month_list), start_end_year_month_list))
    start_end_year_month_list_neartwo = near_twolist(start_end_year_month_list)

    # 标记出错误月份，以及错误月份对应的数据量
    wrong_month = []
    for i in start_end_year_month_list_neartwo:
        if i[0][0].startswith('end') and i[0][1][0] == i[1][1][0]:
            for a in range(int(i[0][1][1])+1,int(i[1][1][1])):
                year_month_list = []
                year_month_list.append(i[0][1][0])
                year_month_list.append(a)
                wrong_month.append(year_month_list)
        elif i[0][0].startswith('end') and i[0][1][0] != i[1][1][0]:
            for a in range(int(i[0][1][0]),int(i[1][1][0])+1):
                year_month_list = []
                b = i[0][1][1]
                while a < int(i[1][1][0]) and b < 12:
                    year_month_list = []
                    year_month_list.append(a)
                    b +=1
                    year_month_list.append(b)
                    wrong_month.append(year_month_list)
                c = i[1][1][1]
                d = 1
                while a == int(i[1][1][0]) and d <i[1][1][1]:
                    year_month_list = []
                    year_month_list.append(a)
                    d += 1
                    year_month_list.append(b)
                    wrong_month.append(year_month_list)

        else:
            pass

    print(wrong_month)
    return start_year_month


'''
1、算出所有月份的平均值
2、判断当前月份对应的值是否是大于平均值的五分之一，并小于平均值的五倍，如果是则记录，如果不是则正常并且新的纪录
3、每两个组成一个组合进行对比，前一个要保证大于后一个的2分之一并小于前一个的2倍，否则删除进行下一个操作，直到有满足条件的，一直往下取，形成新的列表
4、
3、排列顺序，取出最大的月份，和最小的月份，并且判断最小的月份和后一个月份是连续的，如果不是则继续
'''


if __name__ == '__main__':
    sheet1_list = datelist(filename)
    for i in sheet1_list:
        if i[1] == type and i[2] == b:
            type_list.append(i)
    c = avarage_month(type_list)
    print(c)
    near_month(c[2])
            # print(c[0])
            # print(c[1])