#!usr/bin/python
#coding:utf-8
#author:bingka.wang

'''
1、类学校成员，方法：自我介绍，类，加个人介绍，统计总数
2、子类老师，继承，方法：打招呼
3、子类学生，继承，方法：重写打招呼，方法：学习情况
'''

# 1、创建一个学校成员类，这个类登记成员的姓名并在成员加入时自我介绍，还要统计学校的总人数。
class Sch_num():
    count_num = 0
    def __init__(self,aname,aintro):
        self.name = aname
        self.intro = aintro
        Sch_num.count_num +=1

# 4、实例对象结束的时候，总人数减一，
    def __del__(self):
        # self.__class__.count_num -=1
        print('del'+self.name)
        Sch_num.count_num -= 1
        print('实例对象结束。'+str(Sch_num.count_num))


# 2、创建一个老师类，这个类继承学校成员类，创建对象的时候总人数加一，老师类重写具体打招呼的类容
class Teach_num(Sch_num):
    def say_hi(self):
        return '大家好，我是一名教师。'

# 3、创建一个学生类，这个继承学校成员类，创建对象时总人数也会加一，学生类重写打招呼的类容，增加一个方法介绍自己的学习情况。
class Stu_num(Sch_num):
    def say_hi(self):
        return '大家好，我是一名学生。'
    def __init__(self,aname,aintro,alnstu):
        #这句是保证子类能继续使用父类的构造方法
        Sch_num.__init__(self,aname,aintro)
        self.lnstu = alnstu

c =Sch_num('张三','今年50岁')
print('大家好'+'，'+'我叫{}，{}'.format(c.name,c.intro))


a =Teach_num('王一','女，今年30岁')
print(a.say_hi()+'姓名是%s'%a.name+'，'+a.intro)


b = Stu_num('李二','男，今年15岁','我去年所有科目的平均分数99')
print(b.say_hi()+'姓名是%s'%b.name+'，'+b.intro+'，'+b.lnstu)

print(a.count_num)










