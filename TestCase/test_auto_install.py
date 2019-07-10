#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.AutoEngine import AutoEngine
import time
import re

"""
1.安装部署infinity
2.安装部署hyhive
"""


def test_auto_install():
    package_name = "infinity-3.2.1.tgz"
    soft_dir = package_name.strip(".tgz")
    cls = AutoEngine()
    autoConfigPool = True

    # cls.log_info("获取infinity软件包,放入指定目录")
    for id in range(1, 4):
        id = str(id)
        cls.login_node(id="%s" % id)
        cls.wrapper_excute(nodeID="%s" % id, wrapperName="resolv_fingerprint", kargs={"ip": "10.0.6.138"})

        cls.execute_cmd(nodeID="%s" % id, cmd={"cmd": "sftp root@10.0.6.138",
                                               "waitstr": ["password:", "123456", "sftp>",
                                                           "get /package/%s /root/" % package_name, "100%",
                                                           "exit"]}, timeout=120)
        cls.execute_cmd(nodeID="%s" % id, cmd={"cmd": "sftp root@10.0.6.138",
                                               "waitstr": ["password:", "123456", "sftp>",
                                                           "get /package/LocalCdrom.repo /etc/yum.repos.d/",
                                                           "100%", "exit"]}, timeout=60)

        time.sleep(5)
        cls.execute_cmd(nodeID="%s" % id, cmd="tar -zxvf %s" % package_name)

        cls.execute_cmd(nodeID="%s" % id, cmd="yum clean all")

        res = cls.execute_cmd(nodeID="%s" % id, cmd="ll /root/%s" % soft_dir)
        if not re.search(soft_dir + ".iso", res):
            raise Exception("no iso found !")

        cls.execute_cmd(nodeID="%s" % id, cmd="mount /root/%s/%s.iso /media/" % (soft_dir, soft_dir))

    cls.log_info(">>> 配置ssh互通 <<<")

    cls.execute_cmd(nodeID="1", cmd={"cmd": "sh /root/%s/expand_pre.sh" % soft_dir,
                                     "waitstr": ["Nodes Count:", "3", "[y|n]", "n", "node1:",
                                                 cls.bedDir["nodes"]["1"]["ip"], "node2:",
                                                 cls.bedDir["nodes"]["2"]["ip"],
                                                 "node3:", cls.bedDir["nodes"]["3"]["ip"], "confirm [y|n]", "y",
                                                 "node1", "node1", "node2", "node2", "node3", "node3", "confirm [y|n]",
                                                 "y", "do it <y>, skip <n>", "y", "connecting (yes/no)?", "yes",
                                                 "password:", cls.bedDir["nodes"]["1"]["password"],
                                                 "(/root/.ssh/id_rsa)", "", "empty for no passphrase", "",
                                                 "same passphrase again", "", "password:",
                                                 cls.bedDir["nodes"]["1"]["password"], "connecting (yes/no)?", "yes",
                                                 "password:", cls.bedDir["nodes"]["2"]["password"],
                                                 "(/root/.ssh/id_rsa)", "", "empty for no passphrase", "",
                                                 "same passphrase again", "", "password:",
                                                 cls.bedDir["nodes"]["2"]["password"], "connecting (yes/no)?", "yes",
                                                 "password:", cls.bedDir["nodes"]["3"]["password"],
                                                 "(/root/.ssh/id_rsa)", "", "empty for no passphrase", "",
                                                 "same passphrase again", "", "password:",
                                                 cls.bedDir["nodes"]["3"]["password"], "password:",
                                                 cls.bedDir["nodes"]["1"]["password"], "password:",
                                                 cls.bedDir["nodes"]["2"]["password"], "password:",
                                                 cls.bedDir["nodes"]["3"]["password"], "password:",
                                                 cls.bedDir["nodes"]["1"]["password"], "password:",
                                                 cls.bedDir["nodes"]["1"]["password"], "password:",
                                                 cls.bedDir["nodes"]["2"]["password"], "password:",
                                                 cls.bedDir["nodes"]["2"]["password"], "password:",
                                                 cls.bedDir["nodes"]["3"]["password"], "password:",
                                                 cls.bedDir["nodes"]["3"]["password"], "password:",
                                                 cls.bedDir["nodes"]["2"]["password"], "password:",
                                                 cls.bedDir["nodes"]["3"]["password"]]}, timeout=60)

    time.sleep(10)
    cls.log_info(">>> 安装infinity <<<")
    for id in range(1, 4):
        id = str(id)
        cls.execute_cmd(nodeID="%s" % id, cmd={
            "cmd": "yum group install @^Infinity --exclude=infinitycore-fs-client --disablerepo=* --enablerepo=InfiRom",
            "waitstr": ["Is this ok", "y", "Complete!", ""]}, timeout=600)
    time.sleep(60)
    for id in range(1, 4):
        id = str(id)
        cls.execute_cmd(nodeID="%s" % id, cmd="rpm -ivh /media/infinitycore-fs-client*rpm --force")

    time.sleep(80)

    cls.log_info(">>> 配置：infinity <<<")
    cls.generate_web_driver()
    # cls.webdriver.open_url("http://10.0.30.75/infinity3")
    # cls.webdriver.login_infinity()
    cls.webdriver.open_url("http://10.0.30.75/sysdbconf")

    cls.webdriver.login_infinity()
    time.sleep(5)
    cls.webdriver.send_keys(element="addSysdbNode", by="id", conment=",".join(
        [cls.bedDir["nodes"]["1"]["ip"], cls.bedDir["nodes"]["2"]["ip"], cls.bedDir["nodes"]["3"]["ip"]]))
    cls.webdriver.click(element="//*[@id=\"sysdbAddModal\"]/div/div/div[1]/button", by="xpath")
    time.sleep(120)
    if not cls.webdriver.wait_element(element="pname", by="name"):
        raise Exception("sysdb 节点信息添加失败")

    cls.webdriver.open_url("http://10.0.30.75/infinity3/nodeinfo")
    cls.webdriver.login_infinity()
    cls.webdriver.click(element="add_node", by="id")
    time.sleep(3)
    cls.webdriver.send_keys(element="add_aNewSip", by="id", conment=",".join(
        [cls.bedDir["nodes"]["1"]["ip"], cls.bedDir["nodes"]["2"]["ip"], cls.bedDir["nodes"]["3"]["ip"]]))

    cls.webdriver.click(element="//*[@id=\"addNodeModal\"]/div/div/div[1]/button[2]", by="xpath")

    time.sleep(120)
    if not cls.webdriver.wait_element(element="/html/body/div[2]/nav/div/ul/li[3]/a/span[2]", by="xpath"):
        raise Exception("平台节点 添加失败 啦")

    cls.log_info(">>> license 授权 <<<")
    cls.webdriver.click_into_cluster_management()
    cls.webdriver.click(element="/html/body/div[2]/div[1]/ul/li[2]/a", by="xpath")
    time.sleep(20)
    # cls.webdriver.move_to_element(element="/html/body/div[2]/div[2]/div/div[1]/div/div/div[1]/span[2]/a", by="xpath")
    cls.webdriver.ActionChains_double_click(
        element="/html/body/div[2]/div[2]/div/div[1]/div/div/div[1]/span[2]/span/a[1]", by="xpath")
    time.sleep(10)

    cls.log_info(">>> 配置向导 <<<")
