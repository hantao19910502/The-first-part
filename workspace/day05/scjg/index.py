#!/usr/bin/env python
#_*_coding:utf-8_*_
from scjg.model.admin import Admin

def main():
    user = raw_input('Please input username:')
    pwd = raw_input('Please input password:')
    admin = Admin()
    result = admin.CheckValidate(user,pwd)
    if not result:
        print '�û��������������'
    else:
        print '����ɹ�'
     


if __name__ == '__main__':
    main()
else:
    print '���ɣ�'
    
    