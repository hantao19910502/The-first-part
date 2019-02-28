#!/usr/bin/env python
#_*_coding:utf-8_*_

class person:
    def __init__(self,name,gene,weight):
        self.Name = name
        self.Gene = gene
        self.Weight = weight
        self.Age = None
    def talk(self):
        print 'xxxxxxxxxxxxxxxxxxx'
    def fight(self,vaule):
        if self.Weight > vaule:
            print '´òËû'
        else:
            print '¸Ï½ôÅÜ'
p1 = person('hantao','a',120)
p1.Age = 20
print p1.Age 
p2 = person('hanzhiwei','b',140) 
p1.fight(p2.Weight)        
    
                