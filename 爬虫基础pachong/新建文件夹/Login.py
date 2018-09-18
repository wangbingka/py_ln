#!/usr/bin/env python
#encoding=utf-8
#@Author: tingru.yin@yiducloud.cn, 2017, all rights reserved
#@Created on 2017-06-11
#@Brief:
'''common module for user login
'''

import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

import hashlib
import json
import urllib
import urllib.request

# import cookielib
import http.cookiejar

# import urlparse
from urllib import parse


import requests

headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36',
'Connection':'keep-alive',}

session1 = requests.session()
session1.headers.update(headers)

nginx_proxy_session = "Zm8M0XNiBixi8GjB3wRgWg..|1537323095|2OXyzeqpQIOY2RQtrjBwsRpiWF0." # 每日更新
requests.utils.add_dict_to_cookiejar(session1.cookies,{"nginx_proxy_session":nginx_proxy_session})

class Login():
    class Login():
        login_url = "http://oauth2.dev.m.com/api/iam/authenticate/password"

        username = "qatest80"
        password = "lifeisgood007A"
    def __init__(self):
        pass

    @classmethod
    def user_login(self, cluster,username, password, msg_list = None):
        """user login function"""

        global session1
        cookiejar = http.cookiejar.CookieJar()
        login_host = 'http://test.%s.yiducloud.cn'%cluster
        login_info = {}
        login_info["username"] = username
        login_info["password"] = self.gen_md5(password)
        login_json = json.dumps(login_info)
        #print 'login'
        # url_opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookiejar))
        #login_url = urlparse.urljoin(login_host, "/api/iam/authenticate/password")
        # login_url = login_host + "/sso/passport/user/login?" + "oauth=" + login_host + "/sso/oauth/token" + "&cluster={}".format(cluster) + "&callback=" + login_host + "&appid=79391884-a070-11e4-9ac2-52540f6400b4"

        login_url = ('http://test.{}.yiducloud.cn/sso/passport/user/login'
                     '?oauth=http%3A%2F%2Ftest.{}.yiducloud.cn%2Fsso%2Foauth%2Ftoken'
                     '&cluster={}'
                     '&callback=http%3A%2F%2Ftest.{}.yiducloud.cn'
                     '&appid=79391884-a070-11e4-9ac2-52540f6400b4)').format(cluster,cluster,cluster,cluster)
        print(login_url)
        #print login_url
        req = session1.post(login_url, login_json, {"Content-Type" : "application/json"})
        print(req)
        print(req.text)
        #print "login:",req
        #print req
        session = None
        try:
            response = url_opener.open(req)
            #print 'response'
            #print response.read()
            #print 'cookiejar'
            #print cookiejar
            ss = [cookie.value for cookie in cookiejar]
            if len(ss) < 1:
                print("failed to read session")
                exit()
            session = ss[0]
            sso_usession=session
            session=session+';'+'sso_usession='+sso_usession

            #print 'session'
            #print session
            #print 'ss'
           # print ss
        except Exception as ecp:
            #print "ecp:",ecp
            print("[ERROR]login failed:",ecp)
            raise
            #if msg_list is not None:
            #    msg_list.append("login:%s" % str(ecp))
        return session

    @classmethod
    def gen_md5(self, str):
        if not str:
            return None
        m1 = hashlib.md5()
        m1.update(str.encode("utf8"))
        return m1.hexdigest()

if __name__ == "__main__":

    result = Login().user_login('fjs1','wangbingka@yiducloud','Za598521')
    print(result)
    if not result:
        print("login failed")
        exit()
    print("succeed to login.")