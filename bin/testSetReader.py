#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml
from xml.dom.minidom import parse
import xml.dom.minidom


class XML_PARSER(object):

    def __init__(self, xmlPath):
        self.tree = xml.dom.minidom.parse(xmlPath).documentElement

    def getSetDir(self):
        # 收集测试用例集，测试环境信息，运行策略
        setDir = {}
        setDir["cases"] = self.__getCase()
        setDir["environment"] = self.__getDevice()
        setDir["strategy"] = self.__strategy()

        return setDir

    def __getDevice(self):
        # 获取每个node tag的属性，转换成devices字典
        nodes = self.tree.getElementsByTagName('node')
        devices = {}
        for n in nodes:
            device = {}
            nodeID = n.getAttribute('id')
            for attributeName in n._attrs.keys():
                device[attributeName] = n._attrs[attributeName].value
            loginInfo = n.getElementsByTagName("loginInfo")[0]
            for attributeName in loginInfo._attrs.keys():
                device[attributeName] = loginInfo._attrs[attributeName].value

            devices[nodeID] = device
        return devices

    def __getCase(self):
        # 收集测试用例集
        cases = {}
        tests = self.tree.getElementsByTagName('test')
        for test in tests:
            script_path = test.firstChild.data
            case_name = script_path.split("\\")[-1]
            case_name = case_name.replace(".py", "")
            cases[case_name] = script_path
        return cases

    def __strategy(self):
        # 获取执行策略，
        strategyInfo = {}
        log = self.tree.getElementsByTagName('log')[0]
        strategyInfo['log_path'] = log.firstChild.data

        order = self.tree.getElementsByTagName('order')[0]
        strategyInfo['order'] = order.firstChild.data

        paralle = self.tree.getElementsByTagName('paralle')[0]
        strategyInfo['paralle'] = paralle.firstChild.data

        timeout = self.tree.getElementsByTagName('timeout')[0]
        strategyInfo['timeout'] = timeout.firstChild.data

        retype = self.tree.getElementsByTagName('retype')[0]
        strategyInfo['retype'] = retype.firstChild.data

        return strategyInfo


if (__name__ == "__main__"):
    pass
