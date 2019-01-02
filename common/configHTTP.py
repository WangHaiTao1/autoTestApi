#!/usr/bin/env python
# -*- coding:utf-8 -*-
import readConfig
import requests
readConf = readConfig.ReadConfig()
class config_Http:

    def __init__(self):
        global  testUrl , realUrl

        testUrl = str(readConf.get_Url("testUrl"))
        realUrl = readConf.get_Url("realUrl")
        self.url = None
    def set_url(self,address):
        """
        设置URL
        :param address:
        :param kwargs:
        :return:
        """
        self.url = testUrl + address

    def post(self):
        """
        构建post请求
        :return:
        """
        try:
            response=requests.post(self.url)
            return response
        except TimeoutError as e :
            print("时间超时:{}".format(e))
            return None