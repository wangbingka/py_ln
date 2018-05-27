#coding:utf-8
#author:bingka.wang

"""
写一个函数，该函数能判断传入的参数是否是一个完数，如果是完数则返回True，否则返回False
提示：完数就是一个数等于他的因子之和，如6=1+2+3,那么这个数就是完数.
"""
#1、写一个函数，要求必须是整数数字，如果是非纯数字则报错

num1 = input('Please input a number：')
# num1 = 10001


# 如果是整数字符继续运行，如果非整数则退出，
# 目前还未能让其自动循环再次输入
if num1.isdigit() and int(num1)%1 ==0:
	pass
else:
	print('sorry，它不是一个整数，请重新再来')
	exit()

num11 = int(num1)

#2、找这个数的因子
#百度了之后没找到我能看到的不需要其他库的找所有因子的方法
#想到了一个笨方法，用质数来求，一个数的最大因子是a/2，其次是a/3，/4、....，最大可以是a/2，判断余数是否为0

	# list1 = []
	# sum_list1 = 0
	# for n in range(1,num1//2+1):
	# 	 if num1%n ==0:
	# 	 	list1.append(n)
	# 	 	sum_list1 +=num1
	# 	 n +=1
	# print(list1)
	# print(sum_list1)

list1 =[]
sum_list1 = 0
def dataw(num1):
	global list1 
	global sum_list1 
	for n in range(1,num11//2+1):
		if num11%n ==0:
			list1.append(n)
			sum_list1 +=(int(n))
		n +=1
	return sum_list1



# #3、判断这个数与因子之和的关系
# #4、返回结果


sum_list2 = dataw(num1)
if num11 == sum_list2:
	print('True')
	print('恭喜，你输入的是完数')
else:
	print('False')
	print('Sorry，这不是完数')

# print(list1)
# print(sum_list1)
