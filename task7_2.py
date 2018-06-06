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

def random1():
    global c
    c = random.choice([b[2*i],b[2*i+1]])
    if c == b[2*i+1]:
        b[2*i+1] = b[2*i]
    else:
        pass
    return c

def buttonClick():
    print('button clicked')

def list1(a,b):
    list2 = []
    for i in range(a,b):
        list2.append(str(i))
    return list2

def veryf1():
    #messagebox，不同的方式，不同的显示
    # if tkinter.messagebox.askokcancel('Sundy','Hi Sundy'):
    # if tkinter.messagebox.showerror('Sundy', 'Hi Sundy'):
    # if tkinter.messagebox.askquestion('Sundy', 'Hi Sundy'):
    # if tkinter.messagebox.askretrycancel('Sundy', 'Hi Sundy'):
    # if tkinter.messagebox.showinfo('Sundy', 'Hi Sundy'):
    tkinter.messagebox.showinfo('投票','投票成功')

def id_num():
    list3 = list1(1,int(get_num1)+1)
    id_num = list3[0]
    del list3[0]
    return id_num

# ----------------------------------------------------------------------
def hide():
    """"""
    root.withdraw()

# ----------------------------------------------------------------------
def openFrame1():
    """"""
    # hide()
    global otherFrame
    otherFrame = Toplevel()
    # otherFrame.withdraw()
    otherFrame.attributes('-toolwindow', True)
    otherFrame.geometry('400x200')
    Label(otherFrame, text='你的编号:'+str(id_num()), width=50).pack()
    Label(otherFrame, text='单词:' + random1(), width=50).pack()
    Button(otherFrame, text='隐藏', width=50, command=onCloseOtherFrame).pack()

# ----------------------------------------------------------------------
def onCloseOtherFrame():
    """"""
    otherFrame.withdraw()

# ----------------------------------------------------------------------
def show(self):
    """"""
    root.update()
    root.deiconify()

def get_num():
    global get_num1
    get_num1 = comboxlist.get()
    return get_num1


i = random.randint(0,10)




root =Tk()
root.title("谁是卧底")

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

# row3容器添加按钮

comboxstr = list1(1,21)
comboxlist = ttk.Combobox(row3,values=comboxstr)  # 初始化
comboxlist.current(0)  # 选择第一个
comboxlist["state"] = "readonly"
comboxlist.bind("<<ComboboxSelected>>",print(comboxlist.get()))
comboxlist.grid(row=2,column=0)

button1 = Button(row3, text='选择玩家数量\n并开始游戏', width=30, command=get_num)
button1.grid(row=2, column=1)

# button2 = Button(row3, text='开始游戏', width=25, command=)
# button2.grid(row=2, column=2, sticky=E)
button3 = Button(row3, text='查看编号和单词', width=30, command=openFrame1)
button3.grid(row=2, column=2, sticky=E)
button4 = Button(row3, text='选择玩家号码', width=30, command=buttonClick)
button4.grid(row=2, column=3, sticky=E)

comboxstr1 = ['选择玩家号码']+list1(1,20)
comboxlist1 = ttk.Combobox(row3,values=comboxstr1)  # 初始化
comboxlist1.current(0)  # 选择第一个
comboxlist1["state"] = "readonly"
comboxlist1.grid(row=2,column=3)

button5 = Button(row3, text='投票', width=25, command=veryf1)
button5.grid(row=2, column=4, sticky=E)
button6 = Button(row3, text='结束游戏', width=25, command=quit)
button6.grid(row=2, column=5, sticky=E)

row1.grid_propagate(0)
row2.grid_propagate(0)
row3.grid_propagate(0)

root.mainloop()