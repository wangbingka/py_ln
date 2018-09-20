#!usr/bin/python
#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time :  2018/9/20 15:18
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
sheet1_rows = sheet1.nrows

sheet1_list = []

for i in range(0, sheet1.nrows):
    cols = sheet1.row_values(i)
    if isinstance(cols[-1],int) or isinstance(cols[-1],float) and \
            (isinstance(cols[3], int) or isinstance(cols[4], float) ) and cols[3] in range(1990, 2019) and cols[4] in range(0, 13):

        cols1 = int_list(cols)
        sheet1_list.append(cols1)
    else:
        pass
print('sheet1_list长度:%s,内容:%s'%(len(sheet1_list),sheet1_list))


visit_type = set()
for i in sheet1_list:
    visit_type.add(i[1])
table_type = set()
for i in sheet1_list:
    table_type.add(i[2])



def int_list(self):
    int_list_str = []
    for i in self:
        if isinstance(i, int) or isinstance(i, float):
            a = int(i)
            # print(a)
            int_list_str.append(a)
        else:
            int_list_str.append(i)
    return int_list_str





class dataCount():
    def __init__(self,data_list):
        self.data_list = data_list
        def avarage_month(self):
            counts = []
            result_list = []
            for i in self:
                # print(i)
                # print(i[-1])
                counts.append(i[-1])
            sum = 0
            for a in counts:
                sum += a
            avarage = sum / len(counts)
            # print(sum)
            # print(len(counts))
            # print(avarage)
            result_list.append(sum)
            result_list.append(avarage)
            return result_list

        def near_twolist(self):
            list1 = []
            for i in range(0, len(self) - 1):
                # if (isinstance(self[i][3], int) or isinstance(self[i][4], float) ) and int(self[i][3]) in range(1990, 2019) and int(self[i][4]) in range(0, 13):
                list5 = []
                list5.append(self[i])
                list5.append(self[i + 1])
                list1.append(list5)
            return list1


















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
    # print(sum)
    # print(len(counts))
    # print(avarage)

    result_list.append(sum)
    result_list.append(avarage)
    return result_list




def near_month(self):
    print('self,长度:%s,内容:%s' % (len(self), self))
    # list1 = []
    # for i in range(0,len(self)-1):
    #     # if (isinstance(self[i][3], int) or isinstance(self[i][4], float) ) and int(self[i][3]) in range(1990, 2019) and int(self[i][4]) in range(0, 13):
    #         list5 = []
    #         list5.append(self[i])
    #         list5.append(self[i+1])
    #         list1.append(list5)

    list2 = list(reversed(near_twolist(self)))
    print('list2,长度:%s,内容:%s'%(len(list2),list2))

    common_month = []
    while list2 != []:
        # print('list2:%s'%list2)
        now_list = list2.pop()
        # print('now_list:%s' % now_list)
        if now_list[0][-1] >  (now_list[1][-1])/2 and now_list[0][-1] <  (now_list[1][-1])*2 :
            if now_list[0] not in common_month:
                common_month.append(now_list[0])
            if now_list[1] not in common_month:
                common_month.append(now_list[1])
        else:
            pass
    print('common_month,长度:%s,内容:%s'%(len(common_month),common_month))


    year_month1 = list(reversed(near_twolist(common_month)))

    print('year_month1,长度:%s,内容:%s' % (len(year_month1), year_month1))

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

    print('start_year_month,长度:%s,内容:%s' % (len(start_year_month), start_year_month))

    start_end_year_month_list = []
    for a in start_year_month.keys():
        start_end_year_month = []
        start_end_year_month.append(a)
        start_end_year_month.append(start_year_month[a])
        # print(a)
        # print(i[a])
        start_end_year_month_list.append(start_end_year_month)


    print('start_end_year_month_list,长度:%s,内容:%s' % (len(start_end_year_month_list), start_end_year_month_list))

    start_end_year_month_list_neartwo = near_twolist(start_end_year_month_list)

    print('start_end_year_month_list_neartwo,长度:%s,内容:%s' % (len(start_end_year_month_list_neartwo), start_end_year_month_list_neartwo))

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
    for a in visit_type:
        for b in table_type:
            print(a, ',',b)
            type_list = []
            for i in sheet1_list:
                if i[1] == a and i[2] == b:
                    type_list.append(i)
            c = avarage_month(type_list)
            print(c)
            print(type_list)
            near_month(type_list)


    # a = [['检验记录日期年份分布', '住院', '微生物', 2012.0, 9.0, 2510.0], ['检验记录日期年份分布', '住院', '微生物', 2012.0, 10.0, 2539.0],
    #      ['检验记录日期年份分布', '住院', '微生物', 2012.0, 11.0, 2668.0], ['检验记录日期年份分布', '住院', '微生物', 2012.0, 12.0, 2814.0],
    #      ['检验记录日期年份分布', '住院', '微生物', 2013.0, 1.0, 2899.0], ['检验记录日期年份分布', '住院', '微生物', 2013.0, 2.0, 2080.0],
    #      ['检验记录日期年份分布', '住院', '微生物', 2013.0, 3.0, 2617.0], ['检验记录日期年份分布', '住院', '微生物', 2013.0, 4.0, 2627.0],
    #      ['检验记录日期年份分布', '住院', '微生物', 2013.0, 5.0, 2896.0], ['检验记录日期年份分布', '住院', '微生物', 2013.0, 6.0, 2598.0],
    #      ['检验记录日期年份分布', '住院', '微生物', 2013.0, 7.0, 2783.0], ['检验记录日期年份分布', '住院', '微生物', 2013.0, 8.0, 2853.0],
    #      ['检验记录日期年份分布', '住院', '微生物', 2013.0, 9.0, 2658.0], ['检验记录日期年份分布', '住院', '微生物', 2013.0, 10.0, 2651.0],
    #      ['检验记录日期年份分布', '住院', '微生物', 2013.0, 11.0, 2632.0], ['检验记录日期年份分布', '住院', '微生物', 2013.0, 12.0, 2873.0],
    #      ['检验记录日期年份分布', '住院', '微生物', 2014.0, 1.0, 2595.0], ['检验记录日期年份分布', '住院', '微生物', 2014.0, 2.0, 2021.0],
    #      ['检验记录日期年份分布', '住院', '微生物', 2014.0, 3.0, 2571.0], ['检验记录日期年份分布', '住院', '微生物', 2014.0, 4.0, 3089.0],
    #      ['检验记录日期年份分布', '住院', '微生物', 2014.0, 5.0, 2968.0], ['检验记录日期年份分布', '住院', '微生物', 2014.0, 6.0, 3068.0],
    #      ['检验记录日期年份分布', '住院', '微生物', 2014.0, 7.0, 3304.0], ['检验记录日期年份分布', '住院', '微生物', 2014.0, 8.0, 3087.0],
    #      ['检验记录日期年份分布', '住院', '微生物', 2014.0, 9.0, 3031.0], ['检验记录日期年份分布', '住院', '微生物', 2014.0, 10.0, 3329.0],
    #      ['检验记录日期年份分布', '住院', '微生物', 2014.0, 11.0, 2958.0], ['检验记录日期年份分布', '住院', '微生物', 2014.0, 12.0, 3416.0],
    #      ['检验记录日期年份分布', '住院', '微生物', 2015.0, 1.0, 3302.0], ['检验记录日期年份分布', '住院', '微生物', 2015.0, 2.0, 2721.0],
    #      ['检验记录日期年份分布', '住院', '微生物', 2015.0, 3.0, 3245.0], ['检验记录日期年份分布', '住院', '微生物', 2015.0, 4.0, 3384.0],
    #      ['检验记录日期年份分布', '住院', '微生物', 2015.0, 5.0, 3269.0], ['检验记录日期年份分布', '住院', '微生物', 2015.0, 6.0, 3445.0],
    #      ['检验记录日期年份分布', '住院', '微生物', 2015.0, 7.0, 3891.0], ['检验记录日期年份分布', '住院', '微生物', 2015.0, 8.0, 3672.0],
    #      ['检验记录日期年份分布', '住院', '微生物', 2015.0, 9.0, 3893.0], ['检验记录日期年份分布', '住院', '微生物', 2015.0, 10.0, 3079.0],
    #      ['检验记录日期年份分布', '住院', '微生物', 2015.0, 11.0, 3604.0], ['检验记录日期年份分布', '住院', '微生物', 2015.0, 12.0, 3706.0],
    #      ['检验记录日期年份分布', '住院', '微生物', 2016.0, 1.0, 3223.0], ['检验记录日期年份分布', '住院', '微生物', 2016.0, 2.0, 2900.0],
    #      ['检验记录日期年份分布', '住院', '微生物', 2016.0, 3.0, 3378.0], ['检验记录日期年份分布', '住院', '微生物', 2016.0, 4.0, 3138.0],
    #      # ['检验记录日期年份分布', '住院', '微生物', 2016.0, 5.0, 3164.0], ['检验记录日期年份分布', '住院', '微生物', 2016.0, 6.0, 3450.0],
    #      # ['检验记录日期年份分布', '住院', '微生物', 2016.0, 7.0, 3497.0], ['检验记录日期年份分布', '住院', '微生物', 2016.0, 8.0, 3697.0],
    #      # ['检验记录日期年份分布', '住院', '微生物', 2016.0, 9.0, 3252.0], ['检验记录日期年份分布', '住院', '微生物', 2016.0, 10.0, 3045.0],
    #      # ['检验记录日期年份分布', '住院', '微生物', 2016.0, 11.0, 3346.0], ['检验记录日期年份分布', '住院', '微生物', 2016.0, 12.0, 3447.0],
    #      # ['检验记录日期年份分布', '住院', '微生物', 2017.0, 1.0, 3020.0], ['检验记录日期年份分布', '住院', '微生物', 2017.0, 2.0, 3180.0],
    #      # ['检验记录日期年份分布', '住院', '微生物', 2017.0, 3.0, 3816.0], ['检验记录日期年份分布', '住院', '微生物', 2017.0, 4.0, 3321.0],
    #      ['检验记录日期年份分布', '住院', '微生物', 2017.0, 5.0, 3619.0], ['检验记录日期年份分布', '住院', '微生物', 2017.0, 6.0, 3402.0],
    #      # ['检验记录日期年份分布', '住院', '微生物', 2017.0, 7.0, 3476.0], ['检验记录日期年份分布', '住院', '微生物', 2017.0, 8.0, 3547.0],
    #      # ['检验记录日期年份分布', '住院', '微生物', 2017.0, 9.0, 3616.0], ['检验记录日期年份分布', '住院', '微生物', 2017.0, 10.0, 3187.0],
    #      # ['检验记录日期年份分布', '住院', '微生物', 2017.0, 11.0, 3467.0], ['检验记录日期年份分布', '住院', '微生物', 2017.0, 12.0, 3186.0],
    #      ['检验记录日期年份分布', '住院', '微生物', 2018.0, 1.0, 3600.0], ['检验记录日期年份分布', '住院', '微生物', 2018.0, 2.0, 2746.0],
    #      ['检验记录日期年份分布', '住院', '微生物', 2018.0, 3.0, 3263.0], ['检验记录日期年份分布', '住院', '微生物', 2018.0, 4.0, 3317.0],
    #      # ['检验记录日期年份分布', '住院', '微生物', 2018.0, 5.0, 3458.0],
    #      ['检验记录日期年份分布', '住院', '微生物', 2018.0, 6.0, 3031.0]]
    # near_month(a)
