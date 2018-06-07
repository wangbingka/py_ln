#!usr/bin/python
#coding:utf-8
#author:bingka.wang

#  F(n)=F(n-1)+F(n-2)（n>=2，n∈N*）

#方法1
# list1 = [1, 1]
# count1 =3
# for i in range(2,100000):
#     if i == list1[count1-3] + list1[count1-2]:
#         list1.append(i)
#         count1 += 1
#     else:
#         continue
# print(list1)

# 方法2
list1 = [1, 1]
count1 =3
i = 0
while i < 100000:
    if i == list1[count1-3] + list1[count1-2]:
        list1.append(i)
        count1 += 1
print(list1)

