#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/3 22:30
# @Author  : bingka.wang 
# @Email   : wangbingka@126.com

from tkinter import *
# 1、root，容器，不能直接卡到
# 2、widget,ui主键
# 3、WM，窗体显示，以及叠加方式
# 4、event，输入事件，类似鼠标和键盘，button传导操作方式，
# 状态事件
# 管理事件，类似窗体的生命周期消亡

button =Button(text='SundyButton',padx=10,pady=10)
button.config(cursor='gumby')
button.config(bd=8,relief=RAISED)
button.config(bg='green',fg='yellow')
button.config(font=('Helvetica',10,'bold italic'))
button.pack()
button.mainloop()

