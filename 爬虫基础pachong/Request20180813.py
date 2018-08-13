#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/13  23:21
# @Author  : bingka.wang
# @Email   : wangbingka@126.com

import requests
import bs4

url = 'http://www.ranzhi.org/book/ranzhi/about-ranzhi-4.html'

response = requests.get(url)

#查看响应状态

print(response.status_code)


r = response.content.decode('utf-8')
# print(r)


content = bs4.BeautifulSoup(r,'lxml')
element_id = content.find_all(id='book')
# print(element_id)

element_all = content.find_all('nav')
print(element_all)





