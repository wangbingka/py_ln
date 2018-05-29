#coding:utf-8


"""
学完基础之后，还应该针对性学习：
1、装饰器
2、迭代对象、迭代器和生成器
3、函数式变成
4、面向对象
5、多线程
6、网络编程
7、图形化编程
等等
"""


"""
课后实战-猜数字游戏规则：
1、运行程序时让用户输入名字和猜数字的范围,并根据用户输入的范围生产随机数(random)
2、最多只能有5次机会
3、没猜对，则提示最新的数字范围
4、猜对了则提示成功并推出程序
5、用户中途不愿猜了，可以输入exit或者quit退出程序
6、需要讲用户猜数字的记录写到文件保存
"""
"""
额外要求：
1、尽量不要让程序出现异常，如果出现请捕获异常，并将异常信息写入到文件
2、尽可能的封装代码，让代码变得简洁易读
"""

import random

rules = '''让我们来玩一个猜数字的游戏，游戏规则如下：
1、先依次输入两个自然数，第二数要比第一个数大差超过20，
2、我会从你给的两个数字之间任选一个数字让你来猜,
3、你有五次机会哦，猜对的话有奖。'''
# 1、运行程序时让用户输入名字和猜数字的范围,并根据用户输入的范围生产随机数(random)



def int1():
    while True:
        num1 = input('Please input a number：')
        if num1 == 'exit':
            exit()
        elif num1.isdigit() and int(num1)%1 ==0 and int(num1) >=0:

            break
        else:
            print('sorry，它不是一个自然数，请重新再输入来，退出可以输入exit或者quit')
    return int(num1)

def guess_game(num2,num3):
    count1 = 0
    global right_num
    while True and count1 < 5:
        gus_num = int1()
        count1 += 1
        if gus_num  == right_num:
            print('恭喜你呀，猜对了!')
            print(right_num)
            a = open('guess_record1.txt','r')
            printrecord(a)
            exit()
        elif gus_num < right_num:
            print('很遗憾你猜错了，稍微小了点。')
            record1('猜的第%d数字：'%count1 + str(gus_num))
        elif gus_num > right_num:
            print('So sorry，你猜的太大了。')
            record1('猜的第%d数字：'%count1 + str(gus_num))
    print('很抱歉，你可猜的次数已耗尽，请重新再来')
    b = open('guess_record1.txt', 'r')
    printrecord(b)

def record1(self):
    with open('guess_record1.txt', 'a+') as f:
        f.write(self + '\n')

def printrecord(self):
    for i in self:
        print(i)

user_name = input('请输入你的姓名:')
with open('guess_record1.txt', 'w+') as f:
    f.write('')
record1('user_name:'+str(user_name))
print(rules)

print('请输入第一个数字。')
num2 = int1()
record1('第一个较小的数字:'+str(num2))

print('请输入第二个较大的数。')
while True:
    num3 = int1()
    if num3 < num2+40:
        print('很抱歉，你输入的第二个数字太小了，请重新输入。')
    else:
        break
record1('第二个较大的数字:'+str(num3))


print('''现在我们开始游戏了。')
3秒钟后...
我已经随机从你给的两个数字之间选了一个数,
请开始输入你想要猜的数字''')
right_num = random.randint(num2, num3)
record1('我随机选中的数字：'+str(right_num))

guess_game(num2,num3)










        
# 2、最多只能有5次机会

# 3、没猜对，则提示最新的数字范围
# 4、猜对了则提示成功并推出程序
# 5、用户中途不愿猜了，可以输入exit或者quit退出程序
# 6、需要讲用户猜数字的记录写到文件保存