#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/31  21:27
# @Author  : bingka.wang 
# @Email   : wangbingka@126.com


import requests
import urllib.request
import os
import threading
from html.parser import  HTMLParser
import parser
import re
from lxml import html
from lxml import etree



def _guwen_content(url):

    poem_content = {}

    ss = session.get(url)

    # time.sleep(1)

    response1 = etree.HTML(ss.content.decode('utf-8'))

    # print(str(url.encode('utf-8')))
    # print(type(str(url)))

    if  'wen_' not in str(url):
        content = response1.xpath('//div[@class="left"]/div[@class="sons"]')

        # print(ss.content.decode('utf-8'))

        # 诗词标题
        try:
            title = content[0].xpath('string(./div[@class= "cont"]/h1)')
            title1 = re.sub(r'[\n\t\r\u3000]', '', title)
            poem_content['title'] = title1
        except:
            poem_content['title'] = ''

        # 诗词朝代和作者
        try:
            chaodai = content[0].xpath('string(./div[@class = "cont"]/p[@class= "source"])')

            chaodai1 = re.sub(r'[\n\t\r\u3000]', '', chaodai)
            poem_content['chaodai_author'] = chaodai1
        except:
            poem_content['chaodai_author'] = ''

        # 诗词正文
        try:
            content_txt = content[0].xpath('string(./div[@class = "cont"]/div[@class= "contson"])')
            print(content_txt)
            content_txt1 = re.sub(r'[\n\t\r\u3000]', '', content_txt)
            poem_content['content'] = content_txt1
        except:
            poem_content['content'] = ''


        # 诗词译文
        try:
            yiwen_txt = content[1].xpath('string(./div[@class = "contyishang"])')
            yiwen_txt1 = re.sub(r'[\n\t\r\u3000]', '', yiwen_txt)
            poem_content['yiwen'] = yiwen_txt1
        except:
            poem_content['yiwen'] = ''


        # 诗词网址
        poem_content['url'] = url

    else:
        content = response1.xpath('//div[@class="left"]/div[@class="sons"]')

        # print(ss.content.decode('utf-8'))

        # 诗词标题
        try:
            title = content[0].xpath('./div[@class= "cont"]/h1/text()')
            title1 = ''.join(title)
            title2 = re.sub(r'[\n\t\r\u3000]', '', title1)
            poem_content['title'] = title2
        except:
            poem_content['title'] = ''

        # 诗词朝代和作者
        try:
            chaodai = content[0].xpath('string(./div[@class = "cont"]/p[@class= "source"])')
            chaodai1 = ''.join(chaodai)
            chaodai1 = re.sub(r'[\n\t\r\u3000]', '', chaodai)
            poem_content['chaodai&anthor'] = chaodai1

        except:
            poem_content['chaodai&anthor'] = ''

        # 诗词正文
        try:

            # 取出对应文本下所有的包括子节点下的文本内容
            content_txt = content[0].xpath('string(./div[@class = "cont"]/div[@class= "contson"])')
            content_txt1 = re.sub(r'[\n\t\r\u3000]', '', content_txt)
            poem_content['content'] = content_txt1

        except:
            poem_content['content'] = ''

        # 诗词译文
        try:
            yiwen_txt = content[1].xpath('string(./div[@class = "contyishang"]/p/text())')
            yiwen_txt1 = re.sub(r'[\n\t\r\u3000]', '', yiwen_txt)
            poem_content['yiwen'] = yiwen_txt1
        except:
            poem_content['yiwen'] = ''


        # 诗词网址
        poem_content['url'] = url

    print(poem_content)

    return poem_content





if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0', }
    # 创建一个session，更新headers,保持全局可以使用
    session = requests.Session()
    session.headers.update(headers)
    # url = 'https://www.gushiwen.org/wen_1906.aspx'
    # url = 'https://so.gushiwen.org/shiwenv_a76804eee5c9.aspx'

    url = 'https://so.gushiwen.org/shiwenv_740cef8b5937.aspx'


    url = 'https://www.gushiwen.org/wen_1951.aspx'

    type_url_list = _guwen_content(url)