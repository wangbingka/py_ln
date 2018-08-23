#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time :  2018/8/20 22:17
# @Author: Bingka.wang
# @Email:  wangbingka@126.com

import requests
from html.parser import  HTMLParser
import re

'''
此脚本失败，未达成目的
原因，HTMLParser,div内包含一个div，导致无法通过handle_endtag，初始化设置的True为False
'''

def _attr(attrlist, attrname):
    for attr in attrlist:
        if attr[0] == attrname:
            return attr[1]
    return None

class tangshiParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.tangshi_list = []
        self.in_div = False
        self.in_div2 = False
        self.in_a = False
        self.in_span = False
        self.current_poem = {}
        self.pattern = re.compile(r'''
                (.+)  #匹配标题
                \n\(    #匹配作者左边的括号
                (.+)  #匹配作者
                \)    #匹配作者右边的括号
                ''', re.VERBOSE)
    def handle_starttag(self,tag,attrs):
        if tag == 'div' and _attr(attrs,'class') == 'typecont':
            self.in_div = True
        if self.in_div and _attr(attrs,'class') == 'bookMl':
            self.in_div2 =True
        if self.in_div and tag == 'span':
            self.in_span = True
        if self.in_div  and tag == 'a':
            self.in_a = True
            self.current_poem['url'] = _attr(attrs,'href')
            print(self.current_poem['url'])
    def handle_endtag(self,tag):
        # if tag == 'div':
        #     self.in_div = False
        if tag == 'span':
            self.in_span = False
        if tag == 'a':
            self.in_a = False
            self.in_div = False
            self.in_div2 = False
    def handle_data(self,data):
        # if self.in_a:
        #     # print(data)
        #     self.current_poem['title'] = data
        if self.in_span:
            print(data)
            # self.current_poem['author'] = data
            # self.tangshi_list.append(self.current_poem)
            m = self.pattern.match(data)
            print(m)
            if m:
                self.current_poem['title']  = m.group(1)
                print(m.group(1))
                self.current_poem['author'] = m.group(2)
                self.tangshi_list.append(self.current_poem)







def retrive_tangshi_300():
    url = 'https://www.gushiwen.org/gushi/tangshi.aspx'
    s = requests.get(url)
    parser = tangshiParser()
    # print(s.content.decode('utf-8'))
    parser.feed(s.content.decode('utf-8'))
    return parser.tangshi_list

if __name__  == '__main__':
    retrive_tangshi_300()
    for i in retrive_tangshi_300():
        print(i)
