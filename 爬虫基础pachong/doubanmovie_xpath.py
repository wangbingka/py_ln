#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/22  17:58
# @Author  : bingka.wang 
# @Email   : wangbingka@126.com

import requests
from lxml import html
from write_movie_data import *
from read_data import *

#输入电影名，获取电影推荐对应的id
def search_movie_id_by_name(name):

    #最简单的防止反爬虫
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    r = requests.get('https://movie.douban.com/j/subject_suggest?q={}'.format(name),headers=headers)

    # print(r) #返回的是相应类型，类似200
    print(r.text)
    rep = r.json()[0]
    return  rep['id']

def search_movie_by_id(movie_id):
    #输入电影的id，获取电影的展示链接

    url = 'https://movie.douban.com/subject/{}/?from=showing'.format(movie_id)
    r= requests.get(url)

    #r.text是xml结构，可以打印查看
    # print(r.text)
    tree = html.fromstring(r.text)
    #获取对应xml结构中的节点内容
    movie_tuijian = tree.xpath('//*[@id="recommendations"]/div/dl/dd/a')
    # 获取对应xml结构中的节点中的整个文本内容
    movie_tuijian_name = tree.xpath('//*[@id="recommendations"]/div/dl/dd/a/text()')
    # 获取对应xml结构中的节点中的某个属性
    movie_tuijian_url = tree.xpath('//*[@id="recommendations"]/div/dl/dd/a/@href')
    # print(movie_tuijian)
    # print(movie_tuijian_name)
    # print(movie_tuijian_url)
    # for i in range(0,9):
    #     print(movie_tuijian_name[i]+':'+movie_tuijian_url[i])

    # zip,使两个列表，索引一一对应的组合，形成一个集合，然后再所有集合组成一个大的集合
    movie_list = zip(movie_tuijian_name,movie_tuijian_url)
    return list(movie_list)   #list，将集合转换为列表

def similar_movie_list(similar_movie):
    for m in similar_movie:
        print(m)
        #根据集合中的Url内容，切片取出电影的id
        mid = m[1].split('/')[-2]
        s = search_movie_by_id(mid)
        # print(s)
        write_data(input_movie,m[0]+'-相似指数:3')
        for m1 in s:
            mid1 = m1[1].split('/')[-2]
            s1 = search_movie_by_id(mid1)
            # print(s1)
            write_data(input_movie,'\t'+m1[0]+'-相似指数:2')
            for m2 in s1:
                write_data(input_movie,'\t'+'\t'+m2[0]+'-相似指数:1')

input_movie = '蛮荒故事'
create_write_data(input_movie)

m_id= search_movie_id_by_name(input_movie)
similar_movie = search_movie_by_id(m_id)
similar_movie_list(similar_movie)

print(similar_movie_count(input_movie))
for i in similar_movie_count(input_movie):
    write_data(input_movie + '相似电影推荐排名', str(i))


#输出类似的推荐电影

#网页、微信、小程序、api