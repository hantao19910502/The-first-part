#!/usr/bin/env python
#_*_coding:utf-8_*_

'''
a = []
help(a)

print dir()    #�г����е�key
print vars()   #�г����е�key var
#['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'a']
#{'a': [], '__builtins__': <module '__builtin__' (built-in)>, '__file__': 'C:\\Users\\hantao\\workspace\\day3\\\xc4\xda\xd6\xc3\xba\xaf\xca\xfd\xa3\xa8\xd2\xbb\xa3\xa9\\index.py', '__package__': None, '__name__': '__main__', '__doc__': None}
'''
from operator import itemgetter

'''
a=[]
a1=list()
a2={}
print  type(a)      #��ʾ���ĵ��ļ� ������
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

print id(t1)    #��¼�������ڴ��е�λ��
print id(t2)

#4755184
#4755160

'''


##cmp

'''
#bool()�ж�����߼�

print bool(0)
print bool(1)
print bool(2)
print bool(3)
'''

'''
##divmod  #������̺�����
print divmod(9,4)
print divmod(9,3)

#(2, 1)
#(3, 0)
'''

'''
#max min ȡ��������Сֵ
print max([1,3,4])
print min([1,3,4])

#4
#1
'''
'''
#sum()���
print sum([1,3,4])
#8
'''

'''
#pow ָ����ĳ���ļ��η��ã�
print pow(2,10)
#1024
'''
'''
#len ����
print len([1,3,4,0])
#4
'''
'''
#all ���������еĲ���ֵΪ���Ϊ�棩
print all([1,3,4,0])
print all([1,3,4,1])

#False
#True
'''
'''
#any ������Ϊ��
print any([1,3,4,0])
print any([0,0,0,0])
'''

'''
#chr ord ��˹������໥ת��
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
#hex ʮ������ bin ������  oct�˽���
print hex(2)
print bin(2)
print oct(2)
#0x2
#0b10
#02
'''

'''
#enumerate ������ֵ��һ������(����ֵ)
li = ['����','��־ΰ','������']

for item in li:
    print item
for item in enumerate(li,0):
    print item[0],item[1]
    
#����
#��־ΰ
#������
#0 ����
#1 ��־ΰ
#2 ������

'''

'''
#s.format�ַ����ĸ�ʽ��
s = 'i am {0},{1}'
print  s.format('����','xxxxxx') 
#i am ����,xxxxxx
'''

'''
#applyִ�к���
def Function(arg):
    print arg
Function('����')
print apply(Function,('aaa'))
'''

'''
#map
#����map�ķ���
def foo(arg):
    return arg + 100
li = [11,22,33]

temp=[]
for item in li:
    temp.append(foo(item))
print temp

#��map�ķ���
def foo(arg):
    return arg + 100
li = [11,22,33]
print map(foo,li)

#map�����
temp = map(lambda arg:arg + 100,li)
print temp

#[111, 122, 133]
#[111, 122, 133]
#[111, 122, 133]
'''

'''
###filter ����(ǰ���filter��һ������)

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
##reduce �ۼӵķ���

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

#eval   ���ַ����е���ʽ����ִ��

a = '8*8'
b = '7+7'
print eval(a)
print eval(b)

