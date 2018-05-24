# coding:utf-8
#author:bingka.wang


"""
随便输入一个字符串，可以判断这个字符串的组成，
包括有多少个数字，多少个字母，
以及多少个空格，还有多少个特殊符号。
"""


#1、接受输入一个字符串
# a = 'sfdfghtrfsdf!@#$ @@134 fdh'
a = input('请任意输入一个字符串，我可以帮你判断它的组成:')
#2、对字符串拆分，并判断每个字符串的类型，计算数据量，
def count_strtype(str1):
	str_sum = 0
	flock_sum = 0
	other_sum = 0
	num_sum = 0

	for i in str1:
		if i.isalpha() :
			str_sum +=1
		elif i.isspace() :
			flock_sum +=1
		elif i.isdigit() :
			num_sum +=1
		else:
			other_sum +=1
	#3、输出结果
	print('你输入的字符里面有%s个字母，%s个数字，%s个空格，%s个其他字符。'%(str_sum,num_sum,flock_sum,other_sum))


count_strtype(a)