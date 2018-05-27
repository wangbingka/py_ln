#coding:utf-8
#author:bingka.wang

""""
#异常
1、什么是异常？遇到异常怎么办？
2、掌握常见的异常类型
    BaseException,所有异常基类
    KeyboardInterrupt，用户终端异常，ctrl+c
    Exception，常见错误的基类
3、如何捕获异常
4、使用raise手动出发异常
5、使用自定义异常解决跳出整个嵌套循环的问题
"""

#一、常见错误异常
# ZeroDivisonError,除0变量，被除数为0
    #     # a = 9/0 ，或者9//0
# syntaxError,语法错误
# NameError,命名错误，使用了没有被定义的参数
    # print(aa)
# ZeroDivisonError
    #a = 9/0 ，或者9//0
#FileNotFoundError，找不到文件异常
    #open('1.txt','r')，必须先创建才能读取
#ImportError，模块异常，导入了不存在的模块
    # import DDDDDSSD
#IndexError,序列中没有此所以(index)
    # a = [1,2]
    # a[2]
#KeyError，键值异常，字典中没有在这个键
    # a = {'a':1}
    # a['b']
#AttributeError，属性错误，比如一个字符串使用不存在的函数
    # a = 1
    # a.dddsssd()
#SyntaxErrorPython 语法错误，比如说变量名以数字开头
    # 8sad = 'ddd'
#IndentationError 缩进错误
#TypeError 对类型无效的操作
    # a = 10
    # a[0]
#ValueError 传入无效的参数
    # int('fff')


"""
如何捕获异常
以下为完整结果，使用时起码要有try和except模块
try:
<语句>      #运行代码
except<异常名>:
<语句>      #如果在try部分引发了'name'异常
except<异常名>,<数据>:
<语句>      #如果引发了'name'异常,获取附加的数据
else：#    如果没有异常发生
语句>      #如果没有异常发生
finally:   #不管有没有异常，始终会被执行到的代码
<语句>
"""
    # try:
    #     int('fff')
    #     print(aaa)
    # except ValueError as e:
    #     print('处理了异常',e)
    # except:
    #     print('处理了其他额外的异常')

#使用raise手动出发异常
    # raise ValueError

#使用自定义异常解决跳出整个嵌套循环的问题
class MyException(Exception):
    pass

list1 = ['a','b','c']
list2 = [1,2,3,5]
new_list = []
try:
    for m in list1:
        for n in list2:
            if n ==3:
                raise MyException
                # continue
                # break
                # print(new_list)
                # exit()

            new_list.append([m,n])
except MyException:
    pass
print(new_list)