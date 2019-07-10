#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from lib.AutoEngine import AutoEngine
# import pytest
# from lib.interface.connectBase import Connection
import threading

import paramiko, socket
import threading, os, re, sys
import time


class Connection(object):

    def __init__(self, **kwargs):

        self.ip = kwargs.get("ip")
        self.username = kwargs.get("username", "root")
        self.password = kwargs.get("password", "daemon")
        self.port = kwargs.get("port", 22)
        self.log = kwargs.get("log", None)
        # if self.log == None: print(" NO runlog to write !!!")
        self.channel = self.__createChannel()

    def __createChannel(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.ip, int(self.port)))  # tuple
        ssh = paramiko.Transport(sock)
        ssh.connect(username=self.username, password=self.password)
        # print("<<<<<<  connect to %s success.  >>>>>>>" % self.ip)
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
                if re.search(waitStr, res):
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

    def exe_cmd(self, cmd, timeout=None):
        if isinstance(cmd, dict):
            stdout = ""
            if len(cmd["waitstr"]) % 2 == 1:
                self.__send(self.channel, cmd["cmd"])
                for index, field in enumerate(cmd["waitstr"]):
                    if index == 0:
                        stdout += self.__receive(self.channel, waitList=[field], writeLog=False)
                    elif index % 2 == 1:
                        self.__send(self.channel, cmd=field)
                        stdout += self.__receive(self.channel, waitList=cmd["waitstr"][index + 1], writeLog=False)
                stdout += self.__receive(self.channel, writeLog=False)
            else:
                self.__send(self.channel, cmd["cmd"])
                for index, field in enumerate(cmd["waitstr"]):
                    if index == 0:
                        stdout += self.__receive(self.channel, waitList=[field], writeLog=False)
                    elif index == len(cmd["waitstr"]) - 1:
                        self.__send(self.channel, cmd=field)
                    elif index % 2 == 1:
                        self.__send(self.channel, cmd=field)
                        stdout += self.__receive(self.channel, waitList=cmd["waitstr"][index + 1], writeLog=False)
                stdout += self.__receive(self.channel, writeLog=False)
            self.log.info(stdout)
        else:
            self.__send(self.channel, cmd)
            stdout = self.__receive(self.channel)
        return stdout

    def close(self):
        self.channel.close()


ip_24 = "192.168.0."
ip_range = [3, 54]  # 要求同网段
cmd = "fio -filename=/dev/vdb -direct=1 -iodepth 16 -thread -rw=randread -ioengine=libaio -bs=4k -size=5G -numjobs=16 -runtime=300 -group_reporting -name=mytest>/root/hhh.log"
cmd_d = "ls"
cmd_cat = "cat /root/hhh.log"
import time


def demo(ip, num):
    t = Connection(ip=ip, password="123456")
    c = cmd.replace("hhh", str(num))
    t.exe_cmd(c)
    time.sleep(300)


def test_linuxVM_send_cmd():
    for i in range(ip_range[0], ip_range[1]):
        if i == 50:
            continue
        ip = ip_24 + str(i)
        t = threading.Thread(target=demo, args=(ip, i))
        t.setDaemon(True)
        print(ip)
        t.start()

    time.sleep(600)


def test():
    fault = []
    success = []
    for i in range(ip_range[0], ip_range[1]):
        if i == 50:
            continue
        ip = ip_24 + str(i)
        t = Connection(ip=ip, password="123456")
        res = t.exe_cmd("ll")
        if "total" in res:
            print(" %s connect success." % ip)
            success.append(ip)
        else:
            fault.append(ip)
            print(p.read())
        t.close()
    print("\n".join(fault))
    print("fault: %s" % str(len(fault)))
    print("success: %s" % str(len(success)))


def print_data():
    f = open("C:\\file\\test.txt", "a+")
    for i in range(ip_range[0], ip_range[1]):
        if i == 50:
            continue
        ip = ip_24 + str(i)
        t = Connection(ip=ip, password="123456")
        c = cmd_cat.replace("hhh", str(i))
        res = t.exe_cmd(c)
        import re
        if re.search("read: IOPS=\d+", res):
            s = re.search("read: IOPS=\d+", res).group(0)
            print(ip + " :  " + s)
            f.write(s.split("=")[1] + "\n")
        else:
            print("err : %s" % ip)


if __name__ == "__main__":
    if sys.argv[1] == "test":
        test()
    elif sys.argv[1] == "start":
        test_linuxVM_send_cmd()
    elif sys.argv[1] == "get":
        print_data()
    elif sys.argv[1] == "delete":
        delete_file()

