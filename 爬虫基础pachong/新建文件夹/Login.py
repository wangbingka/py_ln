#!/usr/bin/env python
#encoding=utf-8
#@Author: tingru.yin@yiducloud.cn, 2017, all rights reserved
#@Created on 2017-06-11
#@Brief:
'''common module for user login
'''

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import hashlib
import json
import urllib2
import cookielib
import urlparse


class Login():
    login_url = "http://oauth2.dev.m.com/api/iam/authenticate/password"

    username = "qatest80"
    password = "lifeisgood007A"

    def __init__(self):
        pass

    @classmethod
    def user_login(self, login_host, username, password, msg_list = None):
        """user login function"""
        cookiejar = cookielib.CookieJar()
        login_info = {}
        login_info["username"] = username
        login_info["password"] = self.gen_md5(password)
        login_json = json.dumps(login_info)
        #print 'login'
        url_opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))
        #login_url = urlparse.urljoin(login_host, "/api/iam/authenticate/password")
        login_url = login_host + "/sso/passport/user/login?" + "oauth=" + login_host + "/sso/oauth/token" + "&cluster=xxx" + "&callback=" + login_host + "&appid=79391884-a070-11e4-9ac2-52540f6400b4"
        #print login_url
        req = urllib2.Request(login_url, login_json, {"Content-Type" : "application/json"})
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
                print "failed to read session"
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
            print "[ERROR]login failed:",ecp
            raise
            #if msg_list is not None:
            #    msg_list.append("login:%s" % str(ecp))
        return session

    @classmethod
    def gen_md5(self, str):
        if not str:
            return None
        m1 = hashlib.md5()
        m1.update(str)
        return m1.hexdigest()

if __name__ == "__main__":

    result = Login.user_login()
    print result
    if not result:
        print "login failed"
        exit()
    print "succeed to login."