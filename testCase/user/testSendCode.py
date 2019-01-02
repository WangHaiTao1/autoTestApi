#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
import paramunittest
import readConfig
from common import configHTTP ,public
import time
caseList = public.Get_xlsx("userCase.xlsx","testSendCode")

readConf = readConfig.ReadConfig()
configHttp = configHTTP.config_Http()

@paramunittest.parametrized(*caseList)
class SendCode(unittest.TestCase):

    def setParameters(self,caseNo,case_name,mobile,address,mothod,realmsg,testmsg):
        """
        设置参数
        :param caseNo:
        :param case_name:
        :param mobile:
        :param address:
        :param mothod:
        :param realmsg:
        :param testmsg:
        :return:
        """
        self.caseNo = str(caseNo)
        self.case_name = str(case_name)
        self.mobile = str(mobile).split(".")[0]
        self.address = str(address)
        self.mothod = str(mothod)
        self.realmsg = str(realmsg)
        self.testmsg = str(testmsg).split(".")[0]
    def description(self):
        """
        测试描述
        :return:
        """
        return self.case_name
    def setUp(self):
        """
        测试开始
        :return:
        """
        print(self.case_name + "测试开始前准备")

    def test_sendCode(self):
        """
        测试用例
        :return:
        """
        #设置URL
        self.url = self.address +self.mobile
        configHttp.set_url(self.url)
        print("第一步：设置url"+configHttp.url)

        #set headers
        print("第二步: 设置header(token等)")

        #set params

        print("第三步：设置发送请求的参数")
        #发送post请求
        self.return_json = configHttp.post()
        method = str(self.return_json.request)[
                 int(str(self.return_json.request).find('['))
                 + 1:
                 int(str(self.return_json.request).find(']'))]
        print("第四步：发送请求\n\t\t请求方法："+method)
        print(self.testmsg)
        print(self.return_json.json())
        #检查结果

        self.checkResult()
        print("第五步:检查结果")


    def checkResult(self):
        self.info = self.return_json.json()

        if self.caseNo.split("_")[-1] == "1":
            self.assertIn(self.testmsg,self.info["value"])

        if self.caseNo.split("_")[-1] == "2":
            self.assertIn(self.testmsg, self.info["errorMessage"])

        if self.caseNo.split("_")[-1] == "3":
            self.assertIn(self.testmsg, self.info["errorDescription"])

    def tearDown(self):

        time.sleep(3)


