#!/usr/bin/env python
# -*- coding:utf-8 -*-
import readConfig
import os
import unittest
import HTMLTestRunner
from common import public
proDir = readConfig.proDir

class allTest:

    def __init__(self):
        self.caselistDir = os.path.join(proDir, "caselist.txt")
        self.caseFileDir = os.path.join(proDir, "testCase", "user")
        self.reportDir = public.get_reportPath()

    def set_case_list(self):
        caseList = []
        fb = open(self.caselistDir)
        for value in fb.readlines():
            data = str(value)
            if data != "" and not data.startswith("#"):
                caseList.append(data.replace("\n", ""))
        fb.close()
        return caseList

    def set_case_suite(self):
        caselist = self.set_case_list()
        test_suite = unittest.TestSuite()
        suite_module = []

        for case in caselist:
            case_name = case.split("/")[-1]
            discover = unittest.defaultTestLoader.discover(
                self.caseFileDir, pattern=case_name + ".py",
                top_level_dir=None
            )
            suite_module.append(discover)
        if len(suite_module) > 0:

            for suite in suite_module:
                for test_name in suite:
                    test_suite.addTest(test_name)
        else:
            return None
        return test_suite

    def run(self):
        try:
            suite = self.set_case_suite()
            if suite is not None:
                fb = open(self.reportDir, "wb")
                runner = HTMLTestRunner.HTMLTestRunner(
                    stream=fb, title="Test Report",
                    description="测试描述"
                )

                runner.run(suite)
                fb.close()
            else:
                print("失败")
        except Exception as e:
            print(e)

allTest().run()