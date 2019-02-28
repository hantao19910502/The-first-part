#!/usr/bin/env python
#_*_coding:utf-8_*_


import sys
retry_limit = 3
retry_count = 0
account_file = 'accounts.txt'
lock_file = 'account_lock.txt'

while retry_count < retry_limit:
    username = raw_input('UserName:')
    lock_check = file(lock_file)


    for line in lock_check.readlines():
        if username == line:
            sys.exit('User is lock,username')
    password = raw_input('PassWard')
    f = file(account_file,'rb')
    match_flag = False

    for line in f.readlines():
        user,passwd = line.strip('\n').split()
        if username == user and password == passwd:
            print 'March',username 
            match_flag = True
      
            
            f.close()
    if match_flag == False:
        print 'User unmatched'
        retry_count +=1
    else:
        print "welcome 0"
        exit()
else:
  print 'You accout  is lock!'
  f = file(lock_file,'ab')
  f.write(username)
  f.close()