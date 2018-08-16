#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time :  2018/8/16 22:12
# @Author: Bingka.wang
# @Email:  wangbingka@126.com


import urllib
import urllib.request
from html.parser  import HTMLParser
import requests

class MovieParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.movies = []
        self.inmovies = False
    def handle_starttag(self,tag,attrs):
        # print(attrs)
        def _attr(attrlist,attrname):
            for attr in attrlist:
                if attr[0] == attrname:
                    return attr[1]
            return None

        if tag == 'li' and _attr(attrs, 'data-title'):
            movie = {}
            movie['title'] = _attr(attrs,'data-title')

            movie['score'] = _attr(attrs,'data-rate')
            movie['director'] = _attr(attrs,'data-director')

            movie['actors'] = _attr(attrs,'data-actors')
            movie['duration'] = _attr(attrs, 'data-duration')

            self.movies.append(movie)
            print(movie)
            # 字典的用法：让Key和value值一一对应展示
            print('%(title)s|%(score)s|%(director)s|%(actors)s|%(duration)s'%movie)

            # 在满足上面的If条件时，改变初始变量的值，以便取到的是我们想要范围的值
            self.inmovies = True

        if tag == 'img' and self.inmovies:

            # 获取到范围，再类似初始化初始变量的值，以便不会多获取无关的信息，以便可以循环获取我们想要的内容
            self.inmovies = False

            # 获取对应项获取的信息
            src = _attr(attrs,'src')

            # 字典有一个值时，这个值的索引数是对应的-1位数
            movie = self.movies[len(self.movies)-1]
            movie['poster-url'] = src

            _downloag_poster_image(movie)

def _downloag_poster_image(movie):
    src = movie['poster-url']
    r = requests.get(src)

    # 保存到相对路径的如下两种种写法
    # fname = './images/%s'%(movie['title']+src.split('/')[-1])
    # with open(fname, 'wb') as f:

    fname = movie['title'] + src.split('/')[-1]
    with open('images/%s'%fname,'wb') as f:


        f.write(r.content)
        movie['poster-path'] = fname


def nowpalying_movies(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'}
    s = requests.get(url,headers=headers)
    parser = MovieParser()
    # print(s.read().decode('utf-8'))
    parser.feed(s.content.decode('utf-8'))
    print('正在热播电影的数量：%s' % len(parser.movies))
    return parser.movies

if __name__ == '__main__':
    url = 'https://movie.douban.com/'
    movies = nowpalying_movies(url)
    # print(movies)

    import json

    # 如下写都是乱码，需要转码json.dumps 序列化时默认使用的ascii编码，想输出真正的中文需要指定ensure_ascii=False：
    # 更深入分析，是应为dJSON object 不是单纯的unicode实现，而是包含了混合的unicode编码以及已经用utf-8编码之后的字符串。
    # print('%s'%json.dumps(movies,sort_keys=True,indent=4,separators=(',',':')))

    # 如下写法：让中文可展示
    print(json.dumps(movies,ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':')))