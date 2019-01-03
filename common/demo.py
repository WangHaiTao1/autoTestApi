#!/usr/bin/env python
# -*- coding:utf-8 -*-
# import os
# from xml.etree import ElementTree as ElementTree
# import readConfig
# proDir = readConfig.proDir
# sql_path = os.path.join(proDir, "testFile", "SQL.xml")
# tree = ElementTree.parse(sql_path)
# url_list = []
# for u in tree.findall('database'):
#     print(u)
#     url_name = u.get('name')
#     print(url_name)
#     if url_name == "tester":
#         for c in u.getchildren():
#             print(c)
#             url_list.append(c.text)
# print(url_list)

import pymysql
config = {
        'host': str("localhost"),
        'user': "root",
        'passwd': "123456",
        'port': int(3306),
        'db': "tester"
    }
db = pymysql.connect("localhost","root","123456",3306,"tester")











