#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time :  2018/8/26 23:47
# @Author: Bingka.wang
# @Email:  wangbingka@126.com


import os
import urllib
import urllib.request


'''
urllib模块提供的urlretrieve()函数。urlretrieve()方法直接将远程数据下载到本地。

urlretrieve(url, filename=None, reporthook=None, data=None)

•参数filename指定了保存本地路径（如果参数未指定，urllib会生成一个临时文件保存数据。）
•参数reporthook是一个回调函数，当连接上服务器、以及相应的数据块传输完毕时会触发该回调，我们可以利用这个回调函数来显示当前的下载进度。
•参数data指post导服务器的数据，该方法返回一个包含两个元素的(filename, headers) 元组，filename 表示保存到本地的路径，header表示服务器的响应头

'''

# 将baidu的html抓取到本地，保存在''./baidu.html"文件中，同时显示下载的进度。
def cbk(a,b,c):
    '''''回调函数
    @a:已经下载的数据块
    @b:数据块的大小
    @c:远程文件的大小
    '''
    print('a:%s;\nb:%s;\nc:%s'%(a,b,c))
    per=100.0*a*b/c

    #对于仅仅有一个远程文件的特殊处理
    if c == -1:
        per = a*b/100.0
    if per>100:
        per=100
    # elif per <=100 and c == -1:
    #     per = 100.0*a*b/c
    print('%.2f%%' % per)

url='http://www.baidu.com'

# os.path.abspath，返回
dir=os.path.abspath('.')
work_path=os.path.join(dir,'baidu.html')
urllib.request.urlretrieve(url,work_path,cbk)



url='http://www.python.org/ftp/python/2.7.5/Python-2.7.5.tar.bz2'
dir=os.path.abspath('.')
work_path=os.path.join(dir,'Python-2.7.5.tar.bz2')
urllib.request.urlretrieve(url,work_path,cbk)
