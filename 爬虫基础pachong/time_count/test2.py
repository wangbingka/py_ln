#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time :  2018/9/26 14:55
# @Author: Bingka.wang
# @Email:  wangbingka@126.com


#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time :  2018/9/25 16:33
# @Author: Bingka.wang
# @Email:  wangbingka@126.com

import os
from operator import itemgetter, attrgetter
import re
import shutil
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


# '''
# 1、算出所有月份的平均值
# 2、判断当前月份对应的值是否是大于平均值的五分之一，并小于平均值的五倍，如果是则记录，如果不是则正常并且新的纪录
# 3、每两个组成一个组合进行对比，前一个要保证大于后一个的2分之一并小于前一个的3倍，否则删除进行下一个操作，直到有满足条件的，一直往下取，形成新的列表
# 4、排列顺序，取出最大的月份，和最小的月份，并且判断最小的月份和后一个月份是连续的，如果不是则继续
# '''

def write_data(self,filename):
    with open('%s.txt'%(filename),'a+') as f:
        f.write(self)


class dataCount(object):
    global filepath,typecontent_list,datelist,typelist,typecontent_list,cluster
    def __init__(self,apath):
        self.apath = apath

    def int_list(self):
        int_list_str = []
        for i in self:
            if i == 'NULL':
                a = 0
                int_list_str.append(a)
            elif isinstance(i, int) or isinstance(i, float) or i.isdigit():
                a = int(i)
                int_list_str.append(a)
            else:
                int_list_str.append(i)
        # print(int_list_str)
        return int_list_str


    def near_twolist(self):
        list1 = []
        for i in range(0,len(self)-1):
                list5 = []
                list5.append(self[i])
                list5.append(self[i+1])
                list1.append(list5)
        return list1

    def datelist(self):
        with open('%s' % self, 'r+') as f:
            sheet1_list = []
            for line in f:
                conts = line.split('\t')
                conts1 = []
                for i in conts:
                    b = i.replace('\n', '')
                    conts1.append(b)
                conts2 = int_list(conts1)
                if isinstance(conts2[-1], int):
                    sheet1_list.append(conts2)
                else:
                    pass
        return sheet1_list

    def typelist(self):
        type_list = []
        for i in self:
            visit_type = []
            visit_type.append(i[1])
            visit_type.append(i[2])
            visit_type.append(i[0])
            if visit_type not in type_list:
                type_list.append(visit_type)
        return type_list



    def search_value(self):
        num = 1
        value_list = []
        for i in typecontent_list:
            if self[0] == i[3] and self[1] == i[4]:
                value_list.append(self[0])
                value_list.append(self[1])
                value_list.append(i[5])
                return value_list
            elif num < len(typecontent_list):
                num += 1
                continue
            else:
                value_list.append(self[0])
                value_list.append(self[1])
                value_list.append(0)
                return value_list
    def all_count(self):
        write_data_list = []
        sheet1_list = datelist(apath)
        while not os.path.exists('%s\\move_result' % filepath):
            os.makedirs('%s\\move_result' % filepath)
        shutil.move(apath, '%s\\move_result' % filepath)

        type_list = (typelist(sheet1_list))

        for i in type_list:
            typecontent_list = []
            type_null_value = 0
            for a in self.sheet1_list:
                if i[0] == a[1] and i[1] == a[2]:
                    typecontent_list.append(a)
                    try:
                        if a[3] == 0 or a[4] == 0:
                            type_null_value = a[-1]
                        else:
                            pass
                    except:
                        type_null_value = 0
            c1 = avarage_month(typecontent_list)
            near_month_list1 = near_month(c1[2])
            wrong_month_list1 = wrong_month(near_month_list1)
            write_data_content = '{}\t{}\t{}\t{}\t{}\t{}\t{}年{}月\t{}年{}月\t{}\t'.format(i[2], i[0], i[1], c1[0],
                                                                                       type_null_value, c1[1],
                                                                                       near_month_list1[0][1][
                                                                                           0],
                                                                                       near_month_list1[0][1][
                                                                                           1],
                                                                                       near_month_list1[-1][1][
                                                                                           0],
                                                                                       near_month_list1[-1][1][
                                                                                           1], len(wrong_month_list1))
            if len(wrong_month_list1) > 0:
                # print('数据不正常的月份数量：{},具体月份以及对应的数据量:{}'.format(len(wrong_month_list1), 0,
                #                                                          wrong_month_list1))
                for d in wrong_month_list1:
                    write_data_content += '{}年{}月\t{}\t'.format(d[0], d[1], d[2])
            else:
                pass
            write_data_content += '\n'
            if write_data_content not in write_data_list:
                write_data_list.append(write_data_content)
                write_data(write_data_content, '%s\\%s_type_count' % (filepath, cluster))
            else:
                pass
            typecontent_list1 = table_count(sheet1_list)
            tableconent_list = []
            table_null_value = 0
            for b in typecontent_list1:
                if i[2] == b[0]:
                    tableconent_list.append(b)
                    try:
                        if a[3] == 0 or a[4] == 0:
                            table_null_value = a[-1]
                        else:
                            pass
                    except:
                        table_null_value = 0
            c2 = avarage_month(tableconent_list)
            near_month_list2 = near_month(c2[2])
            wrong_month_list2 = wrong_month(near_month_list2)
            write_data_content = '{}\t{}\t{}\t{}\t{}年{}月\t{}年{}月\t{}\n'.format(i[2], c2[0], table_null_value, c2[1],
                                                                               near_month_list2[0][1][0],
                                                                               near_month_list2[0][1][1],
                                                                               near_month_list2[-1][1][0],
                                                                               near_month_list2[-1][1][1],
                                                                               len(wrong_month_list2))
            if len(wrong_month_list1) > 0:
                for d in wrong_month_list2:
                    write_data_content += '{}年{}月\t{}\t'.format(d[0], d[1], d[2])
            else:
                pass
            write_data_content += '\n'
            if write_data_content not in write_data_list:
                write_data_list.append(write_data_content)
                write_data(write_data_content, '%s\\%s_table_count' % (filepath, cluster))
            else:
                pass
        print write_data_list
        return write_data_list

    def avarage_month(self):
        counts = []
        result_list = []
        for i in self:
            counts.append(i[-1])
        sum = 0
        for a in counts:
            sum += a
        avarage = sum / len(counts)

        normal_list = []
        for i in self:
            if i[-1] < avarage * 5 and i[-1] > avarage / 5 and i[3] in range(1990, 2019) and i[4] in range(0, 13):
                normal_list.append(i)
            else:
                pass

        result_list.append(sum)
        result_list.append(avarage)
        result_list.append(normal_list)
        return result_list



    def near_month(self):

        list2 = list(reversed(near_twolist(self)))

        # 相邻月份，相互差距应小于3倍
        common_month = []
        while list2 != []:
            now_list = list2.pop()
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
            if num==0:
                current_list = []
                current_list.append(start_end_year_month[0][3])
                current_list.append(start_end_year_month[0][4])
                # start_year_month['start%s_year_month'%start_num] = '%s_%s'%(start_end_year_month[0][3],start_end_year_month[0][4])
                start_year_month['start%s_year_month' % start_num] = current_list
                current_list = []
                current_list.append(start_end_year_month[1][3])
                current_list.append(start_end_year_month[1][4])
                start_year_month['end%s_year_month' % start_num] = current_list

            elif (start_end_year_month[0][3] == start_end_year_month[1][3] and start_end_year_month[0][4]+1 == start_end_year_month[1][4]) or (start_end_year_month[0][3]+1 == start_end_year_month[1][3] and start_end_year_month[0][4]-11 == start_end_year_month[1][4]):
                # start_year_month['end%s_year_month'%start_num] = '%s_%s' % (start_end_year_month[1][3],start_end_year_month[1][4])
                current_list = []
                current_list.append(start_end_year_month[1][3])
                current_list.append(start_end_year_month[1][4])
                start_year_month['end%s_year_month' % start_num] = current_list

            else:
                start_num +=1
                current_list = []
                current_list.append(start_end_year_month[1][3])
                current_list.append(start_end_year_month[1][4])
                start_year_month['start%s_year_month' % start_num] = current_list
                start_year_month['end%s_year_month' % start_num] = current_list
            num +=1

        # 标记出各个正常数据量的起始月份阶段
        start_end_year_month_list = []
        for a in start_year_month.keys():
            start_end_year_month = []
            start_end_year_month.append(a)
            start_end_year_month.append(start_year_month[a])
            start_end_year_month_list.append(start_end_year_month)

        start_end_year_month_list1 = near_twolist(start_end_year_month_list)
        start_end_year_month_list_twonear_list = []
        for i in range(0,int(len(start_end_year_month_list)/2)):
            start_end_year_month_list_twonear = []
            start_end_year_month_list_twonear.append(start_end_year_month_list[2*i])
            start_end_year_month_list_twonear.append(start_end_year_month_list[2*i+1])
            start_end_year_month_list_twonear_list.append(start_end_year_month_list_twonear)
        # print('start_end_year_month_list:长度：%s，值：%s' % (len(start_end_year_month_list),start_end_year_month_list))
        # print('start_end_year_month_list_twonear_list:长度：%s，值：%s' % (len(start_end_year_month_list_twonear_list), start_end_year_month_list_twonear_list))

        countnum = 0
        while True and countnum < 10:
            if start_end_year_month_list_twonear_list[0][0][1] != start_end_year_month_list_twonear_list[0][1][1] and \
                    start_end_year_month_list_twonear_list[-1][0][1] == start_end_year_month_list_twonear_list[-1][0][1]:
                break
            elif start_end_year_month_list_twonear_list[0][0][1] == start_end_year_month_list_twonear_list[0][1][1]:
                del i[0]
            elif start_end_year_month_list_twonear_list[-1][0][1] == start_end_year_month_list_twonear_list[-1][0][1]:
                del i[-1]
            countnum +=1

        start_end_year_month_list = []
        for i in start_end_year_month_list_twonear_list:
            for a in i:
                start_end_year_month_list.append(a)
        # print('start_end_year_month_list:长度:%s,值：%s.'%(len(start_end_year_month_list),start_end_year_month_list))
        return start_end_year_month_list

    def wrong_month(self):

        wrong_month_list = []
        start_end_year_month_list_neartwo = near_twolist(self)
        for i in start_end_year_month_list_neartwo:
            a1 = i[0][1][0]
            a2 = i[1][1][0]
            b1 = i[0][1][1]
            b2 = i[1][1][1]

            if i[0][0].startswith('end') and a1 == a2:
                for b in range(b1+1,b2):
                    year_month_list = []
                    year_month_list.append(a1)
                    year_month_list.append(b)
                    b += 1
                    year_month_list1 = search_value(year_month_list)
                    wrong_month_list.append(year_month_list1)
            elif i[0][0].startswith('end') and a1 != a2:
                for a in range(a1,a2+1):

                    # 2.1
                    if a == a1:
                        for b in range(b1+1,13):
                            year_month_list = []
                            year_month_list.append(a)
                            year_month_list.append(b)
                            year_month_list1 = search_value(year_month_list)
                            wrong_month_list.append(year_month_list1)
                            b += 1
                    elif a >a1 and a <a2:
                        for b in range(1,13):
                            year_month_list = []
                            year_month_list.append(a)
                            year_month_list.append(b)
                            year_month_list1 = search_value(year_month_list)
                            wrong_month_list.append(year_month_list1)
                            b += 1
                    else:
                        for b in range(1,b2):
                            year_month_list = []
                            year_month_list.append(a2)
                            year_month_list.append(b)
                            year_month_list1 = search_value(year_month_list)
                            wrong_month_list.append(year_month_list1)
                            b += 1
            else:
                pass

        return wrong_month_list




    def table_count(self):
        # 将来自同一张表的数据按照年月进行统计，并排序
        type_time_list = []
        for i in self:
            type_time_content = []
            type_time_content.append(i[0])
            type_time_content.append(i[3])
            type_time_content.append(i[4])
            if type_time_content not in type_time_list:
                type_time_list.append(type_time_content)

        table_count_list = []
        for i in type_time_list:
            table_count_content = []
            table_count_value = 0
            for a in self:
                if i[0] == a[0] and i[1] == a[3] and i[2] == a[4]:
                    table_count_value += a[5]
                else:
                    pass
            table_count_content.append(str(i[0]))
            table_count_content.append('所有就诊类型')
            table_count_content.append('所有项目类型')
            table_count_content.append(int(i[1]))
            table_count_content.append(int(i[2]))
            table_count_content.append(table_count_value)
            table_count_list.append(table_count_content)


        # 列表排序
        table_count_list.sort(key=itemgetter(0,3,4))
        return table_count_list

if __name__ == '__main__':
    filepath = os.getcwd()
    filepath = '%s\\result' % filepath
    print filepath
    for x in os.listdir(filepath):
        if x.endswith('.txt') and 'date' in x:
            print(x)
            apath = apath = os.path.join(filepath,x)
            cluster = re.split('[._]', apath)[-5]
            print('cluster:%s' % cluster)
            print('apath:%s' % apath)

            write_data(
                '表类型\t就诊类型\t项目类型\t数据总量\t日期null的数据量\t每个月平均值\t开始时间\t结束时间\t开始结束之间异常月份的数量\t不正常的月份\t值\t不正常的月份\t值\t不正常的月份\t值\n',
                '%s\\%s_type_count'  % (filepath,cluster))
            write_data('表类型\t数据总量\t日期null的数据量\t每个月平均值\t开始时间\t结束时间\t开始结束之间异常月份的数量\t不正常的月份\t值\t不正常的月份\t值\n',
                       '%s\\%s_table_count' % (filepath,cluster))

            a = dataCount(apath)
            a.all_count()

