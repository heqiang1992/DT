#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.AutoEngine import AutoEngine
import pytest


# @pytest.fixture(scope="function")
# def hook():
#     print("before")
#     return True
# @pytest.mark.usefixtures("hook")


def test_003_demo():
    cls = AutoEngine()
    cls.login_node(id="1")
    res = cls.execute_cmd(nodeID="1", cmd="pcs status")
    # import re,time
    # name_list = re.findall("volume-.+\n", res)
    # for name in name_list:
    #     time.sleep(60)
    #     cls.execute_cmd(nodeID="1", cmd="rbd remove ssd_for_volume/%s" % name.replace("\r\n", ""))
    # res = cls.execute_cmd(nodeID="3", cmd="pcs status")
    # cls.log_info("回显是：%s" % res)

    raise Exception("raise error")

# def test_004_demo():
#
#     cls = AutoEngine()
#     cls.generate_http_connector(host="1")
#     res = cls.connector.swith_project(prj="demo")
#     # 必须指定镜像和网络
#     setting = {"disks": [
#             {"delete_on_termination": "no", "disk_bus": "virtio", "id": "win10qcow2",
#              "size": 20, "type": "image"}],"name": "云主机autocreate",
#                 "nics": "demo_net","os_type": "linux", "ram": 1024,
#                 "vcpus": 1}
#     cls.connector.create_vm(setting)


def test_005_demo():
    cls = AutoEngine()
    cls.login_node(id="3")
    res = cls.execute_cmd(nodeID="3", cmd={"cmd":"rm a.txt","waitstr":["‘a.txt’?","y"]})
