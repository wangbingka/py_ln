#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time :  2018/8/27 22:36
# @Author: Bingka.wang
# @Email:  wangbingka@126.com


import requests
import urllib.request
import os
import threading
from html.parser import  HTMLParser
import re
from lxml import html
from lxml import etree

'''
1、通过首页https://www.gushiwen.org，获取诗文的所有类型列表,返回一个网址list
2、通过诗文的类型对应的网址list，生产诗文类型对应的所有诗词，返回一个网址list
3、通过生产的所有诗词的url，获取诗词对应的诗文内容和译文

'''

typeUrl_list = []
typeUrl_content = {}
poem_list = []
poem_content = {}


# 空列表，所有待下载的Url列表，多线程下载中会使用到
gImageList = []

# 条件控制多线程
gCondition = threading.Condition()

# 定义生产者
class Producer(threading.Thread):
    def run(self):
        global gImageList
        global gCondition

        print('%s:started'%threading.current_thread())

        pass

        # 对条件进行上锁，以便进行操作
        gCondition.acquire()

        # 将对应的url放入对应多线程的列表中
        pass
        print('%s:produce finished. left:%d'%(threading.current_thread(),len(gImageList)))

        # 通知消费者
        gCondition.notify_all()

        # 解锁，把钥匙放回，释放
        gCondition.release()

class Consumer(threading.Thread):
    def run(self):
        print('%s:started' % threading.current_thread())

        # 循环运行获取图片列表,下载数据
        while True:
            global gImageList
            global gCondition

            # 上锁
            gCondition.acquire()
            print('{}:trying to download from pool.pool size is {}'.format(threading.current_thread(),len(gImageList)))

            # 当列表中是空的时候，等待，然后不断的尝试获取列表不等于0的时刻
            while len(gImageList)  == 0:
                gCondition.wait()
                print('{}:waken up. pool size is {}'.format(threading.current_thread(),len(gImageList)))
            url = gImageList.pop()
            gCondition.release()
            pass




def _guwen_url(url):
    s = session.get(url)
    response = etree.HTML(s.content.decode('utf-8'))
    tangshi300 = response.xpath('//div[@class="typecont"]')
    for x in tangshi300:
        type = x.xpath('./div[@class="bookMl"]//strong/text()')
        for i in range(0,10000):
            url1 = x.xpath('./span/a/@href')
            title = x.xpath('./span/a/text()')
            author = x.xpath('./span/text()')
            try:
                typeUrl_content['type'] = ''.join(type)
                print(typeUrl_content['type'])
                urlist = 'https://so.gushiwen.org/%s' % re.split('/', url1[i])[-1]
                typeUrl_content['url'] = urlist
                typeUrl_content['title'] = title[i]
            except:
                print('This\'s all!')
                break
    return typeUrl_content

def _guwen_content(url):
    global poem_content
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

    return poem_content


def write_tangshi300(self,txt_name):
    with open('{}.txt'.format(txt_name),'a+',encoding='utf-8') as f:
        f.write(self+'\t')

if __name__  == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0', }
    # 创建一个session，更新headers,保持全局可以使用
    session = requests.Session()
    session.headers.update(headers)

