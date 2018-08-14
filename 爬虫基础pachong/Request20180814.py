#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/13  23:21
# @Author  : bingka.wang
# @Email   : wangbingka@126.com

import requests
import bs4
from lxml import html
from selenium import webdriver
import time
import random

driver = webdriver.Chrome()

url = 'http://app1.sfda.gov.cn/datasearch/face3/base.jsp?tableId=25&tableName=TABLE25&title=%B9%FA%B2%FA%D2%A9%C6%B7&bcId=124356560303886909015737447882'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3409.2 Safari/537.36'}
session = requests.Session()
session.headers.update(headers)

driver.get(url)
driver.find_element_by_xpath('//*[@id="content"]/table[2]/tbody/tr[1]/td/p/a').click()


# //*[@id="content"]/div/div/table[1]/tbody/tr[2]/td[2]

response = session.get(url)
driver.find_element_by_xpath('/html/body/ul/li[2]/a').click()
#查看响应状态


print(response.status_code)


r = response.content.decode('utf-8')

tree = html.fromstring(response.text)
title = tree.xpath('//*[@id="content"]/div/div/table[1]/tbody/tr[2]/td[2]')
print(tree)
print(title)


# content = bs4.BeautifulSoup(r,'lxml')
# element_id = content.find_all(id='book')
# # print(element_id)
#
# element_all = content.find_all('nav')
# print(element_all)





