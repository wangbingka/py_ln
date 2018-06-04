#!usr/bin/python
#coding:utf-8
#author:bingka.wang

from tkinter import *
import tkinter.messagebox

root =Tk()

def callback():
    #messagebox，不同的方式，不同的显示
    # if tkinter.messagebox.askokcancel('Sundy','Hi Sundy'):
    # if tkinter.messagebox.showerror('Sundy', 'Hi Sundy'):
    # if tkinter.messagebox.askquestion('Sundy', 'Hi Sundy'):
    # if tkinter.messagebox.askretrycancel('Sundy', 'Hi Sundy'):
    # if tkinter.messagebox.showinfo('Sundy', 'Hi Sundy'):
    if tkinter.messagebox.showwarning('Sundy', 'Hi Sundy'):
        print('Clicked Yes')
    else:
        print('Clicked No')

button = Button(root,text='Button1',command=callback)
button.pack()
button.mainloop()
