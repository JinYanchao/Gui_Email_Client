#!/usr/bin/env python
# -*- coding: utf-8 -*  -
# @Author : Jin Yanchao
# @Time   : 4/3/19 5:43 PM
# @File   : sql_connect.py
from pymysql import *


class SqlConnect(object):

    def __init__(self, host, user, password, db_name, port):
        self.__host = host
        self.__user = user
        self.__password = password
        self.__db_name = db_name
        self.__port = port

    def __connect(self):
        try:
            database = connect(self.__host, self.__user, self.__password, self.__db_name, self.__port)
            return database
        except DatabaseError:
            return

    def test_connect(self):
        try:
            database = connect(self.__host, self.__user, self.__password, self.__db_name, self.__port)
            database.close()
            return True
        except DatabaseError:
            return False

    def ins_data(self, dbsql, values):
        database = self.__connect()
        cursor = database.cursor()
        try:
            cursor.execute(dbsql, values)
            database.commit()
        except DatabaseError:
            database.rollback()
        database.close()

    def sel_data(self, dbsql):
        database = self.__connect()
        cursor = database.cursor()
        try:
            cursor.execute(dbsql)
            results = cursor.fetchall()
            database.close()
            return results
        except DatabaseError:
            database.rollback()
        database.close()

    def refresh(self, dbsql):
        database = self.__connect()
        cursor = database.cursor()
        try:
            cursor.execute(dbsql)
            database.commit()
        except DatabaseError:
            database.rollback()
        database.close()

    def create_table(self):
        database = self.__connect()
        cursor = database.cursor()
        for item in ['draft', 'outbox']:
            dbsql = 'create table is not exists %s' % item + '(`id`  int NOT NULL AUTO_INCREMENT ,' \
                                                             '`sender`  varchar(50) NULL ,' \
                                                             '`receiver`  varchar(50) NULL ,' \
                                                             '`subject`  varchar(20) NULL ,' \
                                                             '`context`  varchar(1000) NULL ,' \
                                                             '`p_date`  varchar(20) NULL ,' \
                                                             'PRIMARY KEY (`id`))'
            try:
                cursor.execute(dbsql)
                database.commit()
            except DatabaseError:
                database.rollback()
        database.close()
