#!usr/bin/python
#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time :  2018/9/18 19:41
# @Author: Bingka.wang
# @Email:  wangbingka@126.com

cluster = 'fjs1'
login_url = ('http://test.{}.yiducloud.cn/sso/passport/user/login'
             '?oauth=http%3A%2F%2Ftest.{}.yiducloud.cn%2Fsso%2Foauth%2Ftoken'
             '&cluster={}'
             '&callback=http%3A%2F%2Ftest.{}.yiducloud.cn'
             '&appid=79391884-a070-11e4-9ac2-52540f6400b4)').format(cluster,cluster,cluster,cluster)
print(login_url)