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
# URLError,HTTPError，HTTPError是URLError的子类
# URLError里只有一个属性：reason,即抓异常的时候只能打印错误信息，类似上面的例子
# HTTPError里有三个属性：code,reason,headers，即抓异常的时候可以获得code,reson，headers三个信息
    # import socket
    # import urllib.error
    # try:
    #     response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
    # except urllib.error.URLError as e:
    #     #判断一个一个对象是否是一个已知的类型，用法：isinstance(object, classinfo),例子：isinstance (2,int)
    #     #socket是关于网络协议的一个模块，socket.timeout表示超市
    #     print(e.reason)
    #     if isinstance(e.reason, socket.timeout):
    #         print('TIME OUT')

#有很多网站为了防止程序爬虫爬网站造成网站瘫痪，会需要携带一些headers头部信息才能访问，最长见的有user-agent参数
#添加headers和data数据
    # url = 'http://httpbin.org/post'
    # headers = {
    #     'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    #     'Host': 'httpbin.org'
    # }
    # dict = {
    #     'name': 'zhaofan'
    # }
    # data = bytes(urllib.parse.urlencode(dict), encoding='utf8')
    # req = urllib.request.Request(url=url, data=data, headers=headers, method='POST')
    # response = urllib.request.urlopen(req)
    # print(response.read().decode('utf-8'))

# 另一种添加headers方式，这种添加方式有个好处是自己可以定义一个请求头字典，然后循环进行添加
    # from urllib import request, parse
    #
    # url = 'http://httpbin.org/post'
    # dict = {
    #     'name': 'Germey'
    # }
    # data = bytes(parse.urlencode(dict), encoding='utf8')
    # req = request.Request(url=url, data=data, method='POST')
    # req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
    # response = request.urlopen(req)
    # print(response.read().decode('utf-8'))

#网站它会检测某一段时间某个IP 的访问次数，如果访问次数过多，它会禁止你的访问,所以这个时候需要通过设置代理来爬取数据
#urlib.request.ProxyHandler()可以设置代理
#代理,ProxyHandler
    # import urllib.request
    # proxy_handler = urllib.request.ProxyHandler({
    #     'http': 'http://127.0.0.1:9743',
    #     'https': 'https://127.0.0.1:9743'
    # })
    # opener = urllib.request.build_opener(proxy_handler)
    # response = opener.open('http://httpbin.org/get')
    # print(response.read())



# cookie中保存中我们常见的登录信息，有时候爬取网站需要携带cookie信息访问,这里用到了http.cookijar，用于获取cookie以及存储cookie
    # import http.cookiejar, urllib.request
    # cookie = http.cookiejar.CookieJar()
    # handler = urllib.request.HTTPCookieProcessor(cookie)
    # opener = urllib.request.build_opener(handler)
    # response = opener.open('http://www.baidu.com')
    # for item in cookie:
    #     print(item.name+"="+item.value)

# 同时cookie可以写入到文件中保存，有两种方式http.cookiejar.MozillaCookieJar和http.cookiejar.LWPCookieJar()，当然你自己用哪种方式都可以
# 1、http.cookiejar.MozillaCookieJar()方式
    # import http.cookiejar, urllib.request
    # filename = "cookie.txt"
    # cookie = http.cookiejar.MozillaCookieJar(filename)
    # handler = urllib.request.HTTPCookieProcessor(cookie)
    # opener = urllib.request.build_opener(handler)
    # response = opener.open('http://www.baidu.com')
    # cookie.save(ignore_discard=True, ignore_expires=True)
# 2、http.cookiejar.LWPCookieJar()方式
    # import http.cookiejar, urllib.request
    # filename = 'cookie.txt'
    # cookie = http.cookiejar.LWPCookieJar(filename)
    # handler = urllib.request.HTTPCookieProcessor(cookie)
    # opener = urllib.request.build_opener(handler)
    # response = opener.open('http://www.baidu.com')
    # cookie.save(ignore_discard=True, ignore_expires=True)



#想要通过获取文件中的cookie获取的话可以通过load方式，当然用哪种方式写入的，就用哪种方式读取。
    # import http.cookiejar, urllib.request
    # cookie = http.cookiejar.LWPCookieJar()
    # cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
    # handler = urllib.request.HTTPCookieProcessor(cookie)
    # opener = urllib.request.build_opener(handler)
    # response = opener.open('http://www.baidu.com')
    # print(response.read().decode('utf-8'))


# URL解析,对你传入的url地址进行拆分
result = urllib.request.urlparse("http://www.baidu.com/index.html;user?id=5#comment")
# print(result)
# 同时我们是可以指定协议类型,拆分的时候协议类型部分就会是你指定的部分，当然如果你的url里面已经带了协议，你再通过scheme指定的协议就不会生效
result = urllib.request.urlparse("www.baidu.com/index.html;user?id=5#comment",scheme="https")
# print(result)

# urlunpars,功能和urlparse的功能相反，它是用于拼接，例子如下：
from urllib.parse import urlunparse
data = ['http','www.baidu.com','index.html','user','a=123','commit']
# print(urlunparse(data))

# urljoin,这个的功能其实是做拼接的，例子如下,并且后面的优先级高于前面，会自动替换前面的内容：
    # from urllib.parse import urljoin
    # print(urljoin('http://www.baidu.com', 'FAQ.html'))
    # print(urljoin('http://www.baidu.com', 'https://pythonsite.com/FAQ.html'))
    # print(urljoin('http://www.baidu.com/about.html', 'https://pythonsite.com/FAQ.html'))
    # print(urljoin('http://www.baidu.com/about.html', 'https://pythonsite.com/FAQ.html?question=2'))
    # print(urljoin('http://www.baidu.com?wd=abc', 'https://pythonsite.com/index.php'))
    # print(urljoin('http://www.baidu.com', '?category=2#comment'))
    # print(urljoin('www.baidu.com', '?category=2#comment'))
    # print(urljoin('www.baidu.com#comment', '?category=2'))



# urlencode，这个方法可以将字典转换为url参数，例子如下
def urlencode():
    params = {'score':100,'name':'爬虫基础','comment':'very good','wd':123}
    qs = urllib.parse.urlencode(params)
    base_url = "http://www.baidu.com?"

    print(base_url+qs)

if __name__ == '__main__':
    urlencode()