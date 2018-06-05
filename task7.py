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
bm = PhotoImage(file = 'wodi_pic.png')
label1 = Label(root,height=300,image=bm,bg='green').pack()
label2 = Label(root,text=rools,justify=LEFT).pack()
def buttonClick():
    print('button clicked')
button = Button(text='3',command=buttonClick).pack()
button = Button(text='开始游戏',command=buttonClick).pack()
button3 = Button(text='查看单词',command=random1).pack()
button = Button(text='选择玩家号码',command=buttonClick).pack()
button = Button(text='投票',command=buttonClick).pack()
button = Button(text='结束游戏',command=quit).pack()

root.mainloop()




