#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/26 22:55
# @Author  : bingka.wang 
# @Email   : wangbingka@126.com

import time

#time.time(),公元1970纪元后经过的浮点秒数
print(time.time())

#time.localtime(),返回当前时间，括号里面可以有输入浮点秒数，如果为空，则返回当前时间为标准。
print(time.localtime())
print(time.localtime(time.time()))

#time.asctime()，返回一个可读的时间形式：Tue Jun 26 23:01:03 2018
print(time.asctime(time.localtime()))

#time.ctime，把一个时间戳转为为time.asctime(t)，如果括号中t未给或者为None的时候，默认为time.time()为参数
print(time.ctime())

#time.strftime(format[,t]),接受以时间元组，返回以可读字符串表示的当地时间，格式有参数format决定
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# python中时间日期格式化符号：
# •%y 两位数的年份表示（00-99）
# •%Y 四位数的年份表示（000-9999）
# •%m 月份（01-12）
# •%d 月内中的一天（0-31）
# •%H 24小时制小时数（0-23）
# •%I 12小时制小时数（01-12）
# •%M 分钟数（00=59）
# •%S 秒（00-59）
# •%a 本地简化星期名称
# •%A 本地完整星期名称
# •%b 本地简化的月份名称
# •%B 本地完整的月份名称
# •%c 本地相应的日期表示和时间表示
# •%j 年内的一天（001-366）
# •%p 本地A.M.或P.M.的等价符
# •%U 一年中的星期数（00-53）星期天为星期的开始
# •%w 星期（0-6），星期天为星期的开始
# •%W 一年中的星期数（00-53）星期一为星期的开始
# •%x 本地相应的日期表示
# •%X 本地相应的时间表示
# •%Z 当前时区的名称
# •%% %号本身


#time.sleep(t)，用于推迟调用线程的运行，可通过参数参数secs单位秒数，表示线程挂起的时间
#time.sleep(t),推迟执行t秒钟

print('start:%s'%time.ctime())
time.sleep(5)
print('end:%s'%time.ctime())

