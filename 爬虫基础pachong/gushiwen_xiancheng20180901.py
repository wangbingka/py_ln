#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/31  22:38
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

'''
1、通过首页https://www.gushiwen.org，获取诗文的所有类型列表,返回一个网址list
2、通过诗文的类型对应的网址list，生产诗文类型对应的所有诗词，返回一个网址list
3、通过生产的所有诗词的url，获取诗词对应的诗文内容和译文

'''

type_content = {}
typeUrl_list = []
poemUrl_content = {}
poemUrl_list = []
poem_list = []


gImageList = []
gCondition = threading.Condition()


# 定义生产者
class Producer(threading.Thread):
    def run(self):

        global poem_url_list
        global gImageList
        global gCondition


        print('%s:started'%threading.current_thread())


        # 循环运行获取图片列表,下载数据
        while len(poem_url_list) > 0:
            # 上锁
            gCondition.acquire()

            # if len(poem_url_list) == 0:
            #     gCondition.wait()

            print(len(poem_url_list))
            gImageList_dict = poem_url_list.pop()

            if 'url' in gImageList_dict:
                gImageList.append(gImageList_dict['url'])

            key_list = []
            value_list = []
            for x in gImageList_dict:
                key_list.append(x)
                value_list.append(gImageList_dict[x])

            write_gushi(key_list[0] + '\t' + value_list[0] + '\t'+key_list[1] + '\t' + value_list[1]+'\t'+key_list[2] + '\t' + value_list[2]+'\n', 'poem_url')




            if len(gImageList) >100:
                gCondition.wait()
                print('%s:produce finished. left:%d' % (threading.current_thread(), len(gImageList)))



            # 通知消费者
            gCondition.notify_all()

            # 解锁，把钥匙放回，释放
            gCondition.release()





class Consumer(threading.Thread):
    def run(self):

        global gImageList
        global gCondition

        print('%s:started' % threading.current_thread())

        num = 0
        # 循环运行获取图片列表,下载数据
        while True and num <11111:
            # 上锁
            gCondition.acquire()
            print('{}:trying to download poem from pool.pool size is {}'.format(threading.current_thread(),len(gImageList)))
            if len(gImageList) == 0:
                gCondition.wait()
                print('{}:waken up. pool size is {}'.format(threading.current_thread(), len(gImageList)))
            url1 = gImageList.pop()
            gCondition.release()
            poem_content_str = _guwen_content(url1)



            if poem_content_str not in poem_list:
                poem_list.append(poem_content_str)

            key_list = []
            value_list = []
            for x in poem_content_str:
                key_list.append(x)
                value_list.append(poem_content_str[x])

            write_gushi(key_list[0] + '\t'+value_list[0]+'\t'+key_list[1] + '\t'+value_list[1]+'\t'+key_list[2] + '\t'+value_list[2]+'\t'+key_list[3] + '\t'+value_list[3]+'\t'+key_list[4] + '\t'+value_list[4]+'\n', 'poem_list')

            num +=1


def _guwen_content(url):
    poem_content = {}

    ss = session.get(url)

    # time.sleep(1)

    response1 = etree.HTML(ss.content.decode('utf-8'))

    # print(str(url.encode('utf-8')))
    # print(type(str(url)))

    if 'wen_' not in str(url):
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
            # print(content_txt)
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

    return poem_content


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
            if  url1[inx2].startswith('/shiwenv') :
                poemUrl_content['type'] = ''.join(type)
                # urlist = urllib.parse.urljoin(url,re.split('/', url1[inx2])[-1])
                urlist = 'https://so.gushiwen.org/%s' % (re.split('/', url1[inx2])[-1])
                poemUrl_content['url'] = urlist
                poemUrl_content['title'] = title[inx2]
            elif  url1[inx2].startswith('/wen') :
                poemUrl_content['type'] = ''.join(type)
                urlist = 'https://www.gushiwen.org/%s'%(re.split('/', url1[inx2])[-1])
                poemUrl_content['url'] = urlist
                poemUrl_content['title'] = title[inx2]
            else:
                poemUrl_content['type'] = ''.join(type)
                urlist = url1[inx2]
                poemUrl_content['url'] = urlist
                poemUrl_content['title'] = title[inx2]

            # 判断字典中是否存在这个键值
            poem_url_only_list = []
            for i in poemUrl_list:
                if 'url' in i:
                    poem_url_only_list.append(i['url'])
            if urlist in poem_url_only_list:
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
            write_gushi(a+'\t'+i[a]+'\t', 'typeUrl_list')
        write_gushi('\n', 'typeUrl_list')


            # write_gushi(a, 'typeUrl_list')
            # write_gushi(i[a], 'typeUrl_list')
            # write_gushi('\n', 'typeUrl_list')


    print(typeUrl_list)
    return typeUrl_list

def write_gushi(self,txt_name):
    with open('./gushi/{}.txt'.format(txt_name),'a+',encoding='utf8') as f:
        f.write(self)


if __name__  == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0', }
    # 创建一个session，更新headers,保持全局可以使用
    session = requests.Session()
    session.headers.update(headers)
    url = 'https://www.gushiwen.org/gushi/'
    type_url_list = _typeUrl_list(url)
    for i in type_url_list:
        print(i['title'])
        poem_url_list = _guwen_url(i['url'])


    # for i in range(10):
    #     Producer().start()
    # for i in range(10):
    #     Consumer().start()

    for i in range(100):
        Producer().start()
        Consumer().start()
