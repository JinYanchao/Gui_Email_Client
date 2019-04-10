#!/usr/bin/env python
# -*- coding: utf-8 -*  -
# @Author : Jin Yanchao
# @Time   : 4/3/19 5:43 PM
# @File   : sql_connect.py
from pymysql import *


class SqlConnect(object):

    def __init__(self, host, user, password, db_name, port):
        self.__database = connect(host, user, password, db_name, port)
        self.__cursor = self.__database.cursor()

    def exec(self, sql, values):
        self.__cursor.execute(sql, values)
        self.__database.commit()


    def __del__(self):
        self.__database.close()
