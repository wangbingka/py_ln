#!usr/bin/python
#coding:utf-8
#author:bingka.wang

import urllib
import urllib.request
from html.parser  import HTMLParser

class MovieParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.movies = []
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


def nowpalying_movies(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'}
    reg = urllib.request.Request(url,headers=headers)
    s = urllib.request.urlopen(reg)
    parser = MovieParser()
    # print(s.read().decode('utf-8'))
    parser.feed(s.read().decode('utf-8'))
    s.close()
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
    # print(json.dumps(movies,ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':')))