#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/30 23:11
# @Author  : bingka.wang 
# @Email   : wangbingka@126.com

#python 面向对象概念
# 对象，是对现实社会的对象
#class
#面向对象四要素：抽象，封装，继承，多态

#类的定义
class Myclass:
    i = 12345
    def f(self):
        return 'hello world'
x = Myclass()

print('myclass 类的属性为',x.i)
print('myclass function is',x.f())

#类的实例，类的具体化：类：可乐， one 可乐
class Cola():
    name = 'Cola'
deskCola = Cola() #deskCola 是对Cola的一次拷贝
print(deskCola.name)
waterCola = Cola() #再一次拷贝,但和deskCola不一样，存储地址也不一样

#类的变量
class Myclass:
    # public 变量，公有变量，类本身，类的实例，其他外部类，外部类都可以访问
    i = 12345
    name = 'sundy'

    # private，私有变量，类本身能访问，其他都不能访问
    __age = 18

    # protected：保护类变量，类的子类，类的实例可以访问
    _size = 20


    def f(self):
        return 'hello world'
x = Myclass()

print('myclass 类的属性为',x.i)
print('myclass function is',x.f())
# print('private:',x.__age)
print('private:',x._size)




