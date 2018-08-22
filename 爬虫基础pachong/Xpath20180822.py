#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time :  2018/8/22 22:50
# @Author: Bingka.wang
# @Email:  wangbingka@126.com


import requests
import ssl
from lxml import etree


ssl._create_default_https_context = ssl._create_unverified_context

session = requests.Session()
for id in range(0, 251, 25):
    URL = 'https://movie.douban.com/top250/?start=' + str(id)
    req = session.get(URL)
    # 设置网页编码格式
    req.encoding = 'utf8'
    # 将request.content 转化为 Element
    root = etree.HTML(req.content)
    # 选取 ol/li/div[@class="item"] 不管它们在文档中的位置

    # // *[ @ id = "content"] / div / div[1] / ol / li[1] / div
    items = root.xpath('//ol/li/div[@class="item"]')
    for item in items:
        # 注意可能只有中文名，没有英文名；可能没有quote简评
        print(item)
        rank, name, alias, rating_num, quote, url = "", "", "", "", "", ""
        try:
            url = item.xpath('./div[@class="pic"]/a/@href')[0]
            rank = item.xpath('./div[@class="pic"]/em/text()')[0]
            title = item.xpath('./div[@class="info"]//a/span[@class="title"]/text()')
            name = title[0].encode('gb2312', 'ignore').decode('gb2312')
            alias = title[1].encode('gb2312', 'ignore').decode('gb2312') if len(title) == 2 else ""
            rating_num = item.xpath('.//div[@class="bd"]//span[@class="rating_num"]/text()')[0]
            quote_tag = item.xpath('.//div[@class="bd"]//span[@class="inq"]')
            if len(quote_tag) is not 0:
                quote = quote_tag[0].text.encode('gb2312', 'ignore').decode('gb2312').replace('\xa0', '')
            # 输出 排名，评分，简介
            print(rank, rating_num, quote)
            # 输出 中文名，英文名
            print(name.encode('gb2312', 'ignore').decode('gb2312'),
                  alias.encode('gb2312', 'ignore').decode('gb2312').replace('/', ','))
        except:
            print('faild!')
            pass
