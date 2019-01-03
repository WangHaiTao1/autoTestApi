#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pymysql
import  readConfig
readconf = readConfig.ReadConfig()
class MyDB:
    def __init__(self):
        global host , username, password , port, database ,config
        host = readconf.get_DB("host")
        username = readconf.get_DB("username")
        password = readconf.get_DB("password")
        port = readconf.get_DB("port")
        database = readconf.get_DB("database")
        config = {
            'host': str(host),
            'user': username,
            'passwd': password,
            'port': int(port),
            'db': database
        }
        self.db = None
        self.cursor = None

    def connectDB(self):
        """
        链接数据库
        :return:
        """
        try:
            # connect to DB
            self.db = pymysql.connect(**config)
            # create cursor
            self.cursor = self.db.cursor()
            print("Connect DB successfully!")
        except ConnectionError as e:
            print("Connect DB Fail!")

    def executeSQL(self,sql):
        """
        执行SQL
        :param sql:
        :param params:
        :return:
        """
        self.connectDB()
        self.cursor.execute(sql)
        self.db.commit()

        return self.cursor

    def get_all(self,cursor):
        """
        获得所有执行结果
        :param cursor:
        :return:
        """
        value = cursor.fetchall()
        return value

    def get_one(self):
        """
        获得单行执行内容
        :param cursor:
        :return:
        """
        value = self.cursor.fatchall()
        return value

    def closeDB(self):
        """
        关闭 database
        :return:
        """
        self.connectDB()
        self.db.close()
        print("Database closed!")
db = MyDB()
print(list(db.get_all(MyDB().executeSQL("select * from student"))))
db.closeDB()