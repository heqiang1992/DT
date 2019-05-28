#!/usr/bin/env python
# -*- coding: utf-8 -*-


from testSetReader import XML_PARSER
from interface.hyhive import HttpHyHive
from interface.CMD_AW import CmdWrapper
import traceback
from AutoAgent import xmlFile
from connectBase import Connection
from LoggerBase import LoggerBase
from WEBUI.WebTestBase import WebTestBase
import glo



def hy_hooker(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            try:
                glo._global_dict["Logger"].warning(traceback.format_exc())
                glo._global_dict["Logger"].case_down()
            except:
                pass
            finally:
                raise Exception(traceback.format_exc())
        else:
            glo._global_dict["Logger"].case_down()

    return wrapper


class AutoEngine():

    def __init__(self, **kwargs):
        parser = XML_PARSER(xmlFile)
        self.bedDir = parser.getBedDir()
        self.case_name = traceback.extract_stack()[-2][2]
        self.__log_initialization()

    def __log_initialization(self):
        name = self.bedDir["log_path"] + self.case_name
        log = LoggerBase(name)
        glo.set_value('Logger', log)
        return True

    def log_info(self, p):
        return glo._global_dict["Logger"].info(p)

    def log_warning(self, p):
        return glo._global_dict["Logger"].info(p)

    def login_node(self, **kwargs):
        id = kwargs.get("id", "1")
        node_info = self.bedDir["nodes"][id]
        node_info["log"] = glo._global_dict["Logger"]
        con = CmdWrapper(**node_info)
        channel_name = "channel" + id
        setattr(self, channel_name, con)

    def execute_cmd(self, nodeID, cmd):
        attr_name = "channel" + nodeID
        channel = getattr(self, attr_name, None)
        if channel:
            res = channel.nodeshell.exe_cmd(cmd)
        else:
            try:
                self.login_node(id=nodeID)
            except Exception as e:
                raise e
            else:
                res = self.execute_cmd(nodeID, cmd)
        res = res.encode("utf-8")
        return res

    def generate_web_driver(self, **kwargs):
        host = kwargs.get("host", "1")
        node_info = self.bedDir["nodes"][host]
        node_info["log"] = glo._global_dict["Logger"]
        self.driver = WebTestBase(**self.bedDir)
        return True

    def generate_http_connector(self, **kwargs):
        host = kwargs.get("host", "1")
        node_info = self.bedDir["nodes"][host]
        node_info["log"] = glo._global_dict["Logger"]
        self.connector = HttpHyHive(**node_info)
        return True
