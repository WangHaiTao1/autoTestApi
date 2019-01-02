#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import configparser
proDir = os.path.split(os.path.realpath(__file__))[0]
configDir = os.path.join(proDir,"config.ini")
class ReadConfig:

    def __init__(self):

        self.cf = configparser.ConfigParser()
        self.cf.read(configDir)

    def get_Url(self,name):

        value = self.cf.get("HTTP",name)
        return value
