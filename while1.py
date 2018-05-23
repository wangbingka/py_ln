# coding:utf-8

"""
while条件表达式：
	满足条件执行的代码
else:
	不满足条件退出循环的时候执行的语句
"""

mystr = 'maizixueyuan666'
#起始位置
i = 0
while i<len(mystr):
	print(mystr[i])
	i +=1
else:
	print('循环顺利执行并结束。')
#一定要避免死循环
# while 1==1:
# 	print('ok')
# 1、学习while语句
# 2、学习for语句
	# for i in mystr:
	# 	print('ok')
#获取值和下标
	# for (i,v) in enumerate(mystr):
	# 	print(i,v)
	# 	if i ==5:
	# 		break
# 3、完成一个实战练习

"""
使用while和for分别完成从1累加到100求奇数和的例子
"""
#初始值num，求和值sum

	# num =1 #while
	# sum =0
	# while num <=100:
	# 	if num%2 !=0:
	# 		sum +=num
	# 	num +=1
	# print(sum)

sum =0 #for
for num in range(1,101):
	if num%2 !=0:
		sum +=num
print(sum)
#continue跳过，break结束苏
i =1
while i <=10:
	i +=1
	if i%2 >0:
		continue
	print(i)
i =1
while 1==1:
	print(i)
	i +=1
	if i >10:
		break
