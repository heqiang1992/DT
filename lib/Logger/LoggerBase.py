#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, re
import time
import datetime
from .html_template import *
import traceback
from collections import Iterable


class LoggerBase(object):

    def __init__(self, name):
        self.generate_case_log(name)

    def generate_case_log(self, name):
        date = self.generate_time_postfix()
        self.dir_path = name + date
        os.mkdir(self.dir_path)
        self.file_path = self.dir_path + "\%s.html" % date
        self.f = open(self.file_path, "a+")
        self.f.write(template_head)
        return True

    @classmethod
    def generate_time_postfix(self):
        TIMESTAMP = datetime.datetime.fromtimestamp(time.time())
        DATE = datetime.datetime.strftime(TIMESTAMP, "%Y_%m_%d_%H_%M_%S")
        DATE = str(DATE).replace(" ", "_")
        return DATE

    def info(self, p):
        timestamp = self.generate_time_postfix()
        stream = re.sub("time", timestamp.replace("_","-"), template_info)
        path = "<br>".join(traceback.format_list(traceback.extract_stack())[-5:-2])
        # stream = re.sub("path", str(path), stream)
        stream = stream.replace("path", path)
        if isinstance(p, (list, tuple)):
            p = ",".join(p)
        else:
            p = str(p)
        stream = stream.replace("content", p.replace("\n", "<br>"))
        self.f.write(stream)

    def warning(self, p):
        timestamp = self.generate_time_postfix()
        stream = re.sub("time", timestamp, template_warning)
        path = "<br>".join(traceback.format_list(traceback.extract_stack())[-5:-2])
        # stream = re.sub("path", str(path), stream)
        stream = stream.replace("path", path)
        if isinstance(p, (list, tuple)):
            p = ",".join(p)
        else:
            p = str(p)
        stream = stream.replace("content", p.replace("\n", "<br>"))
        self.f.write(stream)

    def case_down(self):
        self.f.write(template_end)
        self.f.close()

    def __del__(self):
        self.case_down()