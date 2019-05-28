#!/usr/bin/env python
# -*- coding: utf-8 -*-


import paramiko, socket, telnetlib, ftplib
import threading, os, re, sys
import time


class Connection(object):

    def __init__(self, **kwargs):

        self.ip = kwargs.get("ip")
        self.username = kwargs.get("username", "root")
        self.password = kwargs.get("password", "daemon")
        self.port = kwargs.get("port", 22)
        self.log = kwargs.get("log", None)
        if self.log == None: print " NO runlog to write !!!"
        self.channel = self.__createChannel()

    def __createChannel(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.ip, int(self.port)))  # tuple
        ssh = paramiko.Transport(sock)
        ssh.connect(username=self.username, password=self.password)
        print("<<<<<<  connect to %s success.  >>>>>>>" % self.ip)
        channel = ssh.open_session()
        channel.get_pty(width=200, height=200)
        channel.invoke_shell()
        channel.settimeout(10)
        return channel

    def __send(self, channel, cmd):
        if not channel.active:
            print ("CONNECT CLOSED... RECONNECTING ...")
            channel = self.__createChannel()
            self.channel = channel
        return channel.send(cmd + "\n")

    def __receive(self, channel, timeout=30):
        waitList = [r"]#", r":/>"]
        info = []
        timestamp = time.time()
        while True:
            try:
                res = channel.recv(1024)
            except Exception as e:
                print (e)
                break
            info.append(res.decode("utf-8"))
            for waitStr in waitList:
                if re.search(waitStr, res):
                    break
            if time.time() > timestamp + timeout:
                break
        p = "\n".join(info)
        print(p)
        if self.log:
            self.log.info(p)
        return p

    def exe_cmd(self, cmd):
        self.__send(self.channel, cmd)
        stdout = self.__receive(self.channel)
        return stdout

    def close(self):
        self.channel.close()

if __name__ == "__main__":
    pass
