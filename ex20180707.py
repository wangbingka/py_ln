#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/7
# @Author  : bingka.wang
# @Email   : wangbingka@126.com


# *args：（表示的就是将实参中按照位置传值，多出来的值都给args，且以元祖的方式呈现）
def foo(x,*args):
    print('foo')
    print(x)

    print(args)
foo(1,2,3,4,5) #其中的2,3,4,5都给了args

# 当args与位置参数和默认参数混用的情况下：（注意三者的顺序）

# 示例一、（三者顺序是:位置参数、默认参数、*args）

def foo1(x, y=1, *args):
    print('foo1')
    print(x)
    print(y)
    print(args)

foo1(1, 2, 3, 4, 5)  # )#其中的x为1，y=1的值被2重置了，3,4,5都给了args

# 1、从形参的角度来看：

def foo2(*args):   #其实这一操作相当于def foo（a,b,c,d,e):
    print('foo2')
    print(args)
foo2(1,2,3,4,5)   #其中的1，2,3,4,5都按照位置传值分别传给了a,b,c,d,e

# 2、从实参的角度来看：

def foo3(x, y, z):
    print('foo3')
    print(x)
    print(y)
    print(z)
foo3(*(1, 2, 3))  # 其中的*（1,2,3）拆开来看就是：foo（1,2,3），都按照位置传值分别传给了x,y,z


# **kwargs：（表示的就是形参中按照关键字传值把多余的传值以字典的方式呈现）
def foo4(x,**kwargs):
    print('foo4')
    print(x)
    print(kwargs)
foo4(1,y=1,a=2,b=3,c=4)#将y=1,a=2,b=3,c=4以字典的方式给了kwargs

# 关于**kwargs与位置参数、*args、默认参数混着用的问题：（注意顺序）
# 位置参数、*args、**kwargs三者的顺序必须是位置参数、*args、**kwargs，不然就会报错：


def foo5(x,*args,**kwargs):
    print('foo5')
    print(x)
    print(args)
    print(kwargs)
foo5(1,2,3,4,y=1,a=2,b=3,c=4)

# 错误示例：（由于顺序错误）
    # def foo(x,**kwargs,*args):
    #     print(x)
    #     print(kwargs)
    #     print(args)
    # foo(1,y=1,a=2,b=3,c=4,2,3,4)

# 位置参数、默认参数、**kwargs三者的顺序必须是位置参数、默认参数、**kwargs，不然就会报错：

def foo6(x,y=1,**kwargs):
    print('foo6')
    print(x)
    print(y)
    print(kwargs)
foo6(1,a=2,b=3,c=4)#将1按照位置传值给x，y按照默认参数为1，a=2,b=3,c=4以字典的方式给了kwargs
foo6(1,2,a=2,b=3,c=4)

# 其中关于**，可以从2个角度来看（需要拆分来看）：
# 1、从形参的角度来看：
def foo7(**kwargs): #其实就是相当于def foo(y,a,b,c)
    print('foo7')
    print(kwargs)
foo7(y=1,a=2,b=3,c=4)
# foo7(1,y=1,a=2,b=3,c=4),会如果传入的非设置参数，会报错

#2、从实参的角度来看：
def foo8(a,b,c,d):
    print('foo8')
    print(a)
    print(b)
    print(c)
    print(d)
foo8(**{"a":2,"b":3,"c":4,"d":5})  #**{"a":2,"b":3,"c":4,"d":5}是将字典里的每个值按照关键字传值的方式传给a,b,c,d
# foo8(**{"y":2,"b":3,"c":4,"d":5}) 如果输入的字典key，不在设置范围内，也会报错


def foo8_1(a,b,c,d=1):
    print(foo8_1)
    print(a)
    print(b)
    print(c)
    print(d)
foo8_1(**{"a":2,"b":3,"c":4}) #**{"a":2,"b":3,"c":4}是将字典里的每个值按照关键字传值的方式传给a,b,c；d依旧按照默认参数
foo8_1(**{"a":2,"b":3,"c":4,"d":5}) #如果d再次输入一个对应值，会更改原有的默认值
