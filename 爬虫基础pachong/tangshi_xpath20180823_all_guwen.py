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
    def __init__(self,url,txt_name):
        self.url = url
        self.txt_name = txt_name
        self.tangshi_list = []
        self.current_poem = {}
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0', }
        # 创建一个session，更新headers,保持全局可以使用
        self.session = requests.Session()
        self.session.headers.update(headers)
    def retrive_tangshi_300(self):
        # url = 'https://www.gushiwen.org/gushi/tangshi.aspx'
        s = self.session.get(self.url)
        response = etree.HTML(s.content.decode('utf-8'))
        tangshi300 = response.xpath('//div[@class="typecont"]')

        for x in tangshi300:
            type = x.xpath('./div[@class="bookMl"]//strong/text()')
            for i in range(0,10000):
                url1 = x.xpath('./span/a/@href')
                title = x.xpath('./span/a/text()')
                author = x.xpath('./span/text()')
                try:
                    self.current_poem['type'] = ''.join(type)
                    print(self.current_poem['type'])
                    self.current_poem['title'] = title[i]
                    author = author[i]
                    author_txt = re.sub(r'[\n()]', '', author)
                    self.current_poem['author'] = author_txt
                    urlist = 'https://so.gushiwen.org/%s' % re.split('/', url1[i])[-1]
                    self.current_poem['url'] = urlist



                    # idnum = 'contson%s'%re.split('[_\.]',url1[i])[-2]
                    # # print(idnum)
                    # ss = self.session.get(urlist)
                    # response1 = etree.HTML(ss.content.decode('utf-8'))
                    # # print(ss.content.decode('utf-8'))
                    #
                    # # 取出对应id的诗正文，但只能取当前div中的，取不出里面再下一层，比如<p>正文</p>。
                    # # self.current_poem['content'] = response1.xpath('//div[@id="'+idnum+'"]/text()')
                    #
                    # content_list = response1.xpath('//div[@id="' + idnum + '"]/text()')+response1.xpath('//div[@id="' + idnum + '"]/p/text()')
                    # content_txt = ''.join(content_list)
                    # content_txt1 = re.sub(r'[\n\t\r]', '', content_txt)
                    # self.current_poem['content'] = content_txt1
                    # # print(idnum)
                    # # print(self.current_poem['content'])
                    # yiwen_list = response1.xpath('//div[@class= "contyishang"]/p/text()')
                    # yiwen_list1 = response1.xpath('//div[@class= "contyishang"]')[0]
                    # yiwen_list2 = yiwen_list1.xpath('./p/text()')
                    # # print(yiwen_list2)
                    # yiwen_txt = ''.join(yiwen_list2)
                    # yiwen_txt1 = re.sub(r'[\n\t\r\u3000]', '', yiwen_txt)
                    # # print(yiwen_txt1)
                    # self.current_poem['yiwen'] = yiwen_txt1



                    self.tangshi_list.append(self.current_poem)
                    self.current_poem = {}

                except:
                    print('This\'s all!')
                    break
        for i in self.tangshi_list:
            for a in i.keys():
                # print(a)
                # print(i[a])
                write_tangshi300(a, self.txt_name)
                write_tangshi300(i[a], self.txt_name)
            write_tangshi300('\n', self.txt_name)
        print(self.tangshi_list)
        return self.tangshi_list
    def guwen_content(self):

        for i in (0,10000):
            try:
                url = self.tangshi_list[i]['url']
                idnum = 'contson%s' % re.split('[_\.]', url[i])[-2]
                # print(idnum)
                ss = self.session.get(url)
                response1 = etree.HTML(ss.content.decode('utf-8'))
                # print(ss.content.decode('utf-8'))

                # 取出对应id的诗正文，但只能取当前div中的，取不出里面再下一层，比如<p>正文</p>。
                # self.current_poem['content'] = response1.xpath('//div[@id="'+idnum+'"]/text()')

                content_list = response1.xpath('//div[@id="' + idnum + '"]/text()') + response1.xpath(
                    '//div[@id="' + idnum + '"]/p/text()')
                content_txt = ''.join(content_list)
                content_txt1 = re.sub(r'[\n\t\r]', '', content_txt)
                self.tangshi_list[i]['content'] = content_txt1
                # print(idnum)
                # print(self.current_poem['content'])
                yiwen_list = response1.xpath('//div[@class= "contyishang"]/p/text()')
                yiwen_list1 = response1.xpath('//div[@class= "contyishang"]')[0]
                yiwen_list2 = yiwen_list1.xpath('./p/text()')
                # print(yiwen_list2)
                yiwen_txt = ''.join(yiwen_list2)
                yiwen_txt1 = re.sub(r'[\n\t\r\u3000]', '', yiwen_txt)
                # print(yiwen_txt1)
                self.tangshi_list[i]['yiwen'] = yiwen_txt1
            except:
                print('This\'s all!')
                break
        print(self.tangshi_list)
        return self.tangshi_list


def write_tangshi300(self,txt_name):
    with open('{}.txt'.format(txt_name),'a+',encoding='utf-8') as f:
        f.write(self+'\t')

if __name__  == '__main__':
    # tangshi = tangShi300('https://www.gushiwen.org/gushi/tangshi.aspx','tangshi300')
    # tangshi.retrive_tangshi_300()

    # 用于其他
    gushi300 = tangShi300('https://so.gushiwen.org/gushi/sanbai.aspx', 'gushi300')
    gushi300.retrive_tangshi_300()
    gushi300.guwen_content()




