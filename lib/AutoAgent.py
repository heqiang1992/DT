#!/usr/bin/env python
# -*- coding: utf-8 -*-


from testSetReader import XML_PARSER
import sys, os
import pytest
from lib.LoggerBase import LoggerBase

xmlFile = sys.argv[1]

class AutoAgent():

    def __init__(self):
        self.__getSetInfo()
        self.start()

    def __pytest_initialization(self):
        pass

    def __getSetInfo(self):
        parser = XML_PARSER(xmlFile)
        self.setDir = parser.getSetDir()

    def start(self):
        """
        调用pytest.main()执行目标脚本，生成html报告
        :return:
        """
        main_args = []
        timestamp = LoggerBase.generate_time_postfix()
        report_arg = "--html=%s.html" % (self.setDir["log_path"] + timestamp)
        main_args.append(report_arg)
        main_args.append("-s")   # pytest打开调试模式
        main_args.extend(self.setDir["cases"].values())
        pytest.main(main_args, [self.__plugins()])

    def __plugins(self):
        """
        执行自定义或额外的插件
        :return:
        """
        pass


if (__name__ == "__main__"):
    AutoAgent()
