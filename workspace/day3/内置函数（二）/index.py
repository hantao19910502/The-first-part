#!/usr/bin/env python
#_*_coding:utf-8_*_

'''
####����
#���ַ��������Ƶ���ģ��

temp = 'sys'

mode = __import__(temp)
print mode.path
'''
from test.test_datetime import PicklableFixedOffset

'''
#���ַ���������ִ�к���

temp = 'count'
func = 'count1'

mode1 = __import__(temp)
function = getattr(mode1,func)
print function()

#319

'''

'''
###################################���������
import random
print random.random()             #0-1֮��������
print random.randint(1,2)         #1-2֮����������
print random.randrange(1,10)      #1-10֮����������

#0.316089364546
#3
#3
'''


#����һ������ĸ�����ֵ������
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
code=[]           #�������������б�����б����棨��ᣩ
import random
for h in range(6):
    if h == random.randint(1,5):
        code.append(str(random.randint(1,5)))
    else:
        temp = random.randint(65,90)
        code.append(str(chr(temp)))
print ''.join(code)                     #���б�ת��Ϊ�ַ���

'''

'''
############################MD5���ܵķ���
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
print    dumpsed                  #���л�
print type(dumpsed )   

loadsed = pickle.loads(dumpsed)   #�����л�
print loadsed 
print type(loadsed)       
'''

'''
pickle.dump(li,open('C:/tmp/temp.pk','w'))         #���л����ļ�����

result = pickle.load(open('C:/tmp/temp.pk','r'))   #�����л�
print result
'''
'''
import json
name_dic = {'name':'wupeiqi','age':'34'}
json1 = json.dumps(name_dic)               #���л�
print json1
pickle = pickle.dumps(name_dic)
print pickle
#serialized_obj = json.dumps(name_dic)
load = json.loads(json1)                  #�����л�  
print load
'''



########################������ʽ
'''
import re

result1 = re.match('\d+','adadfasd123dasfad')    #�ڿ�ͷ��ʼ��û���˳���û�з���none
if result1:
    print result1.group()
else:
    print 'nothing'
result2 = re.search('\d+','adadfasd456dasfad')   #�ڿ�ͷ��ʼ��û�н���������
if result2:
    print result2.group()
#nothing
#456

result3 = re.findall('\d+','123adadfasd456dasfad')
print result3
'''

    




