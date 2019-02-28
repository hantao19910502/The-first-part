#!/usr/bin/env python
#_*_coding:utf-8_*_

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.1.140', 22, 'hantao', '123456')
stdin, stdout, stderr = ssh.exec_command('df')
print stdout.read()
ssh.close();