#!/usr/bin/env python
#-*-coding:utf-8-*-

import paramiko

class Tool(object):

    def __init__(self):
        pass

    def connect(self,ip,user):
        try:
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.connect(ip,user)
            print "连接成功"
        except Exception as e:
            print "不能连接"

    def put(self,remote_file,local_file):
        sftp = paramiko.SFTPClient.from_transport(self.ssh.get_transport())
        sftp = self.ssh.open_sftp()
        sftp.put(local_file,remote_file)

    def get(self,local_file,remote_file):
        sftp = paramiko.SFTPClient.from_transport(self.ssh.get_transport())
        sftp = self.ssh.open_sftp()
        sftp.get(remote_file, local_file)

    def close(self):
        self.ssh.close()
        print "连接关闭"

#obj = Tool()
#getattr(obj,'connect')('192.168.1.140','pirate')
#getattr(obj,'put')('a','/tmp/a')