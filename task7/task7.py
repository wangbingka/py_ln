#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/6 22:42
# @Author  : bingka.wang 
# @Email   : wangbingka@126.com

#!usr/bin/python
#coding:utf-8
#author:bingka.wang

import random
from tkinter import *
from tkinter import ttk
import tkinter.messagebox


rools = '''1、游戏有卧底和平民 2 种身份。
2、平民得到同一词语，卧底得到与之相关的另一词语，并且只有一个卧底。
3、每人一轮用一句话描述自己的词语，既不能让卧底察觉，也要给同伴以暗示。
4、每轮描述完毕，所有在场的人投票选出怀疑谁是卧底，得票最多的人出局。
5、若出现平局，平局的人进行描述，大家再进行投票投出那个人。
5、若卧底撑到最后一轮（人数为两人），则卧底获胜，反之，则平民胜利。
'''
b = ['钢笔','铅笔','月亮','太阳','美人痣','青春痘','陈奕迅','张学友','鸭脖','鸡爪','风衣','毛衣','苹果','安卓',\
     '孟非','乐嘉','胡海泉','陈羽凡','唇膏','口红','最炫民族风','江南style']


#随机选词函数，超过人数时使用抓取异常来进行提醒
def random1():
    global c
    try:
        c = random.choice(list4)
    except  IndexError:
        tkinter.messagebox.showinfo('谁是卧底', '次数超出游戏人数，\n请重新确认玩家数量')
        otherFrame.withdraw()
    try:
        list4.remove(c)
    except ValueError:
        pass
    return c

#生成随机选单词的列表
def list_4():
    count1 = 1
    while True and count1 <= int(get_num1):
        if count1 < int(get_num1):
            list4.append(b[2 * i])
        if count1 == int(get_num1):
            list4.append(b[2 * i + 1])
        count1 += 1
    return list4

#生成下拉列表时使用
def list1(a,b):
    list2 = []
    for i in range(a,b):
        list2.append(str(i))
    return list2

#确认投票成功，并获取有效投票的值，
# 但这段貌似有点有问题，投票超过10的数字之后，即使玩家是8个人最大号也就是8，判断会出错，也是投票成功，还未找到原因
def veryf1():
    global sel_num11
    sel_num1 = comboxlist1.get()
    if sel_num1 > get_num1:
        tkinter.messagebox.showinfo('投票', 'sorry，没有此编号的玩家\n目前编号是：1-%d之间。\n请重新投票'%int(get_num1))
    else:
        tkinter.messagebox.showinfo('投票','投票成功')
        sel_num11 = sel_num1
        # print(get_num1)
        # print(sel_num11)

#生成身份编号
def id_num():
    global id_num1
    try:
        id_num1 = id_numlist1[0]
        id_numlist1.remove(id_num1)
    except  IndexError or ValueError:
        pass
    return id_num1

#生成身份编号需要用到的列表
def id_numlist():
    id_numlist1 = []
    for i in range(1,int(get_num1)+1):
        id_numlist1.append(i)
    return id_numlist1


# 查看单词子窗口
def openFrame1():
    global otherFrame
    otherFrame = Toplevel(bg='blue')
    # otherFrame.withdraw()
    otherFrame.attributes('-toolwindow', True)
    otherFrame.geometry('400x200+600+400')
    Label(otherFrame, text='你的编号:'+str(id_num()),bg='blue', fg='white',width=50).pack()
    Label(otherFrame, text='单词:' + random1(),bg='blue', fg='white',width=50).pack()
    Button(otherFrame, text='隐藏', width=50, bg='blue',fg='white',command=onCloseOtherFrame).pack()

#关闭查看单词子窗口
def onCloseOtherFrame():
    otherFrame.withdraw()

#获取参加游戏人数，并且生成两个之后会用到的列表
def get_num():
    global list4
    global id_numlist1
    global get_num1
    get_num1 = comboxlist.get()
    list4 = list_4()
    id_numlist1 =id_numlist()


i = random.randint(0,10)
get_num1 = 3
list4 = []




root =Tk()
root.title("谁是卧底")

#主窗口
row1 = Frame(width=1200, height=400, bg='green')
row2 = Frame(width=1200, height=160, )
row3 = Frame(width=1200, height=40)

row1.grid(row=0, column=0, padx=1, pady=3)
row2.grid(row=1, column=0, padx=1, pady=3)
row3.grid(row=2, column=0)

# row1添加图片
bm = PhotoImage(file="wodi_pic.png")
lblImage = Label(row1, image=bm)
lblImage.image = bm
lblImage.grid()

# row2添加规则
label2 = Label(row2, text=rools, justify=LEFT)
label2.grid()

# row3容器添加按钮，选择玩家数量的下拉列表
comboxstr = list1(3,21)
comboxlist = ttk.Combobox(row3,values=comboxstr)  # 初始化
comboxlist.current(0)  # 选择第一个
comboxlist["state"] = "readonly"
comboxlist.bind("<<ComboboxSelected>>",get_num())
comboxlist.grid(row=2,column=0)

button1 = Button(row3, text='确认玩家数量', width=30, command=get_num)
button1.grid(row=2, column=1)


button2 = Button(row3, text='查看编号和单词', width=30, command=openFrame1)
button2.grid(row=2, column=2, sticky=E)

#选择玩家号码的下拉列表
comboxstr1 = ['选择玩家号码']+list1(1,21)
comboxlist1 = ttk.Combobox(row3,values=comboxstr1)  # 初始化
comboxlist1.current(0)  # 选择第一个
comboxlist1["state"] = "readonly"
comboxlist1.grid(row=2,column=3, sticky=E)

button3 = Button(row3, text='投票', width=25, command=veryf1)
button3.grid(row=2, column=4, sticky=E)
button4 = Button(row3, text='结束游戏', width=25, command=quit)
button4.grid(row=2, column=5, sticky=E)

#锁定窗口大小
row1.grid_propagate(0)
row2.grid_propagate(0)
row3.grid_propagate(0)

root.mainloop()