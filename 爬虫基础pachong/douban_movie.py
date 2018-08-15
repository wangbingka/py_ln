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
            movie['score'] = _attr(attrs,'data-score')
            movie['director'] = _attr(attrs,'data-director')
            movie['actors'] = _attr(attrs,'data-actors')
            movie['duration'] = _attr(attrs, 'data-duration')
            # print(movie)
            self.movies.append(movie)
            # print(self.movies)
            # print(self.movies)
            # print('%(title)s|%(score)s|%(movie)s|%(actors)s|%(duration)s'%movie)

def nowpalying_movies(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'}
    reg = urllib.request.Request(url,headers=headers)
    s = urllib.request.urlopen(reg)
    parser = MovieParser()
    # print(s.read().decode('utf-8'))
    parser.feed(s.read().decode('utf-8'))
    s.close()
    return parser.movies

if __name__ == '__main__':
    url = 'https://movie.douban.com/'
    movies = nowpalying_movies(url)
    print(movies)

    import json
    print('%s'%json.dumps(movies,sort_keys=True,indent=4,separators=(',',':')))