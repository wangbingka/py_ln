
# !/usr/bin/env python




# coding=utf-8




import os




import urllib









def cbk(a ,b ,c):




    '''回调函数




    @a:已经下载的数据块




    @b:数据块的大小




    @c:远程文件的大小




    '''




    per =100.0 * a * b /c




    if per >100:




        per =100




    print '%.2f%%' % per









ur l ='http://www.baidu.com'




di r =os.path.abspath('.')




work_path =os.path.join(dir ,'baidu.html')




urllib.urlretrieve(url ,work_path ,cbk)
