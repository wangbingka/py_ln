#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/29  18:40
# @Author  : bingka.wang 
# @Email   : wangbingka@126.com

import requests
import HTMLParser
# request从基础知识：
"""
1、简介：不是标准库，需要安装，最好用的http库，严格的python格式
2、请求：
    requests.request
        2) method:支持get/post/head/put/delete
        3) params:请求的参数
        4) data:支持字典、字节流、或类文件句柄
        5) json:上传的json数据
        6) headers:自定义http的头
        7) cookies：发送额外的cookies
        8) verify：是否检验证书
    requests.get
        1) url
        2) 参数和request一样
    requests.post
        1) url
        2) data
        3) json
        4) 参数和request一样
    requests.head
    requests.put
    requests.delete
3、 应答：requests.Response
    1) status_code：状态码，200，404,505等
    2） headers：应答的http头
    3） json：应答的json数据
    4） text:应答的unicode编码的文本
    5) content：应答的字节流数据
    6) cookies：应答的cookies。自动处理
3、高级用法：
    1) Session:同一个会话内参数保持一致，且会重用TCP连接以提高性能。也会尽量保持连接也提高性能
        Session 有效范围当前会话，一般常用于添加全局一致的Headers参数
    2) SSL证书认证：开启、关闭，自定义CA证书
    3) 上传普通文件和复杂结构的文件
    4) 代理访问

"""

def get_json():
    r = requests.get('http://api.github.com/events')
    print(r.status_code)
    print(r.headers)
    print(r.content)
    print(r.text)
    print(r.json())

def get_querystring():
    url = 'http://httpbin.org/get'
    params = {'qs1':'value1','qs2':'value2'}
    r = requests.get(url,params=params)
    print(r.status_code)
    print(r.content)

def get_custom_headers():
    url = 'http://httpbin.org/get'
    headers = {'x-header1':'value1','x-header2':'value2',}
    r= requests.get(url,headers=headers)
    print(r.status_code)
    print(r.content)

def get_cookie():
    headers= {'User-Agent':'Chrome'}
    url = 'http://www.douban.com'
    r = requests.get(url,headers=headers)
    print(r.status_code)
    print(r.cookies)

    #打印cookie中某一个属性的值
    print(r.cookies['bid'])
    print(r.headers)

# get_cookie()

class DoubanClient(object):
    def __init__(self):
        headers= {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',}
        #创建一个session，更新headers,保持全局可以使用
        self.session = requests.Session()
        self.session.headers.update(headers)
        pass
    def login(self,username,password,source='main',
        redir='https://www.douban.com/',
        login= '登录'):

        url = 'https://accounts.douban.com/login'
        #获取验证码图片和验证码ID
        r = self.session.get(url)
        captcha_url = _get_captcha(r.content)
        if captcha_url:
            captcha_solution = input('please input solutions for [%s]'%captcha_url)
        data= {'form_email':username,
               'form_password':password,
               'source':source,
               'redir':redir,
               'login':login,
        }
        if captcha_url:
            # data['captcha-id'] = captcha_id
            data['captcha-solutions'] = captcha_solution
        headers = {'referer':'https://accounts.douban.com/login?alias=897266654%40qq.com&redir=https%3A%2F%2Fwww.douban.com&source=None&error=1013',
                   'host':'accounts.douban.com'
                   }
        r = self.session.post(url,data=data,headers=headers)
        print(self.session.cookies.items())

def _attr(attrs,attrname):
    for attr in attrs:
        if attr[0] == attrname:
            return attr[1]
    return None

def _get_captcha(content):
    class CaptchaParser(HTMLParser):
        def __init__(self):
            HTMLParser.__init__(self)
            # self.captcha_id=None
            self.captcha_url= None
        def handle_starttag(self, tag, attrs):
            # if tag == 'input' and _attr(attrs,'type') == 'hidden' and _attr(attrs,'name') == 'captcha_id':
            #     self.captcha_id =  _attr(attrs,'value')
            if tag == 'input' and _attr(attrs, 'type') == 'img' and _attr(attrs, 'id') == 'captcha_image':
                self.captcha_url = _attr(attrs,'src')

    p = CaptchaParser()
    p.feed(content)
    return p.captcha_url

c = DoubanClient()
c.login('897266654@qq.com','Za598521')

