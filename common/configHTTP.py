#!/usr/bin/env python
# -*- coding:utf-8 -*-
import readConfig
import requests
import json
from common import public
readConf = readConfig.ReadConfig()
class config_Http:

    def __init__(self):
        global  testUrl , realUrl

        testUrl = str(readConf.get_Url("testUrl"))
        realUrl = readConf.get_Url("realUrl")
        self.url = None
        self.params = None
        self.header = None
    def set_url(self,address):
        """
        设置URL
        :param address:
        :param kwargs:
        :return:
        """
        self.url = testUrl + address
    def set_header(self,header):
        """
        设置头部
        :param header:
        :return:
        """
        self.header = json.loads(header)
    def set_params(self,param):
        """
        设置参数
        :param param:
        :return:
        """
        self.params = param
    def post(self):
        """
        构建post请求
        :return:
        """
        try:
            response=requests.post(self.url,headers=self.header,json=self.params)
            return response
        except TimeoutError as e :
            print("时间超时:{}".format(e))
            return None
    def get(self):
        """
        构建get请求
        :return:
        """
        try:
            response=requests.get(self.url)
            return response
        except TimeoutError as e :
            print("时间超时:{}".format(e))
            return None
    def put(self):
        """
        构建get请求
        :return:
        """
        try:
            response=requests.put(self.url)
            return response
        except TimeoutError as e :
            print("时间超时:{}".format(e))
            return None
#     def return_code(self):
#         code =  str(self.post().json()["value"]).split("! ")[-1]
#         return code
# print((public.Get_xlsx("userCase.xlsx","testLogin")[0][2]))