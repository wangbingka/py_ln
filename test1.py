#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/5 22:06
# @Author  : bingka.wang 
# @Email   : wangbingka@126.com

from tkinter  import *

import time

import threading



def showother():

    otherFrame.update()

    otherFrame.deiconify()

    hide_thd()



def delaysHideOther():

    time.sleep(5)

    otherFrame.withdraw()



def hide_thd():

    threading.Thread(target = delaysHideOther).start()



root = Tk()



otherFrame = Toplevel()

otherFrame.withdraw()

otherFrame.attributes('-toolwindow', True)

otherFrame.geometry('150x50')

Label(otherFrame, text="5秒后关闭!", width=50).pack()



root.geometry('150x80')

Button(root, text='显示弹窗', width=10, command=showother).pack()


root.mainloop()
