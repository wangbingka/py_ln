#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/3 17:32
# @Author  : bingka.wang 
# @Email   : wangbingka@126.com

from tkinter import *

root = Tk()

label = Label(root,text='Hello world')
label.config(cursor='gumby')
label.config(width=80,height=10,fg='yellow',bg='dark green')
label.config(font=('times','28','bold'))
label.pack()
label = Label(root,text='Hello world',bg = 'red').pack()
label = Label(root,text='Hello world',bg = 'blue').pack()
label = Label(root,text='Hello world',bg = 'green',fg='white').pack()





root.mainloop()

# top = tkinter.tk()
# #进入消息循环
# top.mailoop()