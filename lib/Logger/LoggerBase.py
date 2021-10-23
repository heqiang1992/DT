#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, re, logging
import time
import datetime
import traceback
from collections import Iterable

"""
20210910 日志模块重写，直接引用python标准库logging。

"""


class LoggerBase(object):

    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self._formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def _generate_StreamHandler(self, level):
        """
        使日志控制台输出
        :param level: logging.DEBUG,logging.INFO
        :return:
        """
        sh = logging.StreamHandler()
        sh.setLevel(level)
        sh.setFormatter(self._formatter)
        self.logger.addHandler(sh)

    def _generate_FileHandler(self, result_log, level):
        """
        不需要使用此函数，logging往控制台输入后，allure会记录
        :param result_log:
        :param level : logging.DEBUG,logging.INFO
        :return:
        """
        fh = logging.FileHandler(result_log)
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self._formatter)
        self.logger.addHandler(fh)


log = LoggerBase().logger
