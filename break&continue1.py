#coding:utf-8
#
"""
break和continue案例分析
1、遍历字符串，当值为x的时候使用break\continue\exit控制程序
2、使用嵌套循环将两个列表的值取出生成一个新的列表，
新的列表包含原列表的所有组合
"""
#break跳出整个循环，跳出后之后循环的内容不再执行
mystr = 'maizixueyuan666'
	# for v in mystr:
	# 	if v == 'x':
	# 		break
	# 	print(v)
	# print('循环顺利执行结束')
#continue跳出当前循环，跳出后下一次循环继续执行
		# for v in mystr:
		# 	if v == 'x':
		# 		continue
		# 	print(v)
		# print('循环顺利执行结束')
#exit()退出程序，循环体之外的所有代码也不会执行
	# for v in mystr:
	# 	if v == 'x':
	# 		exit()
	# 	print(v)
	# print('循环顺利执行结束')

#得到一个新的列表，包含两个列表所有的值所有两两组合的列表
list1 = ['a','b','c']
list2 = [1,2,3,5]
new_list = []
for m in list1:
	for n in list2:
		new_list.append([m,n])
print(new_list)
