#!/usr/bin/env python
# -*- coding: utf-8 -*-


from bin.testSetReader import XML_PARSER
import sys, os
import pytest
from lib import conmonMethod
from lib import glo

# 传参xml
xmlFile = sys.argv[1]


class AutoAgent():

    def __init__(self):
        self.__getSetInfo()
        self.start()

    def __getSetInfo(self):
        parser = XML_PARSER(xmlFile)
        self.setDir = parser.getSetDir()
        glo.set_value('xml', self.setDir)

    def start(self):
        """
        调用pytest.main()执行目标脚本，生成html报告
        :return:
        """
        """pytest打开调试模式,禁用告警,失败时打印局部变量"""
        """retype 失败时打印信息的详细程度"""
        retype = self.setDir["strategy"]["retype"]
        main_args = ["-s", "--disable-warnings", "-l", "--color=yes", "--tb=%s" % retype]

        """timeout 测试套中timeout参数值大于0时，设置超时时间为timeout参数的值"""
        timeout = self.setDir["strategy"]["timeout"]
        if timeout != '0':
            main_args.append("--timeout=%s" % timeout)

        """设置用例执行顺序，order值不为0时，随机执行测试套中用例"""
        order = self.setDir["strategy"]["order"]
        if order != 0:
            main_args.append("--random-order")

        """并发模式设置并发度，paralle值为0时采用串行方式，大于0时，采用并行方式，值为并发度"""
        paralle = self.setDir["strategy"]["paralle"]
        if paralle != '0':
            main_args.append("-n %s" % paralle)

        timestamp = conmonMethod.generate_time_postfix()

        # 本地形成日志文件
        # result_log = os.path.abspath(os.path.join(os.getcwd(), "..", "report", "test_result.log"))
        # main_args.append("--resultlog=%s"%result_log)
        # report_arg = "--html=%s.html" % (self.setDir["log_path"] + timestamp)
        # main_args.append(report_arg)  #生成html报告

        """指定allure配置"""
        result_dir = os.path.abspath(os.path.join(os.getcwd(), "..", "result"))
        main_args.append("--alluredir=%s" % result_dir)

        # main_args.append("--clean-alluredir")  #不能参数清，准备改为多次运行pytest.mian
        def cleardir(result_dir):
            for i in os.listdir(result_dir):
                file = os.path.join(result_dir, i)
                os.remove(file)

        cleardir(result_dir)

        """指定测试集 ;运行"""
        for name, path in self.setDir["cases"].items():
            run_cmd = main_args
            run_cmd.append(path)
            pytest.main(run_cmd)

        # html日志
        alluredir = os.path.join(os.getcwd(), "..", "report", timestamp)
        os.mkdir(alluredir)
        os.system("allure generate %s/ -o %s/ --clean" % (result_dir, alluredir))


if (__name__ == "__main__"):
    AutoAgent()
