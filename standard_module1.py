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
#拆分路径为元组，包括后缀名，最后一个是
print(os.path.splitext('C:\py_ln\resources_cn.jar'))
a= os.path.splitext('C:\py_ln\resources_cn.jar')
print(a[-1])
