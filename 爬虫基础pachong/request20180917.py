#!usr/bin/python
#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time :  2018/9/17 17:14
# @Author: Bingka.wang
# @Email:  wangbingka@126.com

import requests
import time
import os
import uuid
import threading
from html.parser import  HTMLParser
import parser
import re
from lxml import html
from lxml import etree
import json
import hashlib



headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36',
'Connection':'keep-alive',}
cookies = {
'nginx_proxy_session':'UkfGw3Yp2Ae-ik1oLU6suw..|1537236802|OuK6zuELNCYvDU3kXTC0FMNwzKQ.',
'session':'A72HI6WZ7KR72II6O6X7QOF3AQKZRIVYGTYZIM7QS2OXI27JCO55HPXVXEVHG7D2ZO2O2W7OQRAGQNIJHEEHKOF7K73ILULXOAFUCC6YVPOAYNHTDZIFIVMRMRXET63M6KEJSLEGTZTIQKQKWMRA6C6YQM======',
'uid':'5eb6491e1b8e-0b59-5e54-902c-41a16b56',
}

cookies = {

'nginx_proxy_session':'hKzIkwebFFfsPj0rvsSsKw..|1537270168|YGUx9NlwmsrK9NklbVBKox671Co.',
'Hm_lvt_4e5bdf78b2b9fcb88736fc67709f2806':1537183769,
'Hm_lpvt_4e5bdf78b2b9fcb88736fc67709f2806':1537185408,
'Hm_lvt_cc903faaed69cca18f7cf0997b2e62c9':1537183769,
'Hm_lpvt_cc903faaed69cca18f7cf0997b2e62c9':1537185408,
'session':'34AOQAQHMTUHNLXUDCYM3TWYXRUFZBCQPJVLZQSN76SMXRFXC2LB7P5QMYUFLEZSCMSIB6LV3MCTLHHMTQXPD2TUGS5VD4PU25SL5D5YJYMGHY7WK4KSOTHHXAKADHYURVEP4EX5KHTDZ6MULQDJLUJCSQ======',
'uid':'5eb6491e1b8e-0b59-5e54-902c-41a16b56',
}


params = {
'dataType':0,
'labelType':0,
'pageType':0,
'systemType':0,
'timeFilter':0,
'updateType':0,
'versionType':1,
}

nginx_proxy_session = "hKzIkwebFFfsPj0rvsSsKw..|1537270168|YGUx9NlwmsrK9NklbVBKox671Co." # 每日更新

session = requests.session()
session.headers.update(headers)
requests.utils.add_dict_to_cookiejar(session.cookies,{"nginx_proxy_session":nginx_proxy_session})


def gen_md5(str):
    if not str:
        return None
    m1 = hashlib.md5()
    m1.update(str.encode("utf8"))
    return m1.hexdigest()

print(gen_md5('Za598521'))
print(gen_md5('Za598521'))
print(gen_md5('Za598521'))


login_url = 'http://passport.dp.yiducloud.cn/api/iam/authenticate/password'
payload = {
'password':'%s'%(gen_md5('Za598521')),
'username':'bingka.wang',
}

Jsondata = '[{"password":"Za598521","username":"bingka.wang"}]'
j=json.loads(Jsondata)

l = session.post(login_url,json=j)
print(l.text)

comment_url = 'http://deming.dp.yiducloud.cn/api/dm/hospital/getIndexHospital'


# s = session.get(url,params=params,cookies=cookies)
# print(s)
# data = s.json()
# print(data)
# # response = etree.HTML(s.content.decode('utf-8'))
# # print(s.content.decode('utf-8'))
# # print(response)