# coding:utf-8
#开奖的彩票号码

import time

no = '896521357'

#接收输入的彩票信息
# myno = input('请输入你的彩票号码：')
# if myno == no:
# 	print('买房买车')
# else:
# 	print('哎呀差一点中了，请继续加油')


"""
获取系统时间，并判断现在是上、还是中、或者下旬，并且判断是星期几：
"""
#1、先获取到系统时间
now_time = time.localtime()
#2、得到系统时间的当月天数，还有星期几的数据
mday = now_time.tm_mday
wday = now_time.tm_wday
result = '现在是%s月的%s日，并且是当月的'%(now_time.tm_mon,wday)
#3、根据获得天数信息进行判断是，上、中、下旬
# if mday <=15:
# 	result +='上旬'
# else:
# 	result +='下旬'
#另一种简单写法，仅限于只有两种可能的
result +='上旬' if mday <=15 else '下旬'
if wday ==1:
	result +=',而且是星期一哦。'
elif wday ==2:
	result +=',而且是星期二哦。'
elif wday ==3:
	result +=',而且是星期三哦。'
elif wday ==4:
	result +=',而且是星期四哦。'
elif wday ==5:
	result +=',而且是星期五哦。'
elif wday ==6:
	result +=',而且是星期六哦。'
elif wday ==0:
	result +=',而且是星期天哦。'
else:
	print('难道会是星期八嘛！')
print(result)