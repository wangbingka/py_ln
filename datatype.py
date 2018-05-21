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

#格式化字符串，1、%占位符，2，format
p = '张三你好，我是卡卡王，今年18岁'
print(p)
p = '%s你好，我是%s，今年18岁'%('张三','卡卡王')
print(p)
#p = '%s你好，我是%s，今年%d岁'%('张三','卡卡王','18'),会报错
p = '%s你好，我是%s，今年%d岁'%('张三','卡卡王',18)
print(p)
h =  '{},你好,我是{},今年{}岁'.format('张三','卡卡王','18')
print(h)
h =  '{1},你好,我是{0},今年{2}岁'.format('张三','卡卡王','18')
print(h)
h =  '{1},你好,我是{1},今年{2}岁'.format('张三','卡卡王','18')
print(h)
h =  '{1},你好,我是{0},今年{2:d}岁'.format('张三','卡卡王',18)
print(h)

#py3中，'123'和'abc都是str，encode和decode是转换str和bytes数据类型
#py2中,a='123'和b=u'abc'不是同样的类型前者str，后者是unicode，
#可以通过a.encode('gbk')转为str，也可以通过b.decode('gbk')转回
a = 'abc'
b = a.encode('gbk')
print(a)
print(type(a))
print(b)
print(type(b))