#!/usr/bin/env python
#_*_coding:utf-8_*_

'''
a = []
help(a)

print dir()    #列出所有的key
print vars()   #列出所有的key var
#['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'a']
#{'a': [], '__builtins__': <module '__builtin__' (built-in)>, '__file__': 'C:\\Users\\hantao\\workspace\\day3\\\xc4\xda\xd6\xc3\xba\xaf\xca\xfd\xa3\xa8\xd2\xbb\xa3\xa9\\index.py', '__package__': None, '__name__': '__main__', '__doc__': None}
'''
from operator import itemgetter

'''
a=[]
a1=list()
a2={}
print  type(a)      #显示传的的文件 的类型
print type(a1)
print type(a2)

#<type 'list'>
#<type 'list'>
#<type 'dict'>

'''

####id
'''
t1 = 123
t2 = 124

print id(t1)    #记录变量在内存中的位置
print id(t2)

#4755184
#4755160

'''


##cmp

'''
#bool()判断真或者假

print bool(0)
print bool(1)
print bool(2)
print bool(3)
'''

'''
##divmod  #相除得商和余数
print divmod(9,4)
print divmod(9,3)

#(2, 1)
#(3, 0)
'''

'''
#max min 取最大或者最小值
print max([1,3,4])
print min([1,3,4])

#4
#1
'''
'''
#sum()求和
print sum([1,3,4])
#8
'''

'''
#pow 指数（某数的几次方得）
print pow(2,10)
#1024
'''
'''
#len 长度
print len([1,3,4,0])
#4
'''
'''
#all 迭代（所有的布尔值为真才为真）
print all([1,3,4,0])
print all([1,3,4,1])

#False
#True
'''
'''
#any 有真则为真
print any([1,3,4,0])
print any([0,0,0,0])
'''

'''
#chr ord 阿斯科码的相互转换
print chr(66)
print chr(67)
print chr(68)
print chr(69)
print ord('B')
print ord('C')
print ord('D')
print ord('E')
#B
#C
#D
#E
#66
#67
#68
#69

'''
'''
#hex 十六进制 bin 二进制  oct八进制
print hex(2)
print bin(2)
print oct(2)
#0x2
#0b10
#02
'''

'''
#enumerate 给变量值加一个序列(索引值)
li = ['韩涛','韩志伟','韩美震']

for item in li:
    print item
for item in enumerate(li,0):
    print item[0],item[1]
    
#韩涛
#韩志伟
#韩美震
#0 韩涛
#1 韩志伟
#2 韩美震

'''

'''
#s.format字符串的格式化
s = 'i am {0},{1}'
print  s.format('韩涛','xxxxxx') 
#i am 韩涛,xxxxxx
'''

'''
#apply执行函数
def Function(arg):
    print arg
Function('韩涛')
print apply(Function,('aaa'))
'''

'''
#map
#不用map的方法
def foo(arg):
    return arg + 100
li = [11,22,33]

temp=[]
for item in li:
    temp.append(foo(item))
print temp

#用map的方法
def foo(arg):
    return arg + 100
li = [11,22,33]
print map(foo,li)

#map精简版
temp = map(lambda arg:arg + 100,li)
print temp

#[111, 122, 133]
#[111, 122, 133]
#[111, 122, 133]
'''

'''
###filter 过滤(前提给filter加一个条件)

li = [11,22,33]
def foo(arg):
    if arg <22:
        return True
    else:
        return False

print filter(foo,li)
#[11]

temp = filter(lambda x:x<22,li)
print temp
#[11]

'''

'''
##reduce 累加的方法

li = [11,22,33]
temp = reduce(lambda x,y:x + y,li)
temp1 = reduce(lambda x,y:x * y,li)
print temp 
print temp1

'''
'''
x = [1,2,3]
y = [4,5,4]
z = [4,5,9]
q = [8,7,3]

print zip(x,y,z,q)

#[(1, 4, 4, 8), (2, 5, 5, 7), (3, 4, 9, 3)]

'''

#eval   将字符串中的算式进行执行

a = '8*8'
b = '7+7'
print eval(a)
print eval(b)

