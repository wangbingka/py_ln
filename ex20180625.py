#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/25 23:02
# @Author  : bingka.wang 
# @Email   : wangbingka@126.com

#计算1-2+3-4....+99-100的值

# start1 = 0
# count_num = 0
# while True:
#     if start1 ==101:
#         break
#     if start1%2 == 0:
#         count_num -=start1
#     if start1%2 != 0:
#         count_num +=start1
#     start1 +=1
# print(count_num)


#先设定用户名和密码
#用户名输错则重新输入
#密码输错则重新开始输入账号和密码
#同一账号密码输错三次则此账号不允许再次输入提示已锁定。
    # us1_psd = {'abc':'a123','bcd':'a234','cde':'a235'}
    #
    # count_us1=1
    # count_psd = 1
    # while True:
    #     if count_us1 == 6:
    #         print('账号输入错误次数已达到5次限制，请24小时后再次尝试')
    #         exit()
    #     input_username=input('请输入您的账号名称:')
    #     while us1_psd.__contains__(input_username):
    #         input_password=input('请输入您的密码:')
    #         if count_psd ==6:
    #             print('此账号密码错误方式达到五次，此账号已被锁定24小时。')
    #             exit()
    #         if input_password == us1_psd.get(input_username,None):
    #             print('登录成功')
    #             exit()
    #         else:
    #             count_psd +=1
    #             print('密码错误，请重新输入')
    #             continue
    #     print('账号输入错误，请重新出入')
    #     count_us1 +=1



