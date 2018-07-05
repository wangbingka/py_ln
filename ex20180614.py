#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/13 22:06
# @Author  : bingka.wang 
# @Email   : wangbingka@126.com


class Menpiao:
    price = 100
    def count_price(self):
        aud_num = self.aud_num1()
        child_num = self.child_num1()
        iswkd = self.iswkd1()
        if iswkd == 'yes':
            total1 = '您应支付的总金额：'+\
                     str((aud_num*self.price+child_num*self.price*0.5)*1.2)
        elif iswkd == 'no':
            total1 = '您应支付的总金额：' + \
                  str((aud_num * self.price + child_num * self.price * 0.5))
        else:
            total1 = '很抱歉您的输入有误。'
            print('很抱歉您的输入有误。')
        return total1
    def aud_num1(self):
        aud_num2 = int(input('请输入大人的数量：'))
        return aud_num2
    def child_num1(self):
        chlid_num2 = int(input('请输入儿童的数量：'))
        return  chlid_num2
    def iswkd1(self):
        iswkd2 = input('请问是否周末来？ yes/no:')
        return iswkd2


print('欢迎光临迪士尼。')
a = Menpiao()
print(a.count_price())

