#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/29 23:02
# @Author  : bingka.wang 
# @Email   : wangbingka@126.com

import time

def sleep():
    start_time = time.time()
    time.sleep(1)
    end_time =time.time()
    use_time = end_time -start_time
    print(use_time)


def time_dec(f):
    def wrap(*args,**kwargs):
        start_time = time.time()
        # time.sleep(1)
        f(*args,**kwargs)
        end_time =time.time()
        use_time = end_time -start_time
        print(use_time)
    return wrap

def sleep(n):
    time.sleep(n)

sleep = time_dec(sleep)
sleep(1)

@time_dec
def method1(self):
    fbnq_list = [1,1]
    if self == 1:
        return [1]
    elif self == 2:
        return [1,1]
    else:
        i = 0
        while i < int(self)-2:
            a = fbnq_list[i]+fbnq_list[i+1]
            fbnq_list.append(a)
            i +=1
        return fbnq_list

@time_dec
def method2(self):
    fbnq_list = [1,1]
    if self == 1:
        return [1]
    elif self == 2:
        return [1,1]
    else:
        for i in  range(int(self)-2):
            a = fbnq_list[i]+fbnq_list[i+1]
            fbnq_list.append(a)
        return fbnq_list



#此方法严重缺陷，递归层数有限制：
#不断查询，也会非常慢
def fibo(self):
    if self == 1:
        return 1
    elif self == 2:
        return 1
    else:
        return fibo(self-1)+fibo(self-2)

@time_dec
def method3(self):
    fbnq_list = []
    for i in range(1,int(self)+1):
        fbnq_list.append(fibo(i))
    return fbnq_list

print(method3(20))


def fibo3(self,fibo_dict):
    #缓存命中的时候
    if fibo_dict.get(self):
        return fibo_dict.get(self)
    if self == 1:
        return 1
    elif self == 2:
        return 1
    else:
        data = fibo3(self-1,fibo_dict)+fibo3(self-2,fibo_dict)
        #生成缓存
        fibo_dict.update({self:data})
        return data

@time_dec
def method4(self):
    fbnq_list = []
    fibo_dict = {}
    for i in range(1,int(self)+1):
        fbnq_list.append(fibo3(i,fibo_dict))
    return fbnq_list

print(method1(100000))
print(method2(100000))
print(method4(100000))


if __name__ == '__main__':
    # sleep = time_dec(sleep)
    sleep(2)