#!/usr/bin/env python
#!_*_coding:utf-8 _*_

print_info=input('Please input you want to input:')
count=0
while count <1000000:
   #print 'loop:',count
   if count == print_info:
      print 'loop22:',count
      chois=raw_input('you want to count:y/n')
      if chois  == 'n':
         break
      else:
          while print_info <=count:
             print_info=input('Please input you want to input:')
             #while print_info <= count:
             print "You are NO"
             #continue
   else:
      print 'loop:',count
   count +=1
else:
   print 'loop:',count
	
	
