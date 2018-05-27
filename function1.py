#coding:utf-8
#author:bingka.wang
#1、学会自定义函数
"""
def 函数名(参数1，参数2,...):
	函数代码
	return 返回值
"""
	# def myfunc(name):
	# 	print('这是我的第一个函数')
	# 	print('我是%s'%name)
	# 	#return 返回值
		
	# myfunc('王兵卡')

#设置默认参数，但可以更改
	# def myfunc(name='王兵卡',age=18):
	# 	print('这是我的第一个函数')
	# 	print('我是%s,今年%d岁。'%(name,age))
	# 	#return 返回值
		
	# myfunc()
	# myfunc('力王')
	# myfunc('力王',19)

#不确定自己多少个参数，可以用可变参数
	# def myfunc(name='王兵卡',age=18,*args):
	# 	print('这是我的第一个函数')
	# 	print('我是%s,今年%d岁。'%(name,age))
	# 	print(args)
	# 	#return 返回值
		
	# myfunc()
	# myfunc('力王')
	# myfunc('力王',19)
	# myfunc('力王',19,30,102,'abc')

#不确定自己多少个参数，可以用可变参数*args,另一个中可变参数**kwargs，是需要有关键字参数
# '*args'返回元组的数据类型，'**kwargs'返回字典的数据类型

	# def myfunc(name='王兵卡',age=18,*args,**kwargs):
	# 	print('这是我的第一个函数')
	# 	print('我是%s,今年%d岁。'%(name,age))
	# 	print(args)
	# 	print(kwargs)

		
	# myfunc('力王',19,30,102,'abc',sex='男')



#2、参数、参数默认值和可变参数
#3、学会调用函数
#4、学会return语句的使用


"""
return,当没有return，默认返回空对象none,如果定义return，可以在后面使用,
并且return后面的语句不会再被执行
return函数也可以用于跳出整个循环，但return只能用于函数内
"""
	# def myfunc(name='王兵卡',age=18,*args,**kwargs):
	# 	print('这是我的第一个函数')
	# 	print('我是%s,今年%d岁。'%(name,age))
	# 	print(args)
	# 	print(kwargs)
	# 	#return 返回值
	# 	return 'succed'
	# 	print('hahahaha1')
		

	# result1 = myfunc('力王',19,30,102,'abc',sex='男',cc='pp')
	# print('result1',result1)

"""
实战案例：
1、把之前做的从1累加到100求计数和的例子改成函数的方法进行调用。
2、使用return跳出整个嵌套循环
"""
#1、关于for函数，转换为自定义函数
sum1 = 0
for i in range(0,101):
	if i%2 != 0:
		sum1 +=i
print(sum1)

def sum_ca(start,end):
	sum2 = 0
	for i in range(start,end+1):
		if i%2 != 0:
			sum2 +=i
	return sum2
print(sum_ca(2,98))


#2、关于while循环，转化为自定义函数
	# num1 =1
	# sum2 =0
	# while num1 <= 100:
	# 	if num1%2 !=0:
	# 		sum2 +=num1
	# 	num1 +=1
	# print(sum2)

def sum_ca1(start,end):
	sum3 =0
	while start <= end:
		if start%2 !=0:
			sum3 +=start
		start +=1
	return sum3
print(sum_ca1(1,100))
print(sum_ca1(2,98))
print(type(sum_ca1))

#5、了解匿名函数(lambda)，意义为了简化冗余代码，也有替代方法
(lambda :print('我是胡明星'))()

myfunc2 = lambda :print('我是胡明星')
myfunc2()


#6、课后扩展，学习常用的内置函数
