#!usr/bin/python
#coding:utf-8
#author:bingka.wang

from tkinter import *

root = Tk()
def callback():
    print('clicked toolbar buttton')

toolbar = Frame(root)
b = Button(toolbar,text='new',width=6,command=callback)
b.pack(side=LEFT,padx=2,pady=2)

b = Button(toolbar,text='open',width=6,command=callback)
b.pack(side=LEFT,padx=2,pady=2)

toolbar.pack(side=TOP,fill=X)
root.mainloop()