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
		if n ==3:
			# continue
			 break
			# print(new_list)
			# exit()

		new_list.append([m,n])

print(new_list)


#怎么从内层，直接跳出三层循环
#1、定义变量，更改变量状态，不满足条件，循环跳出
break_flag=False
for i in range(10):
    print("爷爷层")
    for j in range(10):
        print("爸爸层")
        for k in range(10):
            print("孙子层")
            if k==3:
                break_flag=True
                break                    #跳出孙子层循环，继续向下运行
        if break_flag==True:
            break                        #满足条件，运行break跳出爸爸层循环，向下运行
    if break_flag==True:
        break                            #满足条件，运行break跳出爷爷层循环，结束全部循环，向下运行

print("keep going...")

#2、while循环语句，定义条件，条件改变，循环结束
break_flag=False
count=0
while break_flag==False:
    print("爷爷层...")
    while break_flag==False:
        print("爸爸层...")
        while break_flag==False:
            if count<5:
                print("孙子层...")
                count+=1
            else:
                break_flag=True
print("keep going...") 
#3、在Python中，函数运行到return这一句就会停止，因此可以利用这一特性，将功能写成函数，终止多重循环
def work():                                  #定义函数

    for i in range(5):

        print("i=", i)

 

        for j in range(5):

            print("--j=", j)

 

            for k in range(5):

 

                if k<2:

                    print("------>k=", k)

                else:

                    return i,j,k              

print (work())
