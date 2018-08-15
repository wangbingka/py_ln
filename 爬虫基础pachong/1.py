#!usr/bin/python
#coding:utf-8
#author:bingka.wang

import urllib
import urllib.request
import urllib.parse


#打开网站
response = urllib.request.urlopen('http://www.baidu.com')

# print(response) #这是一个存储地址的格式
# print(response.read()) #无法按照html的样式自动换行
#获取网站的element代码
# print(response.read().decode('utf-8'))



# 这里就用到urllib.parse，通过bytes(urllib.parse.urlencode())可以将post数据进行转换放到urllib.request.urlopen的data参数中。这样就完成了一次post请求。
# 所以如果我们添加data参数的时候就是以post请求方式请求，如果没有data参数就是get请求方式
#更新data
    # data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
    # print(data)
    # response = urllib.request.urlopen('http://httpbin.org/post', data=data)
    # print(response.read().decode('utf-8'))

# timeout参数的使用
# 在某些网络情况不好或者服务器端异常的情况会出现请求慢的情况，或者请求异常，所以这个时候我们需要给
# 请求设置一个超时时间，而不是让程序一直在等待结果。例子如下：
# 如果设置时间太短，还不够打开网页，同样会报错，比如：timeout=0.1
    # response = urllib.request.urlopen('http://httpbin.org/get', timeout=1)
    # print(response.read().decode('utf-8'))

#对于报错,可以用error进行快速处理：
import socket
import urllib.error
try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    #判断一个一个对象是否是一个已知的类型，用法：isinstance(object, classinfo),例子：isinstance (2,int)
    #socket是关于网络协议的一个模块，socket.timeout表示超市
    print(e.reason)
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')

#有很多网站为了防止程序爬虫爬网站造成网站瘫痪，会需要携带一些headers头部信息才能访问，最长见的有user-agent参数
#添加headers和data数据
url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'httpbin.org'
}
dict = {
    'name': 'zhaofan'
}
data = bytes(urllib.parse.urlencode(dict), encoding='utf8')
req = urllib.request.Request(url=url, data=data, headers=headers, method='POST')
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))



def urlencode():
    params = {'score':100,'name':'爬虫基础','comment':'very good'}
    qs = urllib.parse.urlencode(params)
    print(qs)

if __name__ == '__main__':
    urlencode()