#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/21  11:57
# @Author  : bingka.wang 
# @Email   : wangbingka@126.com

from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://tieba.baidu.com/index.html')
driver.find_element_by_xpath('//*[@id="com_userbar"]/ul/li[4]/div/a').click()

print('请登录')
time.sleep(50)
print('获取cookie')
print(driver.get_cookies())