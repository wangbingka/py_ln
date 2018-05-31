#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/31 22:44
# @Author  : bingka.wang 
# @Email   : wangbingka@126.com

'''
建立一个能够不断增加学校成员的脚本
'''

# 1、创建一个学校成员类，这个类登记成员的姓名并在成员加入时自我介绍，还要统计学校的总人数。
class school_number():
    # record1函数是写入内容，用到了多次
    def pro1(self):
        global sum_num
        while True:
            self = input('''Please enter your professio:\nstudent input s \nor teacher input t \n:')
            if self in ('t','s'):
                sum_num += 1
                break
            elif self == 'exit':
                exit()
            else:
                print('sorry，输入错误，退出可以输入exit')
        return self
    def record1(self,introduce):
        with open('guess_record1.txt', 'a+') as f:
            f.write('self:'+self + ';'+'introduce:'+introduce + '\n')

# 2、创建一个老师类，这个类继承学校成员类，创建对象的时候总人数加一，老师类重写具体打招呼的类容
class teacher_num(school_number):
    professio2 = '教师'
    say_hello = '大家好，我是一名教师。'

# 3、创建一个学生类，这个继承学校成员类，创建对象时总人数也会加一，学生类重写打招呼的类容，增加一个方法介绍自己的学习情况。
class student_num(school_number):
    professio3 = '学生'
    say_hello = '大家好，我是一名学生。'
    def record1(self,introduce):
        with open('guess_record1.txt', 'a+') as f:
            f.write('self:'+self + ';'+'introduce:'+introduce + '\n')

sum_num = 0


type1 = pro1()
print(sum_num)
#
# 4、实例对象结束的时候，总人数减一

