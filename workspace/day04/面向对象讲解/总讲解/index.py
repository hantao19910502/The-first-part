#!/usr/bin/env python
#_*_coding:utf-8_*_

'''
class Person:
    xue = 'Ѫ'
    
class Alex:
    xx = 'û��û��'
    def __init__(self,name):
            self.name = name
p1 = Alex('����')
print p1.name
 
 '''
 
class province:
    #��̬�ֶ�
    mem = '�й���23��ʡ֮һ'
    def __init__(self,name,capital,leader):
        #��̬�ֶ�
        self.Name = name
        self.Capital = capital
        self.Leader = leader
    #��̬����
    def sport_meet(self):
        print self.Name + '���ڿ��˶���'
    #��̬����
    @staticmethod     #�����
    def Foo():
        print 'ÿ��ʡҪ̧ͷ���� '
    #����
    @property
    def Bar(self):
        print self.Name + '���ڴ��'
        return 'nothing'
hb = province('�ӱ�','ʯ��ׯ','�ϴ�')
#print hb.Name
#print hb.Capital 
#print hb.Leader         #���ڶ��� ===��̬�ֶ�self.xxx
#print province.mem      #������  ====��̬�ֶ�
sd = province('ɽ��','����','����')
#print sd
#�಻�ܷ��ʾ�̬�ֶ�
#print province.Name
#������Է��ʾ�̬�ֶ�
#print hb.mem         #�ֶεĵ��÷���
#hb.sport_meet()      #��̬�����ĵ��÷���
#province.Foo()       #��̬�����ĵ��÷���
hb.Bar                #���Եĵ��÷���
print hb.Bar


