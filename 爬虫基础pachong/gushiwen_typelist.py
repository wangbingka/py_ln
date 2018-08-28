#!usr/bin/python
#coding:utf-8
#author:bingka.wang


import requests
import urllib.request
import os
import threading
from html.parser import  HTMLParser
import parser
import re
from lxml import html
from lxml import etree

'''
1、通过首页https://www.gushiwen.org，获取诗文的所有类型列表,返回一个网址list
2、通过诗文的类型对应的网址list，生产诗文类型对应的所有诗词，返回一个网址list
3、通过生产的所有诗词的url，获取诗词对应的诗文内容和译文

'''

typeUrl_list = []
poemUrl_content = {}
poemUrl_list = {}
poem_list = []
poem_content = {}

# 还未使用
def _guwen_content(url):
    global poem_content
    global poem_list
    for i in url:
        idnum = 'contson%s' % re.split('[_\.]', url)[-2]
        ss = session.get(url)
        response1 = etree.HTML(ss.content.decode('utf-8'))
        # print(ss.content.decode('utf-8'))

        # 取出对应id的诗正文，但只能取当前div中的，取不出里面再下一层，比如<p>正文</p>。
        # self.current_poem['content'] = response1.xpath('//div[@id="'+idnum+'"]/text()')

        # 诗词标题
        title = response1.xpath('//div[@class= "cont"]')[0]
        title1 = title.xpath('./h1/text()')
        poem_content['title'] = title1

        # 诗词朝代
        chaodai = response1.xpath('//div[@class= "source"]')[0]
        chaodai1 = chaodai.xpath('./a[0]/text()')
        poem_content['chaodai'] = chaodai1

        # 诗词作者
        author = chaodai.xpath('./a[1]/text()')
        poem_content['author'] = author


        # 诗词正文
        content_list = response1.xpath('//div[@id="' + idnum + '"]/text()') + response1.xpath(
            '//div[@id="' + idnum + '"]/p/text()')
        content_txt = ''.join(content_list)
        content_txt1 = re.sub(r'[\n\t\r]', '', content_txt)
        poem_content['content'] = content_txt1

        # 诗词译文
        yiwen_list = response1.xpath('//div[@class= "contyishang"]/p/text()')
        yiwen_list1 = response1.xpath('//div[@class= "contyishang"]')[0]
        yiwen_list2 = yiwen_list1.xpath('./p/text()')
        # print(yiwen_list2)
        yiwen_txt = ''.join(yiwen_list2)
        yiwen_txt1 = re.sub(r'[\n\t\r\u3000]', '', yiwen_txt)
        # print(yiwen_txt1)
        poem_content['yiwen'] = yiwen_txt1
        # 诗词网址
        poem_content['url'] = url

        poem_list.append[poem_content]

    return poem_list


def _guwen_url(url):
    global poemUrl_list

    poemUrl_content = {}
    s = session.get(url)
    response = etree.HTML(s.content.decode('utf-8'))
    tangshi300 = response.xpath('//div[@class="typecont"]')

    for inx1, x in enumerate(tangshi300):
        print(x)
    # for x in tangshi300:
        type = x.xpath('./div[@class="bookMl"]/strong/text()')
        url1 = x.xpath('./span/a/@href')

        title = x.xpath('./span/a/text()')
        for inx2, i in enumerate(title):
            try:
                poemUrl_content['type'] = ''.join(type)
                urlist = 'https://so.gushiwen.org/%s' % re.split('/', url1[inx2])[-1]
                poemUrl_content['url'] = urlist
                poemUrl_content['title'] = title[inx2]
                poemUrl_list.append(poemUrl_content)
                poemUrl_content = {}

            except:
                # print('This\'s all!')
                break
    print(poemUrl_list)
    return poemUrl_list

def _typeUrl_list(url):
    global typeUrl_list

    type_content = {}

    s = session.get(url)
    response = etree.HTML(s.content.decode('utf-8'))
    type_list = response.xpath('//div[@class="typecont"]')[4]
    type_list1 = type_list.xpath('./span/a/@href')
    type_title = type_list.xpath('./span/a/text()')

    for inx, i in enumerate(type_list1):
    # for i in type_list1:
        if i.startswith('http') is False:
            url1 = url + re.split('/', i)[-1]

            type_content['title'] = type_title[inx]
            type_content['url'] = url1
            typeUrl_list.append(type_content)
            type_content = {}
        else:
            type_content['title'] = type_title[inx]
            type_content['url'] = i
            typeUrl_list.append(type_content)
            type_content = {}
    print(typeUrl_list)
    return typeUrl_list



if __name__  == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0', }
    # 创建一个session，更新headers,保持全局可以使用
    session = requests.Session()
    session.headers.update(headers)
    url = 'https://www.gushiwen.org/gushi/'
    a = _typeUrl_list(url)

    print(a[0]['title'])
    _guwen_url(a[0]['url'])