#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time :  2018/8/24 21:19
# @Author: Bingka.wang
# @Email:  wangbingka@126.com

import requests
import urllib.request
import os

'''
下载百度的国家地理图片：
1、使用参数，发送请求，返回Imgs

'''

def _download_imaage(url,folder = 'image'):
    print('downloading %s' % url)
    if not os.path.isdir(folder):
        os.mkdir(folder)
    def _fname():
        return os.path.join(folder,os.path.split(url)[1])

    '''
    urlretrieve()方法直接将远程数据下载到本地。
    urlretrieve(url, filename=None, reporthook=None, data=None)

    1•参数filename指定了保存本地路径（如果参数未指定，urllib会生成一个临时文件保存数据。）
    2•参数reporthook是一个回调函数，当连接上服务器、以及相应的数据块传输完毕时会触发该回调，我们可以利用这个回调函数来显示当前的下载进度。
    3•参数data指post导服务器的数据，该方法返回一个包含两个元素的(filename, headers) 元组，filename 表示保存到本地的路径，header表示服务器的响应头
    
    '''
    urllib.request.urlretrieve(url,_fname())

def download_wallpaper():
    url = 'http://image.baidu.com/data/imgs'
    session = requests.session()

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
}
    session.headers.update(headers)
    params = {
        'pn': 0,
        'rn': 18,
        'col': '壁纸',
        'tag': '国家地理',
        'tag3':'',
        'width':1960,
        'height': 1200,
        'ic': 0,
        'ie':'utf8',
        'oe':'utf-8',
        'image_id':'',
        'fr':'channel',
        'p': 'channel',
        'from':1,
        'app': 'img.browse.channel.wallpaper',
        't': '0.917075356379357',
    }
    r = session.get(url,params=params)
    print(r.json())
    imgs = r.json()['imgs']
    for i in  imgs:
        print(i)
        if 'downloadUrl' in i:
            print(i['downloadUrl'])
            _download_imaage(i['downloadUrl'])



if __name__ == '__main__':
    download_wallpaper()
