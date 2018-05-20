# coding: utf-8
# author: yopoing
"""
def 函数名(参数1,参数2,...):
     函数代码
     return 返回值

1、学会自定义函数
2、参数、参数默认值和可变参数
3、学会调用函数
4、学会return语句的使用
5、了解匿名函数
6、课后扩展：学习常用的内置函数

"""

"""
可变参数：
*args:接收普通参数，以元组形式进行保存
**kwargs：接收关键字参数，以字典的形式进行保存
"""


# def myfunc(name='胡明星', age=18, *args, **kwargs):
#     print("这是我的第一个函数。")
#     print("我是%s,今年%d岁" % (name, age))
#     print(args)
#     print(kwargs)
#     return 'hello'
#
# result = myfunc("张三", 20, 12, 30, 90, 'abc', sex='男', cc='pp')
# print('result:',result)

# def myfunc():
#     [['a',1],['a',2],['b',1],['b',2],...]
#     list1 = ['a', 'b', 'c']
#     list2 = [1, 2, 3, 5]
#     new_list = []
#     for m in list1:
#         for n in list2:
#             if n == 3:
#                 return new_list
#                 # break
#                 # continue
#                 # exit()
#             new_list.append([m, n])
#     # return new_list
#
# mylist = myfunc()
# print(mylist)


"""
改成从某一个区间的数字求奇数和
"""
# def myfunc(start, end):
#     # 求和值
#     sum = 0
#     while start <= end:
#         if start%2 != 0:
#             sum += start
#         start += 1
#     return sum

# print(type(myfunc))

# 匿名函数(lambda)
# myfunc = lambda :print('我是胡明星')
# myfunc()