#!usr/bin/python
#coding:utf-8
#author:bingka.wang

class Cola():
    name = 'Cola'
    #self代表类的实例，实例方法：普通方法
    def openCola(self):
        print('open cola')
    #构造函数，默认没有参数,改变公有变量默认的值
    def __init__(self,aname):
        self.name = aname
    #类方法,cls代表当前类本身
    @classmethod
    def test2(cls):
        print('this is a class method')
    #静态方法，子类不能继承，类似静态的全局变量
    @staticmethod
    def test3():
        print('this is a static method')

newCola = Cola('SundyCola')
print(newCola.name)
Cola.test2()
Cola.test3()

#类的继承
class CocaCola(Cola):
    color = 'red'
    name = 'CocaCola'
    def openCola(self):
        print('open Cocala')
class PepsiCola(Cola):
    color = 'blue'
    name = 'PepsiCola'
    def openCola(self):
        return 'open PepsiCola'

#子类可继承父类的变量和函数，但也可以重新定义
aCola =CocaCola('CocaCola')
print(aCola.name)
print(aCola.color)
print(aCola.openCola())
bCola = PepsiCola('PepsiCola')
print(bCola.name)
print(bCola.color)
print(aCola.openCola())
print(bCola.openCola())

#type,查对象的数据类型
print(type(12345))
print(type('sundy'))
print(type(Cola))
