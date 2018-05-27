#coding:utf-8
#anthor:bingka.wang

"""
1、打开文件
2、阅读/写入
3、关闭文件
"""
"""
各种读写模式
w:覆盖模式，仅写
a:以追加的方式打开，仅写
r+:以读写模式打开，不断追加，若文件不存在，报错
w+：以读写模式打开，覆盖性，若文件不存在，创建,但不能直接读出，但是编辑中的文件，内容无法被读出，必须先关闭再打开一行一次保存操作
a+：以读写模式打开，覆盖性，附加方式打开,但不能直接读出，但是编辑中的文件，下一次读取只会显示本次追加内容
"""

#1、创建文件
f = open('record1.txt','r+')
#2、写入，write：写入，writeline:写入一行
f.write('hello,卡卡王')
#3、读取内容,read：读取，readline:读取一行
print(f.readline())
#3、关闭文件
f.close

#代码简化
"""
使用with ..as ..语句，不用关闭文件，默认自动关闭
"""
with open('record1.txt','r+') as f:
	print(f.readline())

"""
接受用户的输入，并将用户输入的内容以追加的方式写入到文件，
直到用户输入exit或者quit则退出程序，退出的时候显示文件中所有记录的内容
"""

# 1、一直接受用户的输入
while True:
	mystr1 = input('请输入信息:')
	if mystr1 in ('exit','quit'):
		with open('record1.txt','r') as f:
			for v in f:
				print(v,end='')
		break
	else:
		with open('record1.txt','a+') as f:
			f.write(mystr1+'\n')


# 2、并将用户输入的内容以追加的方式写入到文件
# 3、直到用户输入exit或者quit则退出程序
# 4、退出的时候显示文件中所有记录的内容
