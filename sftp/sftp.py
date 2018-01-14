#!/usr/bin/env python
# coding:utf-8

import paramiko


class MySFTP(object):
    def __init__(self, host, port, user, pwd):
        self.host = host
        self.port = port
        self.user = user
        self.pwd = pwd
        self.transport = None
        self._connect()

    def _connect(self):
        self.transport = paramiko.Transport(sock=(self.host, self.port))
        self.transport.connect(username=self.user, password=self.pwd)

    def download_file(self, remote_file, local_file):
        channel = paramiko.SFTPClient.from_transport(self.transport)
        channel.get(remote_file, local_file)
        channel.close()
        return 1
    
    def __del__(self):
        self.transport.close()    
       

if __name__ == '__main__':
    obj = MySFTP("127.0.0.1", 22, 'fred', 'charging')
    obj.download_file('/home/fred/workspace/test/a.t', '/home/fred/workspace/test/c.t')
""" 
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())#第一次登录的认证信息
ssh.connect(hostname='192.168.0.3', port=22, username='fred', password='charging')

sftp = paramiko.SFTPClient.from_transport(transport)
#channel = ssh.get_transport().open_session()
#a = channel.exec_command('ls -lart /')
#print "exit status: %s" % channel.recv(10000)

ssh.close()
"""
