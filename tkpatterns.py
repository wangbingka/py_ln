#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/4 23:12
# @Author  : bingka.wang 
# @Email   : wangbingka@126.com

from tkinter import *

master = Tk()

w = Canvas(master, width=200, height=100)
w.pack()

w.create_line(0, 0, 200, 100)
w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

w.create_rectangle(50, 25, 150, 75, fill="blue")

mainloop()