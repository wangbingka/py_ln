#字典的声明
a = {}
print(type(a))
a = dict()
print(type(a))

a = {'a':1,'b':2}

#访问字典中的值
print(a['a'])

#修改字典中的值
a['a'] = 10
print(a['a'])
#删除字典中的值
del a['a']
print(a)
#新增元素到字典
a['c']=11
print(a)
#计算字典长度，可以用len函数
print(len(a))
#字典的键key不可变，例如元祖可作为Key,但列表不可
a[(123,)] = '123'
print(a)

#集合的定义
s = {1,2,3}
print(type(s))
s = set()
print(type(s))

#集合的修改,新增
s.add('abc')
print(s)
#update，自动拆分单个字符
s.update('123')
print(s)

#集合的删除
s.remove('abc')
print(s)

#集合的交集
m = set()
m.update('345')
print(s&m)
#集合的并集
print(s|m)
#集合的差集
print(s-m)
print(m-s)