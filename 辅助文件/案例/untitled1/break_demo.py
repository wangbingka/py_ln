# coding: utf-8
# author: yopoing

"""
break和continue案例分析
1、遍历字符串，当值为x的时候使用break\continue\exit控制程序
2、使用嵌套循环将两个列表的值取出生成一个新的列表，新的列表包含原列表
的所有组合
"""
"""
break 跳出整个循环，跳出之后循环体后面的内容也不执行,如果在嵌套循环中使用break，会跳出内层的循环
continue 跳出当前（本次）的循环，但是会继续执行下一次循环
exit 退出程序
"""
# mystr = 'maizixueyuan666'
# for v in mystr:
#     if v == 'x':
#         # break
#         # continue
#         exit()
#     print(v)
# print('循环顺利执行结束')

[['a',1],['a',2],['b',1],['b',2],...]
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3, 5]
new_list = []
for m in list1:
    for n in list2:
        if n == 3:
            break
            # continue
            # exit()
        new_list.append([m, n])
print(new_list)

