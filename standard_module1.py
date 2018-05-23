#time模块
import time
print(dir(time))
now_time = time.localtime()
print(type(now_time))
print(now_time.tm_year)
print(now_time.tm_mon)
print(now_time.tm_mday)
print(str(now_time.tm_year)+'-'+str(now_time.tm_mon)+'-'+str(now_time.tm_mday))
print(time.strftime('%Y',time.localtime()))
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))

#os模块
import os
#判断一个文件的存储地址
print(os.path.abspath('resources_cn.jar'))
#返回一个文件的名称
print(os.path.basename('resources_cn.jar'))
#拆分路径为一个元组
print(os.path.split('C:\py_ln\resources_cn.jar'))
#拆分路径为元组，最后一个是后缀名，也可以直接拆分文件名和后缀
print(os.path.splitext('C:\py_ln\resources_cn.jar'))
a= os.path.splitext('C:\py_ln\resources_cn.jar')
print(a[-1])
#返回当前的路径名
b= os.getcwd()
print(b)
#把某某路径下的所有文件转成列表
c = os.listdir(b)
#print(c)
#makedirs：创建目录层，removedirs：删除目录层，必须超过一个否则会报错
	 #os.makedirs('test_files/test/abc')
	 #os.removedirs('test_files/test/abc')
	 #os.makedirs('test_files/test/abc')
#mkdir：创建单层目录，rmdir：删除单层目录
	 # os.mkdir('test1')
	 # os.mkdir('test2')
	 # os.rmdir('test1')
#创建一个叫123.txt的文件
f = open('123.txt','w') 
f.write('Hello World，你好世界')
f.close()
