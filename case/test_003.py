#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.AutoEngine import AutoEngine, hy_hooker
import lib.glo
import sys
import pytest


@pytest.fixture()
def hook():
    print("before")
    return True



# @pytest.mark.usefixtures("hook")
# @hy_hooker
# def test_003_one():
#     cls = AutoEngine()
#     cls.login_node(id="3")
#     res = cls.execute_cmd(nodeID="3", cmd="ll")
#     # res = cls.execute_cmd(nodeID="3", cmd="pcs status")
#     cls.log_info("回显是：%s" % res)
#
#     raise Exception("raise")


@pytest.mark.usefixtures("hook")
@hy_hooker
def test_004_one():

    cls = AutoEngine()
    cls.generate_http_connector(host="1")
    res = cls.connector.swith_project(prj="test")
    # 必须指定镜像和网络
    setting = {"disks": [
            {"delete_on_termination": "no", "disk_bus": "virtio", "id": "win10qcow2",
             "size": 20, "type": "image"}],"name": "云主机autocreate",
                "nics": "demo_net","os_type": "linux", "ram": 1024,
                "vcpus": 1}
    cls.connector.create_vm(setting)

