# coding: utf-8
# author: yopoing
"""
本节内容：
1、掌握文件处理的流程及对应代码
2、保存中文乱码问题的处理
3、使用with..as语句简化文件操作流程的代码
4、掌握操作文件打开常用的模式
5、完成一个文件读写的实战
"""
"""
1、打开文件
2、阅读\写入
3、关闭
"""
# # 1、打开文件
# f = open('record.txt', 'r+', encoding='utf-8')
# # 2、写入\阅读
# # f.write('hello,胡明星')
# print(f.readline())
# # 3、关闭
# f.close()
"""
使用with..as语句的时候可以不用关闭文件
"""
# with open('record.txt', 'r+', encoding='utf-8') as f:
#     print(f.readline())
"""
接收用户的输入，并将用户输入的内容以追加的方式写入到文件，直到用户输
入exit或者quit则退出程序，退出的时候显示文件中所有记录的内容。
1、一直接收用户输入，输入exit或者quit则退出程序
while True：
    。。。
2、追加的方式
a a+
3、退出的时候要显示记录的内容
break\exit
"""
while True:
    mystr = input('请输入信息：')
    if mystr in ['exit', 'quit']:
        with open('record.txt', 'r', encoding='utf-8') as f:
            for v in f:
                print(v, end='')
        break
    with open('record.txt', 'a+', encoding='utf-8') as f:
        f.write(mystr+'\n')
