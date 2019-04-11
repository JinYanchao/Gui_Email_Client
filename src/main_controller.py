#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Jin Yanchao
# @Time   : 4/2/19 3:37 PM
# @File   : main_controller.py
import os
import json
from smtplib import *
from module import smtp_connect, sql_connect
from view import main_window, new_email, set_database, set_server


def check_database():
    file_path = os.path.join(os.path.abspath('.'), 'database.json')
    if os.path.isfile(file_path):
        with open(file_path, 'r') as load_f:
            load_dicts = json.load(load_f)
            if len(load_dicts) == 5:
                host = load_dicts['host']
                user = load_dicts['user']
                password = load_dicts['password']
                database = load_dicts['database']
                port = load_dicts['port']
                test = sql_connect.SqlConnect(host, user, password, database, port)
                if test.test_connect():
                    return test


def check_server():
    file_path = os.path.join(os.path.abspath('.'), 'server.json')
    if os.path.isfile(file_path):
        with open(file_path, 'r') as load_f:
            load_dicts = json.load(load_f)
            if len(load_dicts) == 5:
                user = load_dicts['user']
                password = load_dicts['password']
                host = load_dicts['host']
                port = load_dicts['port']
                security = load_dicts['security']
                test = smtp_connect.SmtpConnect(user, password)
                test.set_host(host, port, security)
                try:
                    test.connect()
                    test.quit()
                    return test
                except SMTPException:
                    return


if __name__ == '__main__':
    database = check_database()
    while database is None:
        set_db = set_database.SetDatabase()
        set_db.create()
        set_db.start()
        database = check_database()
    server = check_server()
    while server is None:
        set_ser = set_server.SetServer()
        set_ser.create()
        set_ser.start()
        server = check_server()
    # root = main_window.MainWindow(database, server)
    new = new_email.NewEmail(server, database)
    new.start()
