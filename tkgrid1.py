#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/4 23:17
# @Author  : bingka.wang 
# @Email   : wangbingka@126.com

from tkinter import *

root =Tk()
Label(root,text='First').grid(row=0)
Label(root,text='Scecond').grid(row=1)
e1 = Entry(root)
e2 = Entry(root)

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)

Button(root,text='OK').grid(row=2)

root.mainloop()