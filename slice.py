#切片slice函数，支持切片的有列表、元组、字符串等
#slice(起始位置，结束位置，每步的长度)，步长为1时可默认不写
val = 'maizixueyuan666'

#构造slice保存为一个变量
s = slice(1,5,1)
val[s]
print(val[s])
s = slice(1,5,2)
print(val[s])

#切片操作原型，sequence[起始位置：结束位置：步长]，sequence是支持切片操作的序列对象
print(val[1:5:2])
print(val[2])
print(val[0])
print(val[1:7])

#用：,前后可超过最大值，可以省略，表示最大值
print(val[-100:700]) 
print(val[::]) 
print(val[:9:]) 
print(val[::2]) 

#如果第一个数比第二个数大，同时步长仍为正数，则取不出值，必须步长定义为负数
#此时显示结果为倒序
print(val[3:1]+'*')
print(val[3:1:-1]+'*')

print(val[-1:-7:1]+'*')
print(val[-1:-7:-1]+'*')

#列表和元组都支持切片