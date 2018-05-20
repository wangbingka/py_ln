#python面向对象概念
#
# classs，名称、变量、函数
#面向对象四要素:抽象，封装，继承，多态

#类的定义

#类的名称，Myclass
class Myclass:
	#公有变量 public :类本身，类的实例，其他外部类，子类都可以访问
	#类的变量i,是12345
	i = 12345
	name = 'sundy'

	#私有变量 private:类本身能够访问
	__age = 18

	#保护类变量，protected:类的子类，类的实例可以访问，外部能访问
	_size = 20

	#类的函数，是return 'hello world'
	def f(self):
		return 'hello world'

x = Myclass()

print('myclass 类的属性为',x.i)
print('myclass function is',x.f())
#print('private:'x.__age)，私有变量，实例无法访问
print('protected:',x._size)

#类的实例
#实例：类的具体化：类：可乐，具体的某一罐可乐：one 可乐
#
class Cola():
	name = 'Cola'
	#实例方法，普通方法
	def opencole(self):
		print('open cola')

	#构造方法（函数）
	def __init__(self,aname):
		self.name = aname

	#类方法,地址是固定的，类可以继承，可以被修改和调整
	@classmethod
	def test2(cls):
		print('this is a class method')

	#静态方法，子类不能继承，类似一个变量，全局
	@staticmethod
	def test3():
		print('this is a static method')


#deskcola = Cola()
#watercola = Cola()
#print(deskcola.name)
newcole = Cola('Sundycola')
print(newcole.name)

#类的变量

#类的方法
Cola.test2()
Cola.test3()

#类的继承

class Cocacola(Cola):
	color = 'red'
	name = 'Cocacola'
	def opencole(self):
		print('open coca cola')

class Pepsicola(Cola):
	color = 'blue'
	name = 'Pepsicola'
	def opencola(self):
		print('open pepsi cola')

aCoca = Cocacola('Cocacola')
print(aCoca.name)
print(aCoca.color)
print(aCoca.opencole())


bCole = Pepsicola('Pepsicola')

print(bCole.name)
print(bCole.color)
print(bCole.opencola())

#判别对象类型
print(type(122))

print(type(122.0))

print(type('sundy'))

print(type(Cola))