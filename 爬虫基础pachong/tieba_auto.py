#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/21  23:18
# @Author  : bingka.wang 
# @Email   : wangbingka@126.com

from selenium import webdriver
import time
import random


driver = webdriver.Chrome()
# driver.get('https://tieba.baidu.com/index.html')
# driver.find_element_by_xpath('//*[@id="com_userbar"]/ul/li[4]/div/a').click()
#
# print('请登录')
# time.sleep(50)
# print('获取cookie')
# print(driver.get_cookies())

cook = [{'domain': '.tieba.baidu.com', 'expiry': 1609430398.59174, 'httpOnly': False, 'name': 'TIEBAUID', 'path': '/', 'secure': False, 'value': '45a1bae39645d6ee40e230fc'}, {'domain': '.tieba.baidu.com', 'expiry': 1609430398.423176, 'httpOnly': False, 'name': 'TIEBA_USERTYPE', 'path': '/', 'secure': False, 'value': 'dd9cfee9b742286a76f72298'}, {'domain': '.baidu.com', 'expiry': 1563705015.423177, 'httpOnly': False, 'name': 'BAIDUID', 'path': '/', 'secure': False, 'value': 'BF58E9F0E3C357A8CFD21DA45FDA0969:FG=1'}, {'domain': '.baidu.com', 'expiry': 2556057600, 'httpOnly': False, 'name': 'FP_UID', 'path': '/', 'secure': False, 'value': '4edc2c14204f156c9b2b485255114ed8'}, {'domain': '.tieba.baidu.com', 'expiry': 1563705047, 'httpOnly': False, 'name': 'Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948', 'path': '/', 'secure': False, 'value': '1532169016'}, {'domain': '.baidu.com', 'expiry': 1791369045.523743, 'httpOnly': True, 'name': 'BDUSS', 'path': '/', 'secure': False, 'value': 'V4SlZ2bWl0NndHZHBRcE4xUFdsaXZsWmR1dXF5TWptOGJTa3RCaEloSldtSHBiQVFBQUFBJCQAAAAAAAAAAAEAAABCOlvQsKG5~rn-uf5xYXoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFYLU1tWC1NbUX'}, {'domain': '.tieba.baidu.com', 'expiry': 1534761047.17774, 'httpOnly': True, 'name': 'STOKEN', 'path': '/', 'secure': False, 'value': '517fbb4958ab4a3c615470c17458c8ec0149321ac6b99400bc415572db75807c'}, {'domain': '.tieba.baidu.com', 'httpOnly': False, 'name': 'Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948', 'path': '/', 'secure': False, 'value': '1532169048'}]

#进入需要回复的帖子
post_url = 'https://tieba.baidu.com/p/5804883467'

#使用cookie
# def add_cookie(cook):
driver.get('https://tieba.baidu.com/index.html')
driver.delete_all_cookies()

for i in cook:
    print(i)
    driver.add_cookie(i)
print('增加cookie成功')
print('进入帖子页面')
driver.get(post_url)

i = 1
while True and i < 3:
    #发帖
    #点击评论按钮
    driver.find_element_by_xpath('/html/body/ul/li[2]/a').click()
    a = random.uniform(1, 3)
    time.sleep(a)
    #评论框中输入内容
    b= '成功啦'+str(round(random.uniform(1, 1000),0))
    driver.find_element_by_xpath('//*[@id="ueditor_replace"]').send_keys(b)
    driver.find_element_by_xpath('//*[@id="tb_rich_poster"]/div[3]/div[3]/div/a').click()
    i +=1
