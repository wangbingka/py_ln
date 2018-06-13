#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/13 22:06
# @Author  : bingka.wang 
# @Email   : wangbingka@126.com


class Menpiao:
    price = 100
    def __init__(self,aud_num,child_num,iswkd):
        self.aud_num = aud_num
        self.child_num = child_num
        self.iswkd = iswkd
        self.total_price = self.count_price()
        print(self.total_price)
    def count_price(self):
        if self.iswkd == 'yes':
            total1 = '您应支付的总金额：'+\
                     str((self.aud_num*self.price+self.child_num*self.price*0.5)*1.2)
        elif self.iswkd == 'no':
            total1 = '您应支付的总金额：' + \
                  str((self.aud_num * self.price + self.child_num * self.price * 0.5))
        else:
            total1 = '很抱歉您的输入有误。'
        return total1
print('欢迎光临迪士尼。')
aud_num = int(input('请输入大人的数量：'))
chlid_num = int(input('请输入儿童的数量：'))
iswkd = input('请问是否周末来？ yes/no:')
a = Menpiao(aud_num,chlid_num,iswkd)

