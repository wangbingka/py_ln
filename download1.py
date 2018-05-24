# coding:utf-8


import requests
from lxml import html


#1、下载网页
# req = requests.get('https://m.imdb.com/chart/top')
# print(req.content)

def download_url(url):
	req = requests.get(url)
	return req.content
req1 = download_url('https://m.imdb.com/chart/top') 
print(req1)