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



def miss1():
    print('')

def buttonClick():
    print('button clicked')


otherFrame = Toplevel()

otherFrame.withdraw()

otherFrame.attributes('-toolwindow', True)

otherFrame.geometry('150x50')

Label(otherFrame, text="5秒后关闭!", width=50).pack()


i = random.randint(0,10)

# 创建frame容器
row1 = Frame(width=1000, height=500, bg='green')
row2 = Frame(width=1000, height=150, )
row3 = Frame(width=1000, height=30)

row1.grid(row=0, column=0, padx=1, pady=3)
row2.grid(row=1, column=0, padx=1, pady=3)
row3.grid(row=2, column=0)

# row1添加图片
bm = PhotoImage(file="wodi_pic.png")
lblImage = Label(row1, image=bm)
# lblImage.image = bm
lblImage.grid()

# row2添加规则
label2 = Label(row2,text=rools,justify=LEFT)
label2.grid()

# row3容器添加按钮
button1 = Button(row3,text='3',width=22,command=buttonClick)
button1.grid(row=2, column=0)
button2 = Button(row3,text='开始游戏',width=22,command=buttonClick)
button2.grid(row=2, column=1, sticky=E)
button3 = Button(row3,text='查看单词',width=22,command=random1)
button3.grid(row=2, column=2, sticky=E)
button4 = Button(row3,text='选择玩家号码',width=22,command=buttonClick)
button4.grid(row=2, column=3, sticky=E)
button5 = Button(row3,text='投票',width=22,command=buttonClick)
button5.grid(row=2, column=4, sticky=E)
button6 = Button(row3,text='结束游戏',width=22,command=quit)
button6.grid(row=2, column=5, sticky=E)

row1.grid_propagate(0)
row2.grid_propagate(0)
row3.grid_propagate(0)

root.mainloop()




