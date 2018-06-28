#!usr/bin/python
#coding:utf-8
#author:bingka.wang

import random
import string
import os


#随机n个有不同小写字母组成的字符串
    # def ran_str(self):
    #     a = set()
    #     c = []
    #     e = string.ascii_lowercase
    #     count1 = 0
    #     f = ''
    #     for i in e:
    #         c.append(i)
    #     while True and count1 < self:
    #         d = random.choice(c)
    #         c.remove(d)
    #         a.add(d)
    #         count1 +=1
    #     for i in a:
    #         f +=i
    #     return f
    # print(ran_str(26))

#随机生成从1到100的文件名，里面的内容分别为1-100，101-200，...，9901到10000.

for i in range(1,101):
    b = str(os.getcwd())
    c = b.replace('\\', '/')
    a = r'%s/txt1' % c
    #判断此对应目标文件夹是否存在
    if os.path.isdir(a):
        pass
    else:
        #创建目标文件夹
        os.mkdir(r'txt1/')
    f = open('%s/txt1/%d.txt'%(c,i), 'a+')
    for i in range(i*100-99,i*100):
        f.write('%d\n'%i)
    f.close()
