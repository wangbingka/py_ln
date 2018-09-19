#!usr/bin/python
#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time :  2018/9/19 15:03
# @Author: Bingka.wang
# @Email:  wangbingka@126.com


a = [1,2,3,4,5]
while a != []:
    b = a.pop()
    print('b:%s'%b)
    print('a:%s'%a)



start_end_year_month_lists = []

a = 'end%s_year_month' % start_num
key_list = []
for i in range(0, len(start_end_year_month_lists) - 1):
    print(i)
    key_list.append(start_end_year_month_lists[i][0])
print('key_list:%s' % key_list)
print(a)
if a not in key_list:
    start_end_year_month_list = []
    start_end_year_month_list.append('end%s_year_month' % start_num)
    start_end_year_month_list.append(start_end_year_month[1][3])
    start_end_year_month_list.append(start_end_year_month[1][4])
    start_end_year_month_lists.append(start_end_year_month_list)
else:
    pass