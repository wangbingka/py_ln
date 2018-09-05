#!usr/bin/python
#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time :  2018/9/5 16:19
# @Author: Bingka.wang
# @Email:  wangbingka@126.com


import urllib.parse, urllib.request, http.cookiejar
import webbrowser


# 设置cookie
def set_cookie():
    # 初始化一个CookieJar来处理Cookie
    cookie = http.cookiejar.CookieJar()
    cookieProc = urllib.request.HTTPCookieProcessor(cookie)
    # 实例化一个全局opener
    opener = urllib.request.build_opener(cookieProc)
    urllib.request.install_opener(opener)


# 打开网页
def get_url_request(open_url, post_data={}):
    post_data = urllib.parse.urlencode(post_data)
    post_data = post_data.encode(encoding='utf-8')
    # 不添加header也能成功
    # header = {"User-Agent":"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
    req = urllib.request.Request(
        url=open_url,
        data=post_data,
        # headers = header
    )

    return urllib.request.urlopen(req).read().decode("utf-8")


# 执行
if __name__ == "__main__":
    username = "wangbingka@yiducloud"
    password = "Za598521"

    # 以下三个属性通过抓包获取
    # 向此网址发送登录请求
    url_login = r'http://nova.cmu1h.yiducloud.cn/'

    # 登录后跳转到此网址
    url_login_success = r'http://nova.cmu1h.yiducloud.cn/#/data-overview?redirect=true'

    # 登录需要提交的数据
    login_params = {"f": "check_login", "username": username, "password": password}

    # 登录
    # get_url_request(url_login, login_params)
    # # 打开登录后页面
    result = get_url_request(url_login_success)
    print(result)