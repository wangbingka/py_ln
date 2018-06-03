#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/3 17:58
# @Author  : bingka.wang 
# @Email   : wangbingka@126.com

from tkinter import *
class App:
    def __init__(self,master):
        frame = Frame(master)
        frame.pack()
        self.button = Button(frame,text='Hello Class',fg='red',command=frame.quit)
        self.button.pack()
        self.hibutton = Button(frame,text='Say Hi',command=self.say_hi)
        self.hibutton.pack()
    def say_hi(self):
        print('Hi Sundy,Thanks!')

root =Tk()
app = App(root)
root.mainloop()
