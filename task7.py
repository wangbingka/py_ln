#!usr/bin/python
#coding:utf-8
#author:bingka.wang

import random
from tkinter import *
from tkinter import ttk


rools = '''1、游戏有卧底和平民 2 种身份。
2、平民得到同一词语，卧底得到与之相关的另一词语，并且只有一个卧底。
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
    return c



def miss1():
    print('')

def buttonClick():
    print('button clicked')



def list1(self):
    global list1
    list1 = []
    for i in range(3,self):
        list1.append(str(i))
    return list1


i = random.randint(0,10)


class MyApp(object):
    """"""
    # ----------------------------------------------------------------------
    def __init__(self, aroot):
        """Constructor"""
        self.root = aroot
        self.root.title("谁是卧底")
        # self.frame = Frame(aroot)
        # self.frame.pack()
        # btn = Button(self.frame, text="Open Frame", command=self.openFrame)
        # btn.pack()
        self.row1 = Frame(width=1200, height=400, bg='green')
        self.row2 = Frame(width=1200, height=160, )
        self.row3 = Frame(width=1200, height=40)

        self.row1.grid(row=0, column=0, padx=1, pady=3)
        self.row2.grid(row=1, column=0, padx=1, pady=3)
        self.row3.grid(row=2, column=0)

        # row1添加图片
        bm = PhotoImage(file="wodi_pic.png")
        lblImage = Label(self.row1, image=bm)
        lblImage.image = bm
        lblImage.grid()

        # row2添加规则
        label2 = Label(self.row2, text=rools, justify=LEFT)
        label2.grid()

        # row3容器添加按钮

        comboxstr = list1(21)
        comboxlist = ttk.Combobox(self.row3,values=comboxstr)  # 初始化
        comboxlist.current(0)  # 选择第一个
        comboxlist["state"] = "readonly"
        comboxlist.bind("<<ComboboxSelected>>",print(comboxlist.get()))
        comboxlist.grid(row=2,column=0)

        button1 = Button(self.row3, text='选择玩家数量\n并开始游戏', width=30, command=buttonClick)
        button1.grid(row=2, column=1)

        # button2 = Button(self.row3, text='开始游戏', width=25, command=print(comboxlist.current))
        # button2.grid(row=2, column=2, sticky=E)
        button3 = Button(self.row3, text='查看编号和单词', width=30, command=self.openFrame1)
        button3.grid(row=2, column=2, sticky=E)
        button4 = Button(self.row3, text='选择玩家号码', width=30, command=buttonClick)
        button4.grid(row=2, column=3, sticky=E)

        print(list1(comboxlist.get()))
        comboxlist1 = ttk.Combobox(self.row3,values=comboxstr1)  # 初始化
        comboxlist1.current(0)  # 选择第一个
        comboxlist1["state"] = "readonly"
        comboxlist1.grid(row=2,column=3)

        button5 = Button(self.row3, text='投票', width=25, command=buttonClick)
        button5.grid(row=2, column=4, sticky=E)
        button6 = Button(self.row3, text='结束游戏', width=25, command=quit)
        button6.grid(row=2, column=5, sticky=E)

        self.row1.grid_propagate(0)
        self.row2.grid_propagate(0)
        self.row3.grid_propagate(0)

    def show_msg(self):
        retrun

    def id_num(self):
        c = self.get()
        list2 = list1(int(c))
        id_num = list2[0]
        del list2[0]
        return id_num



    # ----------------------------------------------------------------------
    def hide(self):
        """"""
        self.root.withdraw()

    # ----------------------------------------------------------------------
    def openFrame1(self):
        """"""
        self.hide()
        otherFrame = Toplevel()
        # otherFrame.withdraw()
        otherFrame.attributes('-toolwindow', True)
        otherFrame.geometry('400x200')
        Label(otherFrame, text='你的编号:'+self.id_num(MyApp.comboxlist), width=50).pack()
        Label(otherFrame, text='单词:' + random1(), width=50).pack()
        handler = lambda: self.onCloseOtherFrame(otherFrame)
        Button(otherFrame, text='隐藏', width=50, command=handler).pack()

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



# 创建frame容器

root = Tk()
root.geometry("1200x800")
app = MyApp(root)
root.mainloop()




