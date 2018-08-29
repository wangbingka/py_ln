#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time :  2018/8/27 21:31
# @Author: Bingka.wang
# @Email:  wangbingka@126.com


import requests
import urllib.request
import os
import threading

'''
下载百度的国家地理图片：
1、使用参数，发送请求，返回Imgs

'''

# 空列表，所有待下载的Url列表，多线程下载中会使用到
gImageList = []

# 条件控制多线程
gCondition = threading.Condition()

# 定义生产者
class Producer(threading.Thread):
    def run(self):
        global gImageList
        global gCondition

        print('%s:started'%threading.current_thread())

        # 获取图片对应的Url列表
        imgs = download_wallpaper_list()



        # 对条件进行上锁，以便进行操作
        gCondition.acquire()

        # 将对应的url放入对应多线程的列表中

        while True:
            # 上锁
            gCondition.acquire()
            print('{}:trying to download from pool.pool size is {}'.format(threading.current_thread(),len(gImageList)))

            # 当列表中是空的时候，等待，然后不断的尝试获取列表不等于0的时刻
            while len(gImageList)  == 0:
                gCondition.wait()
                print('{}:waken up. pool size is {}'.format(threading.current_thread(),len(gImageList)))
            url = gImageList.pop()
            gCondition.release()
            _download_image(url)

        for i in imgs:
            if 'downloadUrl' in i:
                gImageList.append(i['downloadUrl'])
        print('%s:produce finished. left:%d'%(threading.current_thread(),len(gImageList)))

        # 通知消费者
        gCondition.notify_all()

        # 解锁，把钥匙放回，释放
        gCondition.release()

class Consumer(threading.Thread):
    def run(self):
        print('%s:started' % threading.current_thread())

        # 循环运行获取图片列表,下载数据
        while True:
            global gImageList
            global gCondition

            # 上锁
            gCondition.acquire()
            print('{}:trying to download from pool.pool size is {}'.format(threading.current_thread(),len(gImageList)))

            # 当列表中是空的时候，等待，然后不断的尝试获取列表不等于0的时刻
            while len(gImageList)  == 0:
                gCondition.wait()
                print('{}:waken up. pool size is {}'.format(threading.current_thread(),len(gImageList)))
            url = gImageList.pop()
            gCondition.release()
            _download_image(url)


def _download_image(url, folder='image'):
    print('downloading %s' % url)
    if not os.path.isdir(folder):
        os.mkdir(folder)

    def _fname():
        return os.path.join(folder, os.path.split(url)[1])

    '''
    urlretrieve()方法直接将远程数据下载到本地。
    urlretrieve(url, filename=None, reporthook=None, data=None)

    1•参数filename指定了保存本地路径（如果参数未指定，urllib会生成一个临时文件保存数据。）
    2•参数reporthook是一个回调函数，当连接上服务器、以及相应的数据块传输完毕时会触发该回调，我们可以利用这个回调函数来显示当前的下载进度。
    3•参数data指post导服务器的数据，该方法返回一个包含两个元素的(filename, headers) 元组，filename 表示保存到本地的路径，header表示服务器的响应头

    '''
    urllib.request.urlretrieve(url, _fname())


def download_wallpaper_list():
    url = 'http://image.baidu.com/data/imgs'
    session = requests.session()

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
        }
    session.headers.update(headers)
    params = {
        'pn': 0,
        'rn': 18,
        'col': '壁纸',
        'tag': '国家地理',
        'tag3': '',
        'width': 1960,
        'height': 1200,
        'ic': 0,
        'ie': 'utf8',
        'oe': 'utf-8',
        'image_id': '',
        'fr': 'channel',
        'p': 'channel',
        'from': 1,
        'app': 'img.browse.channel.wallpaper',
        't': '0.917075356379357',
    }
    r = session.get(url, params=params)
    # print(r.json())
    imgs = r.json()['imgs']

    print('%s:totally %d images'%(threading.current_thread(),len(imgs)))
    return imgs

if __name__ == '__main__':
    # download_wallpaper()
    Producer().start()

    for i in range(10):
        Consumer().start()