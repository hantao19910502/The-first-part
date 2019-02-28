#!/usr/bin/env python
#_*_coding:utf-8_*_

'''
####放射
#以字符串的形势导入模块

temp = 'sys'

mode = __import__(temp)
print mode.path
'''
from test.test_datetime import PicklableFixedOffset

'''
#以字符串的形势执行函数

temp = 'count'
func = 'count1'

mode1 = __import__(temp)
function = getattr(mode1,func)
print function()

#319

'''

'''
###################################生成随机数
import random
print random.random()             #0-1之间的随机数
print random.randint(1,2)         #1-2之间的随机整数
print random.randrange(1,10)      #1-10之间的随机整数

#0.316089364546
#3
#3
'''


#生成一个有字母有数字的随机数
#1)
import random
for h in range(6):
    if h == random.randint(1,5):
        print random.randint(1,5)
    else:
        temp = random.randint(65,90)
        print chr(temp)


'''
#2)
code=[]           #将产生的数字列表放在列表里面（变横）
import random
for h in range(6):
    if h == random.randint(1,5):
        code.append(str(random.randint(1,5)))
    else:
        temp = random.randint(65,90)
        code.append(str(chr(temp)))
print ''.join(code)                     #将列表转化为字符串

'''

'''
############################MD5加密的方法
import hashlib

hash = hashlib.md5()
hash.update('aa')
print hash.hexdigest()
#hash.update('admin')
#print hash.hexdigest()
#print hash.digest()
#print aa.hexdigest()
'''


import pickle

li = ['hantao','1','2','hanzhiwei']
'''
dumpsed = pickle.dumps(li)
print    dumpsed                  #序列化
print type(dumpsed )   

loadsed = pickle.loads(dumpsed)   #反序列化
print loadsed 
print type(loadsed)       
'''

'''
pickle.dump(li,open('C:/tmp/temp.pk','w'))         #序列化到文件里面

result = pickle.load(open('C:/tmp/temp.pk','r'))   #反序列化
print result
'''
'''
import json
name_dic = {'name':'wupeiqi','age':'34'}
json1 = json.dumps(name_dic)               #序列化
print json1
pickle = pickle.dumps(name_dic)
print pickle
#serialized_obj = json.dumps(name_dic)
load = json.loads(json1)                  #反序列化  
print load
'''



########################正则表达式
'''
import re

result1 = re.match('\d+','adadfasd123dasfad')    #在开头开始找没有退出，没有返回none
if result1:
    print result1.group()
else:
    print 'nothing'
result2 = re.search('\d+','adadfasd456dasfad')   #在开头开始找没有接着往下找
if result2:
    print result2.group()
#nothing
#456

result3 = re.findall('\d+','123adadfasd456dasfad')
print result3
'''

    




