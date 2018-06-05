#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/5 22:06
# @Author  : bingka.wang 
# @Email   : wangbingka@126.com

from tkinter import  *
win = Tk()
win.title("My tools")
win.geometry('300x300+300+300')
xinyun = StringVar(win)
xinyun.set("猜猜我是谁")
banbie.set("10")
cq_lblxinyun = Label(win, textvariable=xinyun, fg="red",
                      font=("黑体", 30, "bold"),
                      relief="sunken", borderwidth=5)
cq_btstar = Button(win, text="开始抽签", font =("宋体", 14,
                  "normal"), command=chouqian)
cq_lblban = Entry(win, textvariable=banbie, width="4",
                      font=("宋体", 12, "normal"))
cq_lblban1 = Label(win, text="组", width="2", justify="left",
                      font=("宋体", 12, "normal"))
win.mainloop()
