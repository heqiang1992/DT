#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, re
import time
import datetime
import html_template
import traceback
from collections import Iterable


class LoggerBase(object):

    def __init__(self, name):
        self.generate_case_log(name)

    def generate_case_log(self, name):
        date = self.generate_time_postfix()
        self.dir_path = name + date
        os.mkdir(self.dir_path)
        self.f = open(self.dir_path + "\%s.html" % date, "a+")
        self.f.write(html_template.template_head)
        return True

    @classmethod
    def generate_time_postfix(self):
        TIMESTAMP = datetime.datetime.fromtimestamp(time.time())
        DATE = datetime.datetime.strftime(TIMESTAMP, "%Y_%m_%d_%H_%M_%S")
        DATE = str(DATE).replace(" ", "_")
        return DATE

    def info(self, p):
        timestamp = self.generate_time_postfix()
        stream = re.sub("time", timestamp.replace("_","-"), html_template.template_info)
        path = "<br>".join(traceback.format_list(traceback.extract_stack())[-5:-2])
        stream = re.sub("path", path, stream)
        if isinstance(p, (list, tuple)):
            p = ",".join(p)
        else:
            p = str(p.encode("utf-8"))
        stream = re.sub("content", p.replace("\n", "<br>"), stream)
        self.f.write(stream)

    def warning(self, p):
        timestamp = self.generate_time_postfix()
        stream = re.sub("time", timestamp, html_template.template_warning)
        path = "<br>".join(traceback.format_list(traceback.extract_stack())[-5:-2])
        stream = re.sub("path", path, stream)
        if isinstance(p, (list, tuple)):
            p = ",".join(p)
        else:
            p = str(p)
        stream = re.sub("content", p.replace("\n", "<br>"), stream)
        self.f.write(stream)

    def case_down(self):
        self.f.write(html_template.template_end)
        self.f.close()
