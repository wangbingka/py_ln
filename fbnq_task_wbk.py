#!usr/bin/python
#coding:utf-8
#author:bingka.wang

#  F(n)=F(n-1)+F(n-2)（n>=2，n∈N*）

#方法1，速度偏慢，算到第40个，需要几秒钟了,
# 所以如果真的要使用，我觉得可能需要先集中资源，跑出一部分结果数据，方便直接调用
# def fbnq1(self):
#     list1 = [1, 1]
#     count1 =3
#     for i in range(2,1000000000):
#         if i == list1[count1-3] + list1[count1-2] and count1 < self:
#             list1.append(i)
#             count1 += 1
#         elif i == list1[count1-3] + list1[count1-2] and count1 == self:
#             list1.append(i)
#             break
#         else:
#             continue
#     print(list1)
#     return list1[self-1]
# print(fbnq1(40))


# 方法2
def fbnq2(self):
    list1 = [1,1]
    count1 =3
    i = 1
    while True and i < 100000000000:
        i +=1
        if i == list1[count1-3] + list1[count1-2] and count1 < self:
            list1.append(i)
            count1 += 1
        elif i == list1[count1-3] + list1[count1-2] and count1 == self:
            list1.append(i)
            break
        else:
            continue
    print(list1)
    return list1[self-1]
print(fbnq2(35))

