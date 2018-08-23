#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time :  2018/8/22 22:23
# @Author: Bingka.wang
# @Email:  wangbingka@126.com

import requests
from html.parser import  HTMLParser
import re
from lxml import html
from lxml import etree



class tangShi300():
    def __init__(self):
        self.tangshi_list = []
        self.current_poem = {}
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0', }
        # 创建一个session，更新headers,保持全局可以使用
        self.session = requests.Session()
        self.session.headers.update(headers)
    def retrive_tangshi_300(self):
        url = 'https://www.gushiwen.org/gushi/tangshi.aspx'
        s = self.session.get(url)
        response = etree.HTML(s.content.decode('utf-8'))
        tangshi300 = response.xpath('//div[@class="typecont"]')
        for x in tangshi300:
            type = x.xpath('./div[@class="bookMl"]//strong/text()')
            for i in range(0,300):
                url1 = x.xpath('./span/a/@href')
                title = x.xpath('./span/a/text()')
                author = x.xpath('./span/text()')
                try:
                    self.current_poem['type'] = ''.join(type)
                    self.current_poem['title'] = title[i]
                    self.current_poem['url'] = url1[i]
                    idnum = 'contson%s'%re.split('[_\.]',url1[i])[-2]
                    # print(idnum)
                    ss = self.session.get(url1[i])
                    response1 = etree.HTML(ss.content.decode('utf-8'))
                    # print(ss.content.decode('utf-8'))

                    # 取出对应id的诗正文，但只能取当前div中的，取不出里面再下一层，比如<p>正文</p>。
                    # self.current_poem['content'] = response1.xpath('//div[@id="'+idnum+'"]/text()')

                    content_list = response1.xpath('//div[@id="' + idnum + '"]/text()')+response1.xpath('//div[@id="' + idnum + '"]/p/text()')
                    content_txt = ''.join(content_list)
                    self.current_poem['content'] = content_txt
                    # print(idnum)
                    # print(self.current_poem['content'])
                    yiwen_list = response1.xpath('//div[@class= "contyishang"]/p/text()')
                    yiwen_txt = ''.join(yiwen_list)
                    self.current_poem['yiwen'] = yiwen_txt

                    self.current_poem['author'] = author[i]
                    self.tangshi_list.append(self.current_poem)
                    self.current_poem = {}

                except:
                    print('This\'s OK!')
                    break

        return self.tangshi_list

def write_tangshi300(self,txt_name):
    with open('{}.txt'.format(txt_name),'a+',encoding='utf-8') as f:
        f.write(self+'\t')

if __name__  == '__main__':
    tangshi = tangShi300()
    # print(tangshi.retrive_tangshi_300())
    for i in tangshi.retrive_tangshi_300():
        for a in  i.keys():
            print(a)
            print(i[a])
            write_tangshi300(a,'tangshi300')
            write_tangshi300(i[a],'tangshi300')
        write_tangshi300('\n', 'tangshi300')




