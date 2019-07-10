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
        if self.log == None: print(" NO runlog to write !!!")
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
            print("CONNECT CLOSED... RECONNECTING ...")
            channel = self.__createChannel()
            self.channel = channel
        return channel.send(cmd + "\n")

    def handle_waitstr(self, str):
        s = str.replace("]", "\]").replace("[", "\[").replace("|", "\|").replace("{", "\{").replace("}", "\}")
        return s

    def __receive(self, channel, **kwargs):

        waitList = kwargs.get("waitList", [r"]#", r":/>"])
        timeout = kwargs.get("timeout", 60)
        writeLog = kwargs.get("writeLog", True)
        info = []
        timestamp = time.time()
        while True:
            try:
                res = channel.recv(1024)
            except Exception as e:
                print(e)
                break
            res = res.decode("utf-8")
            info.append(res)
            for waitStr in waitList:
                if waitStr in res:
                    break
            if time.time() > timestamp + timeout:
                print("wait ending sign failed ......")
                print(info)
                break
        p = "".join(info)
        print(p)
        if self.log and writeLog:
            self.log.info(p)
        return p

    def exe_cmd(self, cmd, timeout=60):
        if isinstance(cmd, dict):
            stdout = ""
            if len(cmd["waitstr"]) % 2 == 1:
                self.__send(self.channel, cmd["cmd"])
                for index, field in enumerate(cmd["waitstr"]):
                    if index == 0:
                        stdout += self.__receive(self.channel, waitList=[field], writeLog=False, timeout=timeout)
                    elif index % 2 == 1:
                        self.__send(self.channel, cmd=field)
                        stdout += self.__receive(self.channel, waitList=cmd["waitstr"][index + 1], writeLog=False,
                                                 timeout=timeout)
                stdout += self.__receive(self.channel, writeLog=False, timeout=timeout)
            else:
                self.__send(self.channel, cmd["cmd"])
                for index, field in enumerate(cmd["waitstr"]):
                    if index == 0:
                        stdout += self.__receive(self.channel, waitList=[field], writeLog=False, timeout=timeout)
                    elif index == len(cmd["waitstr"]) - 1:
                        self.__send(self.channel, cmd=field)
                    elif index % 2 == 1:
                        self.__send(self.channel, cmd=field)
                        stdout += self.__receive(self.channel, waitList=cmd["waitstr"][index + 1], writeLog=False,
                                                 timeout=timeout)
                stdout += self.__receive(self.channel, writeLog=False, timeout=timeout)
            self.log.info(stdout)
        else:
            self.__send(self.channel, cmd)
            stdout = self.__receive(self.channel, timeout=timeout)
        return stdout

    def close(self):
        self.channel.close()


class SFTP(object):

    def __init__(self, ip, username, password, port=22):
        self.con = self.__createChannel(ip, username, password, port)

    def __createChannel(self, ip, username, password, port=22):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, int(port)))  # tuple
        ssh = paramiko.Transport(sock)
        ssh.connect(username=username, password=password)
        print("<<<<<<  connect to %s success.  >>>>>>>" % ip)
        sftp = paramiko.SFTPClient.from_transport(ssh)
        return sftp

    def get(self, remotepath, localpath):
        print("上传文件: %s" % remotepath)
        self.con.get(remotepath, localpath)

    def put(self, remotepath, localpath):
        print("下载文件: %s" % remotepath)
        self.con.put(remotepath, localpath)


if __name__ == "__main__":
    pass
