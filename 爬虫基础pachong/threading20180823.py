#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time :  2018/8/23 22:59
# @Author: Bingka.wang
# @Email:  wangbingka@126.com

import threading
import time
import random

def worker_func():
    print('worker thread is started at %s'%threading.current_thread())
    random.seed()
    time.sleep(random.random())
    print('')
