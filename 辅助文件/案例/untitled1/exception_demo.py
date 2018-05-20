# coding: utf-8
# author: yopoing
"""
ZeroDivisionError除(或取模)零 (所有数据类型)
AttributeError对象没有这个属性
FileNotFoundError
找不到文件
ImportError导入模块/对象失败
IndexError序列中没有此索引(index)
KeyError
映射中没有这个键
NameError未声明/初始化对象 (没有属性)
SyntaxError Python 语法错误
IndentationError缩进错误
TypeError对类型无效的操作
ValueError
传入无效的参数

"""
# ZeroDivisionError
# a = 9//0
# FileNotFoundError
# open('sss.txt', 'r')
# ImportError
# import dddddss
# IndexError
# a = [1,2]
# a[2]
# KeyError
# a={'a':1}
# a['b']
# NameError
# print(aaa)
# AttributeError
# a='fsdfd'
# a.ddssda()
# SyntaxError
# 8ad = 'ddd'
# IndentationError
# print('fff')
# TypeError
# a=10
# a[0]
# ValueError
# int('fff')
"""
try:
<语句>        #运行别的代码
except <异常名>：
<语句>        #如果在try部份引发了'name'异常
except <异常名>，<数据>:
<语句>        #如果引发了'name'异常，获得附加的数据
else:
<语句>        #如果没有异常发生
finally: #始终会被执行到的代码
<语句>

以上为完整结构，使用的时候至少要有一个try和except代码块。

"""
# try:
#     # int('dfsfd')
#     print(aaa)
# except ValueError as e:
#     print('处理了异常:', e)
# except NameError as e:
#     print('处理了异常:', e)
# except:
#     print('处理了异常')
# else:
#     print('没有异常发生才能执行到')
# finally:
#     print('不管有没有异常始终都能执行到')

# raise TypeError

class MyException(Exception):
    pass

[['a',1],['a',2],['b',1],['b',2],...]
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3, 5]
new_list = []
try:
    for m in list1:
        for n in list2:
            if n == 3:
                raise MyException
                # break
                # continue
                # exit()
            new_list.append([m, n])
except MyException:
    pass
print(new_list)
