# coding:utf-8
#

import requests


#1、下载网页
req = requests.get('https://m.imdb.com/chart/top')
print(req.content)

def download_url(url):
	req = requests.get('https://m.imdb.com/chart/top')
	print(req.content)