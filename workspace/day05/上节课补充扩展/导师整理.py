#!/usr/bin/env python
#_*_coding:utf-8_*_
#from optparse import Values
'''
#=====================����========================
#���������ʽ���е����Ե�����


#�������е�����ȫ�����ǿɶ���д��û��ֻ���Ĺ��ܣ�
class person:
    def __init__(self):
        self.__name = 'alex'
    @property
    def Name(self):
        return self.__name
p1 = person()
print p1.Name         #ͨ������Name,��ȡself.__name ��ֵ
p1.Name = 'xxx'       #ͨ������Name,����self.__name ��ֵ
print p1.Name


#�����������Ĭ�϶���ֻ����  �������Ҫ���ã���ô����Ҫ�ڴ���һ����װ��@xxx.setter���ε�����

class Person(object):
    def __init__(self):
        self.__name = 'alex'
    @property
    def Name(self):
        return self.__name
p1 = Person()
print p1.Name         #ͨ������Name,��ȡself.__name ��ֵ
#p1.Name = 'xxx' 
#print p1.Name         #Error ͨ������Name����self.__name ��ֵ��ʱ�򣬾ͻ����
#AttributeError: can't set attribute

'''
#���������ô���ĺô��Ƿ�ֹ˽�б������޸ģ����еĶ����ֻ�ܶ�ȡ�����ܱ��޸ġ��������˵Ļ���ֻ�ܿ������޸ģ�
'''
    @Name.setter
    def Name(self,value):
        self.__name = value
        '''     
#����һ�����Ϳ���ͨ���������޸���
#�������е�p1.Name = 'xx' �Ͳ��ᱨ����


#Ӧ�ó���
class Person(object):
    def __init__(self,gene,clothes):
        self.__gene = gene
        self.__clothes = clothes
        
    @property
    def Gene(self):
            return self.__gene
    @property
    def Clothes(self):
            return self.__clothes
    @Clothes.setter
    def Clothes(self,value):
            self.__clothes = value
            
#��������ΪAB���ˣ��·��ǱȻ���
b1 = Person('AB','bikini')
#print b1.Gene

#=================���¶���ᱨ��=================
b1.Gene = 'CD'
print b1.Gene
#AttributeError: can't set attribute

#=================���¶���====================
print b1.Clothes
b1.Clothes = 'yiban'
print b1.Clothes

#˽�з�������ֱ�Ӹ��ģ���Ҫͨ��@xxxx.setter��˽�з���һ����д��Ȩ�޲���ʹ��






