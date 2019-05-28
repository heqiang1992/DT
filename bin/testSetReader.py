#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml
from xml.dom.minidom import parse
import xml.dom.minidom


class XML_PARSER(object):

    def __init__(self, xmlPath):
        self.tree = xml.dom.minidom.parse(xmlPath).documentElement

    def getSetDir(self):
        setDir = {}
        setDir["cases"] = self.__getCase()
        setDir["nodes"] = self.__getDevice()
        setDir["log_path"] = self.__getLogPath()
        return setDir

    def __getDevice(self):

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
        cases = {}
        tests = self.tree.getElementsByTagName('test')
        for test in tests:
            script_path = test.firstChild.data
            case_name = script_path.split("\\")[-1]
            case_name = case_name.replace(".py", "")
            cases[case_name] = script_path
        return cases

    def __getLogPath(self):
        log = self.tree.getElementsByTagName('log')[0]
        log_path = log.firstChild.data
        return log_path


if (__name__ == "__main__"):
    pass
