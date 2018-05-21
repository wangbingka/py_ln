#列表的使用
#1、列表的声明
a = [1,2,3,4,5,'a','b']
print(a)
i = []
print(i)
print(type(i))
i =list()
print(i)
print(type(i))
#2、访问列表中的数据
print(a[0])
print(a[-2])
print(a[0:4])
print(a[:4])
#更新列表中的数据
print(a[5])
#改动列表中的数据
a[5] = 'c'
print(a[5])
#给列表增加元素
a.append('g')
print(a)
#删除列表中的元素
del a[0]
print(a)
a.remove('g')
print(a)
#计算列表的长度
print(len(a))
#列表的计算，加法+,乘法*
b = [10,17,'e']
print(a+b)
print(b*2)

#元祖的使用
a = (1,2,3)
print(a)
#元祖最后建议加个'，',否则容易改变元祖的类型
a = (1)
print(a)
print(type(a))
a = (1,)
print(a)
print(type(a))
#元祖的访问可以和列表类似
a = (1,2,3,'e','f')
print(a[2])
#元祖的加法和乘法与列表一致。
#元祖不被允许修改数据，包括更新、新增，删除
#
# for 循环
a = [1,2]
b = 'hello world'
c = [i for i in b]
print(c)