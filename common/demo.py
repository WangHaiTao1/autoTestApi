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

# import pymysql
# config = {
#         'host': str("127.0.0.1"),
#         'user': "root",
#         'passwd': "123456",
#         'port': int(3306),
#         'db': "tester"
#     }
# #连接mysql
# db = pymysql.connect(**config)
# #建立游标
# cursor = db.cursor()
# #执行SQL
# cursor.execute("select * from student")
# #获取sql全部执行内容
# sqldata = cursor.fetchall()
# #获取sql执行内容的一部分
# # print(cursor.fetchone())
# #关闭数据库
# db.close()
# for i in sqldata:
#     print(list(i))
import json
import readConfig
from common import public
import requests


url = "https://m-test.ibubuji.com/api/v1/cfuser/login/mobile"
headers = public.Get_xlsx("userCase.xlsx","testLogin")[0][2]
params = json.loads(public.Get_xlsx("userCase.xlsx","testLogin")[0][3])
params.update({"code":"6219"})

print(type(json.loads(headers)))
print(params)
print(type({"Content-Type":"application/json"}))
data = {"Content-Type":"application/json"}
re = requests.post(url,json=params,headers=json.loads(headers))
print(re.json())




