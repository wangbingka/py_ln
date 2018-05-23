#python支持的运算符
#算术运算符（+、-、*、/、%返回余数、**、//(除法取整数,但是若为-3.5则为-4)）
print(2**3)
print(9/4)
print(9//4)

#比较(关系)运算符，(==等于，！=不等于，<,>,>=,<=)，'<>'python3已经被抛弃
print(1!='1')
print(1=='1')

#赋值运算(=,+=,-=,*=,/=)
a=10
print(a)
a+=10
print(a)
b=60
print(b)
b-=10
print(b)

#逻辑运算符(and,or,not)
print(1==1 and 1=='1')
print(1==1 or 1=='1')
print(not 1=='1')

#位运算符(&、|、^、~、<<、>>)
#成员运算符（in、not int)
print(3 in [1,2,3])
print('3'  not in [1,2,3])

#身份运算符(is、is not)
p = None
print(p is None)
q = 123
print(q  is not '123')