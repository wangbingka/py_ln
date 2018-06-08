#!usr/bin/python
#coding:utf-8
#author:bingka.wang

#  F(n)=F(n-1)+F(n-2)（n>=2，n∈N*）



# 方法1
# def fbnq2(self):
#     list1 = [1,1]
#     count1 =3
#     i = 1
#     while True and i < 100000000000:
#         if i == list1[count1-3] + list1[count1-2] and count1 < self:
#             list1.append(i)
#             count1 += 1
#         elif i == list1[count1-3] + list1[count1-2] and count1 == self:
#             list1.append(i)
#             break
#         else:
#             continue
##返回整个序列数，需要写两个
#     return list1
##返回第n个序列数
#     return list1[self-1]
# print(fbnq2(35))


#方法1的优化版，如果只取第n个序列数时，不会占用太多内容
# #但这个只能用于第几个序列数，不能直接取数列，取数据列结合后面那个fbnq2_list方法实现
#缺陷，只能取大于等于2以上的，取第1会给出错误结果。
# def fbnq2(self):
#     list1 = [0, 1]
#     count1 = 2
#     while True and count1 <= self-1:
#         i = list1[0] + list1[1]
#         list1.append(i)
#         count1 += 1
#         # list1 = [list1[1],list1[2]] #更新列表方法1，形成新的列表，这样列表中会永远只有两个元素
#         del list1[0] #更新列表方法1，删除第一个元素，这样列表中会永远只有两个元素
#     return list1[1]
# print(fbnq2(1))
# print(fbnq2(2))
# print(fbnq2(3))
# print(fbnq2(4))
# print(fbnq2(5))
# print(fbnq2(100000))
#
# #方法2list
# def fbnq2_list(self):
#     list2 = [0]
#     for i in range(2,self+1):
#         list2.append(fbnq2(i))
#     return list2
# print(fbnq2_list(10))


#尝试改进方法2，使其能够将1以下的也取正确
#缺陷是多进行了一步计算，比如我取第10个值，函数中其实将11个值也计算出来了，
# 之所以这样，因为返回值只有一种，为了兼容第一个序列值为0。同时也为了可以不断取后一个值，也得保证每一步计算的列表中有前两值。
# def fbnq2(self):
#     list1 = [0, 1]
#     for count1 in range(1,self):
#         if self == 1:
#             break
#         elif self >=2 :
#             i = list1[0] + list1[1]
#             list1.append(i)
#             # list1 = [list1[1],list1[2]] #更新列表方法1，形成新的列表，这样列表中会永远只有两个元素
#             del list1[0] #更新列表方法1，删除第一个元素，这样列表中会永远只有两个元素
#         count1 += 1
#     return list1[0]
# print(fbnq2(1))
# print(fbnq2(2))
# print(fbnq2(3))
# print(fbnq2(4))
# print(fbnq2(5))
#
# print(fbnq2(100000))
#
# #方法2list
# def fbnq2_list(self):
#     list2 = []
#     for i in range(1,self+1):
#         list2.append(fbnq2(i))
#     return list2
# print(fbnq2_list(10))

#对方法2使用迭代器取列表
def fbnq2(self):
    list1 = [0, 1]
    for count1 in range(1,self):
        if self == 1:
            break
        elif self >=2 :
            i = list1[0] + list1[1]
            list1.append(i)
            # list1 = [list1[1],list1[2]] #更新列表方法1，形成新的列表，这样列表中会永远只有两个元素
            del list1[0] #更新列表方法1，删除第一个元素，这样列表中会永远只有两个元素
        count1 += 1
    return list1[0]
print(fbnq2(1))
print(fbnq2(2))
print(fbnq2(3))
print(fbnq2(4))
print(fbnq2(5))

print(fbnq2(100000))

iterator1 = iter(str(fbnq2(20)))
for i in iterator1:
    print(i)

#方法2list
# def fbnq2_list(self):
#     list2 = []
#     for i in range(1,self+1):
#         list2.append(fbnq2(i))
#     return list2
# print(fbnq2_list(10))


#方法3，根据网上看到的，进行优化
# def fab(max):
#     n, a, b = 1, 0, 1
#     while n <= max:
#         print(b)
#         a, b = b, a + b
#         n +=1
# fab(5)
#改进
# def fab(max):
#     n, a, b = 1, 0, 1
#     list1 =[]
#     while n <= max:
#         list1.append(b)
#         a, b = b, a + b
#         n +=1
#     return list1
# print(fab(5))
# print(fab(100000)[99999])


# class Fab(object):
#     def __init__(self, max):
#         self.max = max
#         self.n, self.a, self.b = 0, 0, 1
#
#     def __iter__(self):
#         return self
#
#     def next(self):
#         if self.n < self.max:
#             r = self.b
#             self.a, self.b = self.b, self.a + self.b
#             self.n = self.n + 1
#             return r
#         raise StopIteration()
#
# for n in Fab(5):
#     print(n)



