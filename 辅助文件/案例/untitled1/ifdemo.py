# coding: utf-8
# author: yopoing
# 开奖的彩票号码
# no = '896521357'
# # 接收输入的彩票信息
# myno = input('请输入你买的彩票号码：')
# if myno == no:
#     print('买房，还要买车')
# else:
#     print('哎呀没中，继续买彩票')

"""
获取系统时间，并根据系统时间判断出今天是当月上旬还是下旬，是星期几。
1、先获取到系统时间
2、得到系统时间的当月天数，还有星期几的天数
3、根据获得天数信息进行判断
"""
import time
# 1、先获取到系统时间
now_time = time.localtime()
# 2、得到系统时间的当月天数，还有星期几的天数
mday = now_time.tm_mday # 当月天数
wday = now_time.tm_wday # 星期几的天数，取值是0到6，0是星期一，6是星期天
result = "现在是%s年%s月%s日,并且是当月的"%(now_time.tm_year, now_time.tm_mon,
                                now_time.tm_mday)
# 3、根据获得天数信息进行判断
# 先判断上旬还是下旬
# if mday <= 15:
#     result += '上旬,'
# else:
#     result += '下旬,'
result += '上旬,' if mday <= 15 else '下旬,'
# 再判断是星期几
if wday == 0:
    result += '而且是星期一哦。'
elif wday == 1:
    result += '而且是星期二哦。'
elif wday == 2:
    result += '而且是星期三哦。'
elif wday == 3:
    result += '而且是星期四哦。'
elif wday == 4:
    result += '而且是星期五哦。'
elif wday == 5:
    result += '而且是星期六哦。'
elif wday == 6:
    result += '而且是星期天哦。'
else:
    result += '难道会是星期班。哈哈，这个语句执行不到'

print(result)
