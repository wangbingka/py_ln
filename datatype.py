#六大基本数据类型
#number,数值
#Sring,字符串
#List,列表
#Tuple,元组
#Sets,集合
#Dictionary,字典

#数字类型：
#int整数，float浮点数即小数，bool或真或假类型，complex复数

a = 100
print(a)
print(type(a))

f = str(a)
print(f)
print(type(f))

h = int(f)
print(h)
print(type(h))

g = float(a)
print(g)
print(type(g))

b = 10.1
print(b)
print(type(b))
i = int(b)
print(i)
print(type(i))

c = True
print(c)
print(type(c))

d = False
print(d)
print(type(d))

e= 3+ 2j
print(e)
print(type(e))

j = """我是一个很长的字符换，
我现在要换行了
的发货的房价的规范 """
print(j)
m = """我是一个很长的字符换，\n我现在要换行了\n的发货的房价的规范 """
print(m)

#打印出表示换行符的"\n"
n = """我是一个很长的字符换，\\n我现在要换行了\\n的发货的房价的规范 """
print(n)
#用"r"转译特殊字符
o = r"""我是一个很长的字符换，\n我现在要换行了\n的发货的房价的规范 """
print(o)

k = '我是某某某'
l = '你是谁'
print(k+','+l)