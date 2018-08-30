#!usr/bin/python
#coding:utf-8
#author:bingka.wang


import requests
import urllib.request
import urllib.parse
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

type_content = {}
typeUrl_list = []
poemUrl_content = {}
poemUrl_list = []
poem_content = {}
poem_list = []




# 还未使用
def _guwen_content(url):
    global poem_content
    global poem_list

    idnum = 'contson%s' % re.split('[_\.]', url)[-2]
    # print(idnum)
    ss = session.get(url)
    response1 = etree.HTML(ss.content.decode('utf-8'))

    print(url)

    if url.startwith('https://www.gushiwen.org'):
        content = response1.xpath('//div[@class="left"]/div[@class="sons"]')

        # print(ss.content.decode('utf-8'))

        # 诗词标题
        try:
            title = content[0].xpath('./div[@class= "cont"]/h1/text()')
            title1 = ''.join(title)
            poem_content['title'] = title1
        except:
            poem_content['title'] = ''

        # 诗词朝代
        try:
            chaodai = content[0].xpath('./div[@class = "cont"]/p[@class= "source"]/a[1]/text()')
            # print(chaodai)
            poem_content['chaodai'] = ''.join(chaodai)

            # 诗词作者
            author = content[0].xpath('./div[@class = "cont"]/p[@class= "source"]/a[2]/text()')
            # print(author)
            poem_content['author'] = ''.join(author)
        except:
            poem_content['chaodai'] = ''
            poem_content['author'] = ''

        # 诗词正文
        content_txt = content[0].xpath('./div[@class = "cont"]/div[@class= "contson"]/text()')
        content_txt1 = ''.join(content_txt)
        content_txt2 = re.sub(r'[\n\t\r]', '', content_txt1)

        # content_list = response1.xpath('//div[@id="' + idnum + '"]/text()') + response1.xpath(
        #     '//div[@id="' + idnum + '"]/p/text()')
        # content_txt = ''.join(content_list)
        # content_txt1 = re.sub(r'[\n\t\r]', '', content_txt)

        poem_content['content'] = content_txt2

        # 诗词译文
        try:
            yiwen_txt = content[1].xpath('./div[@class = "contyishang"]/p/text()')

            yiwen_txt1 = ''.join(yiwen_txt)
            yiwen_txt2 = re.sub(r'[\n\t\r\u3000]', '', yiwen_txt1)

            # # yiwen_list1 = response1.xpath('//div[@class= "contyishang"]')[0]
            # # yiwen_list2 = yiwen_list1.xpath('./p/text()')
            # # print(yiwen_list2)
            # yiwen_txt = ''.join(yiwen_list2)
            # yiwen_txt1 = re.sub(r'[\n\t\r\u3000]', '', yiwen_txt)
            # print(yiwen_txt1)

            poem_content['yiwen'] = yiwen_txt2
        except:
            poem_content['yiwen'] = ''
        # 诗词网址
        poem_content['url'] = url


        # print(poem_content)
        if poem_content in poem_list:
            pass
        else:
            poem_list.append(poem_content)
        poem_content = {}
    else:
        content = response1.xpath('//div[@class="left"]/div[@class="sons"]')

        # print(ss.content.decode('utf-8'))

        # 诗词标题
        try:
            title = content[0].xpath('./div[@class= "cont"]/h1/text()')
            title1 = ''.join(title)
            poem_content['title'] = title1
        except:
            poem_content['title'] = ''

        # 诗词朝代
        try:
            chaodai = content[0].xpath('./div[@class = "cont"]/p[@class= "source"]/a[1]/text()')
            # print(chaodai)
            poem_content['chaodai'] = ''.join(chaodai)

            # 诗词作者
            author = content[0].xpath('./div[@class = "cont"]/p[@class= "source"]/a[2]/text()')
            # print(author)
            poem_content['author'] = ''.join(author)
        except:
            poem_content['chaodai'] = ''
            poem_content['author'] = ''

        # 诗词正文
        try:

            content_txt = content[0].xpath('./div[@class = "cont"]/div[@class= "contson"]')
            content_txt1 = content_txt.xpath('string(.)').encode('utf-8').strip()
            content_txt2 = ''.join(content_txt1)
            content_txt3 = re.sub(r'[\n\t\r]', '', content_txt2)

            # content_list = response1.xpath('//div[@id="' + idnum + '"]/text()') + response1.xpath(
            #     '//div[@id="' + idnum + '"]/p/text()')
            # content_txt = ''.join(content_list)
            # content_txt1 = re.sub(r'[\n\t\r]', '', content_txt)
            poem_content['content'] = content_txt3

        except:
            poem_content['content'] = ''

        # 诗词译文
        try:
            yiwen_txt = content[1].xpath('./div[@class = "contyishang"]/p/text()')

            yiwen_txt1 = ''.join(yiwen_txt)
            yiwen_txt2 = re.sub(r'[\n\t\r\u3000]', '', yiwen_txt1)

            # # yiwen_list1 = response1.xpath('//div[@class= "contyishang"]')[0]
            # # yiwen_list2 = yiwen_list1.xpath('./p/text()')
            # # print(yiwen_list2)
            # yiwen_txt = ''.join(yiwen_list2)
            # yiwen_txt1 = re.sub(r'[\n\t\r\u3000]', '', yiwen_txt)
            # print(yiwen_txt1)

            poem_content['yiwen'] = yiwen_txt2
        except:
            poem_content['yiwen'] = ''
        # 诗词网址

        poem_content['url'] = url

        # print(poem_content)
        if poem_content in poem_list:
            pass
        else:
            poem_list.append(poem_content)
        poem_content = {}




    return poem_list


def _guwen_url(url):
    global poemUrl_list
    global poemUrl_content

    poemUrl_content = {}
    s = session.get(url)
    response = etree.HTML(s.content.decode('utf-8'))
    tangshi300 = response.xpath('//div[@class="typecont"]')

    for inx1, x in enumerate(tangshi300):
    # for x in tangshi300:
        type = x.xpath('./div[@class="bookMl"]/strong/text()')
        url1 = x.xpath('./span/a/@href')
        title = x.xpath('./span/a/text()')




        for inx2, i in enumerate(title):
            if url1[inx2].startswith('http') is False:
                poemUrl_content['type'] = ''.join(type)
                urlist = urllib.parse.urljoin(url,re.split('/', url1[inx2])[-1])
                poemUrl_content['url'] = urlist
                poemUrl_content['title'] = title[inx2]
            else:
                poemUrl_content['type'] = ''.join(type)
                urlist = url1[inx2]
                poemUrl_content['url'] = urlist
                poemUrl_content['title'] = title[inx2]

            if poemUrl_content in poemUrl_list:
                continue
            else:
                poemUrl_list.append(poemUrl_content)
            poemUrl_content = {}



    # print(len(poemUrl_list))
    # print(poemUrl_list)
    return poemUrl_list

def _typeUrl_list(url):
    global typeUrl_list
    global type_content

    s = session.get(url)
    response = etree.HTML(s.content.decode('utf-8'))
    type_list = response.xpath('//div[@class="typecont"]')[4]
    type_list1 = type_list.xpath('./span/a/@href')
    type_title = type_list.xpath('./span/a/text()')

    for inx, i in enumerate(type_list1):
    # for i in type_list1:
        if i.startswith('http') is False:


            url1 = urllib.parse.urljoin(url,re.split('/', i)[-1])
            type_content['title'] = type_title[inx]
            type_content['url'] = url1
            typeUrl_list.append(type_content)
            type_content = {}
        else:
            type_content['title'] = type_title[inx]
            type_content['url'] = i
            typeUrl_list.append(type_content)
            type_content = {}

    for i in typeUrl_list:
        for a in i.keys():
            # print(a)
            # print(i[a])
            write_gushi(a, 'typeUrl_list')
            write_gushi(i[a], 'typeUrl_list')
            write_gushi('\n', 'typeUrl_list')


    print(typeUrl_list)
    return typeUrl_list

def write_gushi(self,txt_name):
    with open('{}.txt'.format(txt_name),'a+',encoding='utf8') as f:
        f.write(self)


if __name__  == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0', }
    # 创建一个session，更新headers,保持全局可以使用
    session = requests.Session()
    session.headers.update(headers)
    url = 'https://www.gushiwen.org/gushi/'
    a = _typeUrl_list(url)

    # b = _guwen_url(a[0]['url'])
    # print(b)
    # c = _guwen_content(b[0]['url'])
    # print(c)


    for i in a:
        print(i['title'])
        b = _guwen_url(i['url'])
        print(b)
        for x in b:
            c = _guwen_content(x['url'])


    for i in poemUrl_list:
        for a in i.keys():
            # print(a)
            # print(i[a])
            write_gushi(a+'\t', 'poemUrl_list')
            write_gushi(i[a], 'poemUrl_list')
            write_gushi('\t', 'poemUrl_list')
        write_gushi('\n', 'poemUrl_list')
    for x in poem_list:
        for a in x.keys():
            # print(a)
            # print(i[a])
            write_gushi(a+'\t', 'poem_list')
            write_gushi(x[a], 'poem_list')
            write_gushi('\t', 'poem_list')
        write_gushi('\n', 'poem_list')