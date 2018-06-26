#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/26 23:14
# @Author  : bingka.wang 
# @Email   : wangbingka@126.com

import time

def time_it(fn):
    print('Time_it is executed.')
    def new_fn(*args):
        start = time.time()
        result = fn(*args)
        end = time.time()
        duration = end -start
        print('%s seconds are consumed in executing function:%s%r'\
            %(duration,fn.__name__,args))
        return result
    return new_fn

@time_it
def acc1(strat,end):
    s = 0
    for i in range(start,end):
        s +=i
    return s

def acc2(strat,end):
    s = 0
    for i in range(start,end):
        s +=i
    return s

print(acc1)
print(acc2)

if __name__ == '__main__':
    acc1(10,1000000)