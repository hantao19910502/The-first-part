#!/usr/bin/env python
#_*_coding:utf-8_*_

'''
#��
class provice:
    #��̬�ֶ�(������)
    memo = '�й�23��ʡ֮һ'
    @staticmethod
    def hantao():
        print 'nihao'
    def sport_meet(self):
        print self.Name + '���ڿ��˶���'
                 #b1  hantao 19 
    def __init__(self,name,age):   #ͨ��__init__ʵ����(name,age����)  
        #��̬�ֶ�
        self.Name = name            #����һ������
        self.Age = age
    #��̬�����������ࣩ  
    @staticmethod
    def Foo():
        print 'Ҫ��ͷ����'
    #provice.Foo()���������
    
    
    #���ԣ������ķ����Ĳ�ͬ���ѣ�
    @property
    def Bar(self):
        print self.Name + '���ڴ��'
        return 'nothing'
    #hb.Bar
        
#��hantao 19  ��װ��b1�������,b1���ȵ���һ������
b1 = provice('hantao',19)
           
#��b1�з�װ�����Ԫ�ش�ӡ����
print b1.Age                        #����  ----���ֶ�


#��̬�������������
print provice.memo                   #��̬����



#������� ��1����װ  Name�Ƕ��������ʱ����ı���
#�಻�ܷ��ʶ�̬�ֶΣ�������Է��ʾ�̬�ֶ�


#ÿ��ʡ�����Ը��Լ����� �������Զ���������Լ�������
#��̬����
def sport_meets1(self):
    print self.Name + '�Ǻ���'

#������ʲô�����ʱ�����������    
b1.sport_meet()   


#��̬����
provice.Foo()


#ʹ�õ����ԭ��---1�����ظ��ķ����򵥻������ظ��Ķ��������ظ�����д��
#����ķ�����1�����ַ���2����������
  


provice.hantao()

'''

'''
#==========================˽�з���============================
from _multiprocessing import flags

class provice():
    def __init__(self,name,leader,flag):
        self.Name = name
        self.Leader = leader
        #˽���ֶ�
        self.__Thailand = flag
    #˽���ֶεĵ���������ģ��м䴫�ݵģ�
    def show(self):
        print self.__Thailand   
    #˽�з�����˽�з����������ǲ��ܷ��ʵģ�����ͨ�����з������ã�
    def __sha(self):
        print '�Ұ�����ٻ'
    #���þ���Ϊ�˵���˽�з������Ա��ܹ�˽�з������ó���
    def Foo(self):
        self.__sha()  
    #����ͨ�����Եķ�ʽֱ�ӷ���˽���ֶ�
    @property
    def Thailand(self):
        return self.__Thailand   

b2 = provice('�ձ�','���˵�',True)

#==============˽�з�������ֱ�ӵ���=====================
#print b2.__Thailand


#==============˽���ֶε��������======================
#b2.show()

#==============˽�з������������======================
#b2.Foo()

#==============���Եķ�ʽֱ�ӷ���˽���ֶ�==================
print b2.Thailand


#==============ǿ�е�ֱ�ӵ���˽�з���==========================
b2._provice__sha()


'''

'''
#=====================ֻ����������д=============================
class provice(object):
    def __init__(self,name,leader,flag):
        self.Name = name
        self.Leader = leader
        self.__Thailand = flag
    #ֻ��
    @property
    def Thailand(self):
        return self.__Thailand  
    #��д
    @Thailand.setter
    def Thailand(self,value):
        self.__Thailand = value 
b2 = provice('�ձ�','���˵�',True)
print b2.Thailand
b2.Thailand = False
print b2.Thailand    
'''


'''
#========================setter�����õ�չʾ=====================
class test1():
    def __init__(self):
        self.__pravite = 'test 1'
        
    @property
    def Show(self):
            return  self.__pravite
 
class test2(object):
    def __init__(self):
        self.__pravite = 'test 2'
        
    @property
    def Show(self):
        return  self.__pravite
    @Show.setter
    def Show(self,value):
        self.__pravite =  value   

t1 = test1()
print t1.Show 
t1.Show = 'change 1'
print t1.Show

t2 = test2()
print t2.Show
t2.Show = 'change 2'
print t2.Show
'''



#=========================��������=================================
#���ͣ�python�ڲ����������Զ�ȥ���黹�к���������������������û���˾�ȥ֪ͨ��������ȥ����__del__,�ͷ��ڴ�
class Foo():
    def __init__(self):
        pass
    
    def __del__(self):
        print '������Ҫ�����ˡ���Ҫ�����һ�ε��ź�'
        
    


#=========================__call__����============================
#���ͣ�ִ�еķ���������

class Foo():
    def __init__(self):
        pass
    
    def __del__(self):
        print '������Ҫ�����ˡ���Ҫ�����һ�ε��ź�'
    def go(self):
        print 'һ�㷽����'
    def __call__(self):
        print 'ִ�е�call����'
f1 = Foo()      #�������������һ������ִ����ķ���
f1.go()         #��������һ��ִ�з���
f1()            #call������ִ�з���

#һ�㷽����
#ִ�е�call����
#������Ҫ�����ˡ���Ҫ�����һ�ε��ź�

