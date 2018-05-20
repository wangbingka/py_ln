#print(*objects,sep='',end='\n',file=sys.stdout,flush=False)
#sep,''里面放分隔符，end=''表示结束完成，file输出位置，flush是否刷新缓冲区
print('hello world')
print('hello world','张三')
print('hello world','张三','李四',sep='|')
print('hello world','张三','李四',sep='$')
print('hello world','张三','李四',sep='$',end='')
print('hello world','张三','李四',sep='$',end='\n')
print('hello world','张三','李四',sep='$',end='\n')