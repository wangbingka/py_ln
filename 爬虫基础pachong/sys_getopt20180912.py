#!usr/bin/python
#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time :  2018/9/12 17:43
# @Author: Bingka.wang
# @Email:  wangbingka@126.com


import sys, getopt

'''
sys.argv 是命令行参数列表。
len(sys.argv) 是命令行参数个数。
注：sys.argv[0] 表示脚本名。
'''

print ('参数个数为:', len(sys.argv), '个参数。')
print ('参数列表:', str(sys.argv))

'''
getopt模块
getopt模块是专门处理命令行参数的模块，用于获取命令行选项和参数，也就是sys.argv。命令行选项使得程序的参数更加灵活。支持短选项模式（-）和长选项模式（--）。
该模块提供了两个方法及一个异常处理来解析命令行参数。 

getopt.getopt 方法
:用于解析命令行参数列表，语法格式如下：
getopt.getopt(args, options[, long_options])
args: 要解析的命令行参数列表。
options: 以字符串的格式定义，options后的冒号(:)表示该选项必须有附加的参数，不带冒号表示该选项不附加参数。
long_options: 以列表的格式定义，long_options 后的等号(=)表示如果设置该选项，必须有附加的参数，否则就不附加参数。
该方法返回值由两个元素组成: 第一个是 (option, value) 元组的列表。 第二个是参数列表，包含那些没有'-'或'--'的参数。
'-i'就是正常的option'-i','--i'表示是option'-ifile'，类推，'--h'对应'--hfile'



Exception getopt.GetoptError
在没有找到参数列表，或选项的需要的参数为空时会触发该异常。
异常的参数是一个字符串，表示错误的原因。属性 msg 和 opt 为相关选项的错误信息。
'''


import sys, getopt

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
      print(opts)
      print(args)
   except getopt.GetoptError:
      print('exit for -GetoptError')
      print ('test.py -i <inputfile> -o <outputfile>')
      # sys.exit(2)
      exit
   for opt, arg in opts:
      if opt == '-h':
         print('exit for -h')
         print ('test.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):

         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print ('输入的文件为：', inputfile)
   print ('输出的文件为：', outputfile)

if __name__ == "__main__":
   main(sys.argv[1:])
