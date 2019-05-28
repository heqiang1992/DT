#!/usr/bin/env python
# -*- coding: utf-8 -*-


import re
import requests
import json
from lib.connectBase import Connection
import RequestData
from CMD_AW import CmdWrapper


class HttpHyHive(CmdWrapper):

    def __init__(self, **kwargs):
        super(HttpHyHive, self).__init__(**kwargs)
        self.nodeInfo = kwargs
        self.__log = kwargs.get("log")
        self.api = "http://%s/api/hyhive" % kwargs.get("ip")
        self.webuser = kwargs.get("webuser")
        self.webpwd = kwargs.get("webpwd")
        self.baseurl = "http://%s/api/hyhive" % self.nodeInfo["ip"]
        self.login_admin()

    def login_admin(self):
        url = self.baseurl + RequestData.AUTH_LOGIN
        data = {"username": self.webuser, "password": self.webpwd}
        con = requests.post(url, data=json.dumps(data), headers=RequestData.headers)
        if con.status_code == 200 and re.search("token", con.content):
            print (">>>>>> login success <<<<<<")
            self.__log.info(">>>>>> login success <<<<<<")
        self.con = con
        return True

    def swith_project(self, prj):
        prj_id = self.get_project_id(prj)
        data = {"project_id": prj_id}
        url = self.baseurl + RequestData.AUTH_PROJECT_RESCOPE
        con = requests.post(url, data=json.dumps(data), cookies=self.con.cookies, headers=RequestData.headers)
        if con.status_code == 200 and re.search(prj, con.content):
            print (">>>>>> switch project success <<<<<<")
            self.__log.info(">>>>>> switch project success <<<<<<")
        self.con = con
        return con.content

    def create_vm(self, setting):
        """
        just support type :image  now.
        data contain default sets , setting must contain :disks,name,nics,ostype
        :param setting:
        :return:
        """
        glance_id = self.get_glance_id(setting["disks"]["id"])
        nit_id, subnet_id = self.get_nics_id(setting["nics"])
        setting["disks"]["id"] = glance_id
        setting["nics"] = [{"net-id": nit_id, "subnet-id": subnet_id}]
        data = {"auto_start": 0, "count": 1, "disks": None,
                "drs_enabled": 0, "host": "", "name": None,
                "nics": None, "numa_enabled": False, "os_type": None, "pci_name": "",
                "ram": 1024, "security_groups": ["default"], "vcpus": 1, "volume_type": "infinity"}
        data.update(setting)
        url = self.baseurl + RequestData.VM_CREATE
        print (json.dumps(data))
        # con = requests.post(url, data=json.dumps(data), cookies=self.con.cookies, headers=RequestData.headers)
        # return con.content

    def check_operation_log(self):
        url = "http://%s/api/hyhive/log/operation/list" % (self.nodeInfo["ip"])
        data = {"lang": 1, "page": 1, "page_size": 10}
        con = requests.post(url, data=json.dumps(data), cookies=self.con.cookies, headers=self.headers)
        self.__log.info(con.status_code)
        self.__log.info(con.content)


