#!/usr/bin/env python
# -*- coding: utf-8 -*-


from lib.interface.hyhive import HttpHyHive
from lib.interface.CmdWrapper import CmdWrapper
import traceback
from lib.Logger.LoggerBase import LoggerBase
from lib.WEBUI.WebTestBase import WebTestBase
from lib import glo


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
        self.bedDir = glo._global_dict["xml"]
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

    def execute_cmd(self, nodeID, cmd, timeout=60):
        attr_name = "channel" + nodeID
        channel = getattr(self, attr_name, None)
        if channel:
            res = channel.nodeshell.exe_cmd(cmd,timeout)
        else:
            try:
                self.login_node(id=nodeID)
            except Exception as e:
                raise e
            else:
                res = self.execute_cmd(nodeID, cmd,timeout)
        return res

    def generate_web_driver(self, **kwargs):
        host = kwargs.get("host", "1")
        node_info = self.bedDir["nodes"][host]
        node_info["log"] = glo._global_dict["Logger"]
        self.webdriver = WebTestBase(**node_info)
        return True

    def generate_http_connector(self, **kwargs):
        host = kwargs.get("host", "1")
        node_info = self.bedDir["nodes"][host]
        node_info["log"] = glo._global_dict["Logger"]
        self.connector = HttpHyHive(**node_info)
        return True

    def wrapper_excute(self, nodeID, wrapperName, kargs):

        attr_name = "channel" + nodeID
        channel = getattr(self, attr_name, None)
        if channel:
            wrapper = getattr(channel, wrapperName, None)
            res = wrapper(**kargs)
        else:
            try:
                self.login_node(id=nodeID)
            except Exception as e:
                raise e
            else:
                wrapper = getattr(channel, wrapperName, None)
                res = wrapper(**kargs)
        return res
