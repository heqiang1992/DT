#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from lib.interface.CmdWrapper import CmdWrapper
from selenium.webdriver.common.action_chains import ActionChains
import time


class WebTestBase(CmdWrapper):

    def __init__(self, **kwargs):
        super(WebTestBase, self).__init__(**kwargs)
        print("<<<<<<  open the browser. start to login web ... >>>>>>>")
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def open_url(self, url):
        self.driver.get(url)

    def send_keys(self, element, by, conment):
        """

        :param element:
        :param by:  id,xpath,name
        :param conment:
        :return:
        """
        map = {"id": By.ID, "xpath": By.XPATH, "name": By.NAME}
        self.wait_element(by=map[by], element=element)
        self.driver.find_element(by=map[by], value=element).clear()
        self.driver.find_element(by=map[by], value=element).send_keys(conment)

    def click(self, element, by):
        """
        :param element:
        :param by:  id,xpath,name
        :return:
        """
        map = {"id": By.ID, "xpath": By.XPATH, "name": By.NAME}
        self.wait_element(by=map[by], element=element)
        self.driver.find_element(by=map[by], value=element).click()

    def wait_element(self, element, by):
        """
        :param element:
        :param by:     id,xpath,name
        :return:
        """
        map = {"id": By.ID, "xpath": By.XPATH, "name": By.NAME}
        for t in range(5):
            if self.driver.find_element(by=map[by], value=element):
                break
            else:
                if t == 4:
                    print("cant find element.")
                    return False
            time.sleep(5)
        return True
    def login_infinity(self):

        self.send_keys(element="pname", by="name", conment="admin")
        self.send_keys(element="pword", by="name", conment="123456")
        self.click(element="btn_login", by="id")
        time.sleep(5)

    def click_into_cluster_management(self):
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath("//*[@id=\"navbar\"]/ul/ul/li[2]/a/b")).perform()
        time.sleep(1)

        ActionChains(self.driver).double_click(
            self.driver.find_element_by_xpath("//*[@id=\"navbar\"]/ul/ul/li[2]/ul/li[3]/a")).perform()

    def click_into_setup_guide(self):
        ActionChains(self.driver).move_to_element(
            self.driver.find_element_by_xpath("//*[@id=\"navbar\"]/ul/ul/li[2]/a/b")).perform()
        time.sleep(1)

        ActionChains(self.driver).double_click(
            self.driver.find_element_by_xpath("//*[@id=\"navbar\"]/ul/ul/li[2]/ul/li[5]/a")).perform()

    def move_to_element(self,element, by):
        """

        :param element:
        :param by:   id,xpath,name
        :return:
        """
        map = {"id": By.ID, "xpath": By.XPATH, "name": By.NAME}

        ActionChains(self.driver).move_to_element(
            self.driver.find_element(by=map[by], value=element)).perform()

    def ActionChains_double_click(self,element, by):
        """

                :param element:
                :param by:   id,xpath,name
                :return:
                """

        map = {"id": By.ID, "xpath": By.XPATH, "name": By.NAME}
        ActionChains(self.driver).move_to_element(
            self.driver.find_element(by=map[by], value=element)).perform()
        time.sleep(1)
        ActionChains(self.driver).double_click(
            self.driver.find_element(by=map[by], value=element)).perform()

    def run_js(self,js):


        self.driver.execute_script(js)



    # def __del__(self):
    #     self.driver.close()
