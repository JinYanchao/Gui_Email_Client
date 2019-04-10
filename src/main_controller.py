#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Jin Yanchao
# @Time   : 4/2/19 3:37 PM
# @File   : main_controller.py
from module import smtp_connect, sql_connect
from view import new_email


if __name__ == '__main__':
    new_server = smtp_connect.SmtpConnect('', '')
    new_sql = sql_connect.SqlConnect('localhost', 'root', 'a3206390', 'email_database', 3306)
    new_mail = new_email.NewEmail(new_server, new_sql)
