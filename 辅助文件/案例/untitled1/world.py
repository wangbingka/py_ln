# coding: utf-8
# author: yopoing
# from mypack import test2
# print(test2.test1)

# mystr = 'maizixueyuan666'
# for v in mystr:
#     if v == 'x':
#         break
#         # continue
#         # exit()
#     print(v)
# print('执行完了')
#
# def ttt():
#     list1 = ['a', 'b', 'c']
#     list2 = [1, 2, 3, 5]
#     new_list = []
#     for m in list1:
#         for n in list2:
#             # 排除值为3的组合
#             if n == 3:
#                 return new_list
#             new_list.append([m, n])
#
# print(ttt())

# while True:
#     mystr = input('请输入你想输入的信息：')
#     if mystr in ['exit', 'quit']:
#         with open('record.txt', 'r', encoding='utf-8') as f:
#             for v in f:
#                 print(v, end='')
#         break
#     with open('record.txt', 'a+', encoding='utf-8') as f:
#         f.write(mystr+'\n')
# a=10
# a[0]
# a='fff'
# a.haha()
#  print('fff')
# a=[1,2]
# a[3]
# a={'a':1}
# a['b']
# open('r.txt', 'r')
# import ffff
# try:
#     # int('aaa')
#     # a=9/0
#     print('aaa')
# except ValueError as e:
#     print('发生ValueError：', e)
# except ZeroDivisionError as e:
#     print('发生ZeroDivisionError：', e)
# except NameError as e:
#     print('发生NameError：', e)
# else:
#     print('我是没有异常发生的时候会执行到的代码哦')
# finally:
#     print('我是无论如何都会执行到的代码哦')

# class MyException(Exception):
#     pass

# [['a',1],['a',2],['b',1],['b',2],...]
# list1 = ['a', 'b', 'c']
# list2 = [1, 2, 3, 5]
# new_list = []
# try:
#     for m in list1:
#         for n in list2:
#             if n == 3:
#                 raise MyException
#                 # break
#                 # continue
#                 # exit()
#             new_list.append([m, n])
# except MyException as e:
#     pass
# print(new_list)

