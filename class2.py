#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/10 22:54
# @Author  : bingka.wang 
# @Email   : wangbingka@126.com

# 案例1
# class MyClass:
#     i = 12345
#     def f(self):
#         return 'hello wordl'
#     def __init__(self,realpart,imagpart):
#         self.r = realpart
#         self.i = imagpart
#
# x = MyClass(3.5,-4.0)
# print(x.i)
# print(x.f())
# print(x.r,x.i)

# 案例2
class Test1:
    def prt(self):
        print(self)
        print(self.__class__)
t = Test1() #类的实例，当前对象的物理存储地址
t.prt()  #代表这个类本身

#类的定义
class People:
    #类属性，只由类自身决定，并且可通过类修改
    name = ''
    age = 0
    total = 1000
    #私有属性，只有类内部能访问，外部无法访问
    __weight = 0
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
        self.total +=1
    def speak(self):
        print('{}说:我{}岁'.format(self.name,self.age))
        print(p1.__weight)  #类内部可以访问私有变量
p1 = People('jack',30,'50kg')
p1.speak()
# print(p1.__weight) #类外部无法访问私有变量
print(p1.total)
#修改类属性
People.total = 2000
print(People.total)
#但是之前已经被定义的属性不会被再次修改
print(p1.total)
p2 = People('amy',24,'45kg')
print(p2.total)


# 单继承示例
class Student(People):
    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类的构函
        # people.__init__(self, n, a, w)
        #更好的继承父类的构造方法
        super().__init__(n,a,w)
        self.grade = g

    # 覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %s 年级" % (self.name, self.age, self.grade))


# 另一个类，多重继承之前的准备
class Speaker():
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s" % (self.name, self.topic))


# 多重继承，可以从多个父类中继承
class Sample(Speaker, Student):
    a = ''

    def __init__(self, n, a, w, g, t):
        Student.__init__(self, n, a, w, g)
        Speaker.__init__(self, n, t)


p3 = Sample('tom',18,'50kg','高三','每个人都有一个梦想')
print(p3.speak())
#强制调用父类中已被重新覆盖的方法
super(Sample,p3).speak()
super(Student,p3).speak()


#类的私有方法
class Site:
    def __init__(self,aname,aurl):
        self.name = aname
        self.url = aurl
    def who(self):
        print('name',self.name)
        print('url',self.url)
    def __foo(self):
        print('这是私有方法')
    def foo(self):
        print('这是公有方法')
        self.__foo()  #私有方法，类内部可以访问
x  = Site('菜鸟变成','www.runoob.com')
x.who()
x.foo()
# x__foo() 私有方法，在类外部不能访问

#类的专有方法
# __init__ : 构造函数，在生成对象时调用
# __del__ : 析构函数，释放对象时使用
# __repr__ : 打印，转换
# __setitem__ : 按照索引赋值
# __getitem__: 按照索引获取值
# __len__: 获得长度
# __cmp__: 比较运算
# __call__: 函数调用
# __add__: 加运算
# __sub__: 减运算
# __mul__: 乘运算
# __div__: 除运算
# __mod__: 求余运算
# __pow__: 乘方

# 运算符重载
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
print(v1+v2)


#关于类的实例的打印
# __repr__和__str__这两个方法都是用于显示的，__str__是面向用户的，而__repr__面向程序员。
#
# •打印操作会首先尝试__str__和str内置函数(print运行的内部等价形式)，它通常应该返回一个友好的显示。
# •__repr__用于所有其他的环境中：用于交互模式下提示回应以及repr函数，如果没有使用__str__，会使用print和str。它通常应该返回一个编码字符串，可以用来重新创建对象，或者给开发者详细的显示。
class Test:
    def __init__(self, value='hello, world!'):
        self.data = value

# >>> t = Test()
# >>> t
# <__main__.Test at 0x7fa91c307190>
# >>> print t
# <__main__.Test object at 0x7fa91c307190>

# 看到了么？上面打印类对象并不是很友好，显示的是对象的内存地址
# 下面我们重构下该类的__repr__以及__str__，看看它们俩有啥区别

# 重构__repr__
class TestRepr(Test):
    def __repr__(self):
        return 'TestRepr(%s)' % self.data

# 重构__repr__方法后，不管直接输出对象还是通过print打印的信息都按我们__repr__方法中定义的格式进行显示了
tr = TestRepr()
print(tr)


# 你会发现，直接输出对象ts时并没有按我们__str__方法中定义的格式进行输出，而用print输出的信息却改变了
# 重构__str__
class TestStr(Test):
    def __str__(self):
        return '[Value: %s]' % self.data
    __repr__ = __str__ #将两者等同，可重复使用。
ts = TestStr()
print(ts)
