#!/usr/bin/env python
#_*_coding:utf-8_*_

import paramiko

private_key_path = '/home/hantao/.ssh/id_rsa'
key = paramiko.RSAKey.from_private_key_file(private_key_path)

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.1.140', 22, username='root',pkey=key)

stdin, stdout, stderr = ssh.exec_command('ifconfig virbr0 | awk -F\'[ :]+\' \'NR==2{print $4}\'')
print stdout.read()
ssh.close()