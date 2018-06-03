#!usr/bin/python
#coding:utf-8
#author:bingka.wang

class Cola():
    name = 'Cola'
    #self代表类的实例，实例方法：普通方法
    def openCola(self):
        print('open cola')
    #构造函数，默认没有参数,改变公有变量默认的值
    def __init__(self):
        self.name = '名字'
    #类方法,cls代表当前类本身
    @classmethod
    def test2(cls):
        print('this is a class method')
    #静态方法，子类不能继承，类似静态的全局变量
    @staticmethod
    def test3():
        print('this is a static method')
newCola = Cola()
newCola.name = 'SundyCola'
print(newCola.name)
Cola.test2()
Cola.test3()

#类的继承
class CocaCola(Cola):
    color = 'red'
    name = 'CocaCola'
    def openCola(self):
        print('open Cocala')
    #子类想要继续使用父类的构造方法
    # 有两种方法能达到这个目的：调用超类构造方法的未绑定版本，或者使用super函数。
    def __init__(self):
        Cola.__init__(self)
        self.manfu = '可口可乐公司'
class PepsiCola(Cola):
    color = 'blue'
    name = 'PepsiCola'
    def openCola(self):
        return 'open PepsiCola'
    def __init__(self):
        super(PepsiCola, self).__init__()
        self.manfu = '百事可乐公司'

#子类可继承父类的变量和函数，但也可以重新定义
aCola =CocaCola()
aCola.name = 'CocaCola'
aCola.manfu = '可口可乐公司厂1'
print(aCola.name)
print(aCola.color)

bCola = PepsiCola()
bCola.name = 'PepsiCola1'
bCola.manfu = '百事可乐公司厂2'
print(bCola.name)
print(bCola.color)

cCola = PepsiCola()

print(aCola.openCola())
print(bCola.openCola())
print(aCola.manfu)
print(bCola.manfu)
print(cCola.manfu)


#type,查对象的数据类型
print(type(12345))
print(type('sundy'))
print(type(Cola))
