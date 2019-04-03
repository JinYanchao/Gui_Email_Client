#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Jin Yanchao
# @Time   : 4/2/19 3:37 PM
# @File   : main_controller.py
from module import smtp_connect, pop_connect
from view import new_email


if __name__ == '__main__':
    new_server = smtp_connect.SmtpConnect('@163.com', '')
    new_mail = new_email.NewEmail(new_server)
