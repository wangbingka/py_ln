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
# 1、运行程序时让用户输入名字和猜数字的范围,并根据用户输入的范围生产随机数(random)
user_name = input('请输入你的姓名')
num1 = input('请出入较小的那个数字')
num2 = input('请输入较大的那个数字')
right_num = random.randint(int(num1),int(num2))
num3 = input('请输入你认为正确的数字')



# 2、最多只能有5次机会

# 3、没猜对，则提示最新的数字范围
# 4、猜对了则提示成功并推出程序
# 5、用户中途不愿猜了，可以输入exit或者quit退出程序
# 6、需要讲用户猜数字的记录写到文件保存
