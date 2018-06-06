#!usr/bin/python
#coding:utf-8
#author:bingka.wang
from tkinter import *

root = Tk()
#!usr/bin/python
#coding:utf-8
#author:bingka.wang

import random
from tkinter import *

root = Tk()
root.title('谁是卧底')

rools = '''1、游戏有卧底和平民 2 种身份。
2、平民得到同一词语，卧底得到与之相关的另一词语。
3、每人一轮用一句话描述自己的词语，既不能让卧底察觉，也要给同伴以暗示。
4、每轮描述完毕，所有在场的人投票选出怀疑谁是卧底，得票最多的人出局。
5、若出现平局，平局的人进行描述，大家再进行投票投出那个人。
5、若卧底撑到最后一轮（人数为两人），则卧底获胜，反之，则平民胜利。
'''
b = ['钢笔','铅笔','月亮','太阳','美人痣','青春痘','陈奕迅','张学友','鸭脖','鸡爪','风衣','毛衣','苹果','安卓',\
     '孟非','乐嘉','胡海泉','陈羽凡','唇膏','口红','最炫民族风','江南style']
def random1():
    global c
    c = random.choice([b[2*i],b[2*i+1]])
    if c == b[2*i+1]:
        b[2*i+1] = b[2*i]
    else:
        pass
    button['text'] = c

i = random.randint(0,10)

def miss1():
    print('')


class MyApp(object):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self, aroot):
        """Constructor"""
        self.root = aroot
        self.root.title("谁是卧底")
        self.frame = Frame(aroot)
        self.frame.pack()


        btn = Button(self.frame, text="Open Frame", command=self.openFrame)
        btn.pack()

    # ----------------------------------------------------------------------
    def hide(self):
        """"""
        self.root.withdraw()

    # ----------------------------------------------------------------------
    def openFrame(self):
        """"""
        self.hide()
        otherFrame = Toplevel()
        otherFrame.geometry("400x300")
        otherFrame.title("otherFrame")
        handler = lambda: self.onCloseOtherFrame(otherFrame)
        btn = Button(otherFrame, text="Close", command=handler)
        btn.pack()

    # ----------------------------------------------------------------------
    def onCloseOtherFrame(self, otherFrame):
        """"""
        otherFrame.destroy()
        self.show()

    # ----------------------------------------------------------------------
    def show(self):
        """"""
        self.root.update()
        self.root.deiconify()

bm = PhotoImage(file = 'wodi_pic.png')

w1 = Frame(height=200, width=500)

w2 = Frame(height=50, width=500)

w3 = Frame(height=30, width=500)

w4 = Frame(w3, height=30, width=65)
w5 = Frame(w3, height=30, width=65)
w6 = Frame(w3, height=30, width=65)
w7 = Frame(w3, height=30, width=65)
w8 = Frame(w3, height=30, width=65)
w9 = Frame(w3, height=30, width=65)

w1.grid(row=0, column=0, padx=2, pady=5)
w2.grid(row=1, column=0, padx=2, pady=5)
w1.grid_propagate(0)
w2.grid_propagate(0)

label1 = Label(w1,height=300,image=bm,bg='green')
label2 = Label(w2,text=rools,justify=LEFT)
label1.pack()
label2.pack()




w3.grid(row=2)

# w4.pack(side='left')
#
# w5.pack(side='left')
#
# w6.pack(side='right')


send_button = Button(w4, text="发送")

file_button = Button(w6, text="发送文件")


send_button.pack(side='left')

file_button.pack(side='right')

root.mainloop()

def buttonClick():
    print('button clicked')
button1 = Button(root,text='选择玩家数量',width=8,height=2,command=buttonClick).grid(row=2,column=1)

button = Button(root,text='开始游戏',width=8,height=2,command=buttonClick).grid(row=2,column=2)
button = Button(root,text='查看单词',command=random1).grid(row=2,column=3)
button = Button(root,text='选择玩家号码',command=buttonClick).grid(row=2,column=4)
button = Button(root,text='投票',command=buttonClick).grid(row=2,column=5)
button = Button(root,text='结束游戏',command=quit).grid(row=2,column=6)

root.mainloop()
