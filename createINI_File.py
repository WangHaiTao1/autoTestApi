#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import configparser
proDir = os.path.join(os.path.abspath("."),"config.ini")
config = configparser.ConfigParser()
config.read(proDir)

if not config.has_section("HTTP"):
    config.add_section("HTTP")
    config.set("HTTP","testUrl","https://m-test.ibubuji.com")
    config.set("HTTP","realUrl","https://m.ibubuji.com")
else:
    print("标题已存在")

with open(proDir,"w") as configFile:
    config.write(configFile)

configFile.close()