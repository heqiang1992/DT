#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .connectBase import Connection, SFTP
import re


class CmdWrapper(object):

    def __init__(self, **kwargs):
        """

        :param kwargs: nodeinfo  not bedinfo
        """
        self.nodeshell = Connection(**kwargs)

    def __extract_string(self, materials, head=False):
        """
        :param head  TRUE:get the first string
        cut out target string like this :
        | name        | demo                             |
        :return: string
        """
        if head:
            inter = materials.split("|")
        else:
            inter = materials.split("|")[::-1]
        for i in inter:
            if re.search("\w+", i):
                return i.strip()

    def get_glance_id(self, name):
        """
        get id of the target glance
        :param name: glance name
        :return:
        """

        self.nodeshell.exe_cmd(". keystone_admin.rc")
        res = self.nodeshell.exe_cmd("glance image-list")
        for line in res.split("\n"):
            if re.search("\s%s\s" % name, res):
                glance_id = self.__extract_string(line, head=True)
                return glance_id

    def get_nics_id(self, name):
        """
        get id of the target network
        :return:
        """

        self.nodeshell.exe_cmd(". keystone_admin.rc")
        res = self.nodeshell.exe_cmd("neutron net-list")
        for line in res.split("\n"):
            if re.search("\s%s\s" % name, res):
                nic_id = self.__extract_string(line, head=True)
                subnets = self.__extract_string(line)
                return nic_id, subnets

    def get_project_id(self, name):
        """
        get id of the target project
        :return:
        """
        self.nodeshell.exe_cmd(". keystone_admin.rc")
        res = self.nodeshell.exe_cmd("openstack project show %s" % name)
        ID = re.search("\sid\s+\|\s+\w+\s", res).group(0)
        ID = self.__extract_string(ID)
        return ID

    def sftp_file_to_linux(self, **kwargs):
        """

        :return:
        """
        sftp_host = kwargs.get("ip", "10.0.6.138")
        localpath = kwargs.get("localpath", "/root/")
        remotepath = kwargs.get("remotepath")
        username = kwargs.get("username", "root")
        password = kwargs.get("password", "123456")
        port = kwargs.get("port", 22)
        client = SFTP(sftp_host, username, password)

    def resolv_fingerprint(self, **kwargs):
        ip = kwargs.get("ip")
        try:
            res = self.nodeshell.exe_cmd("sftp root@%s" % ip)
            if "you want to continue connecting (yes/no)?" in res:
                res = self.nodeshell.exe_cmd("yes")
                if "password:" in res:
                    print("fingerprint ok")
        except:
            print("fingerprint fault ~~~~~~")
        finally:
            self.nodeshell.exe_cmd("\x03")
