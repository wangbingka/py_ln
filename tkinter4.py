#!usr/bin/python
#coding:utf-8
#author:bingka.wang

from tkinter import *
import tkinter.messagebox

root = Tk()
    # def buttonClick():
    #     print('button clicked')
    # button = Button(text='hello',command=buttonClick)
    # button.pack()
    # root.mainloop()
def callback(event):
    # print('Button-1 clicked')
    frame.focus_set()
    print('clicked at:',event.x,event.y)
def key(event):
    print('pressed',repr(event.char))
def closeWindow():
    if tkinter.messagebox.askokcancel('Quit','Do you want to exit'):
        root.destroy()
frame =Frame(root,width=100,height=100)
frame.bind('<Button-1>',callback)
frame.bind('<Key>',key)
frame.pack()
root.protocol('WM_DELETE_WINDOW',closeWindow)
frame.mainloop()
