#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Jin Yanchao
# @Time   : 4/2/19 9:04 AM
# @File   : smtp_connect.py
from smtplib import *
from email.mime.text import MIMEText


class SmtpConnect:

    def __init__(self, mail_user, mail_pwd):
        self.__user = mail_user
        self.__pwd = mail_pwd
        self.__host = None
        self.__port = None
        self.__security = None
        self.__server = None

    def get_user(self):
        return self.__user

    def default_host(self):
        host = self.__user.split('@')[1]
        smtp_dicts = {'qq.com': [465, 'SSL'],
                      '163.com': [465, 'SSL'],
                      'gmail.com': [587, 'STARTTLS'],
                      'outlook.com': [587, 'STARTTLS']}
        if host in smtp_dicts.keys():
            self.__host = 'smtp.' + host
            self.__port = smtp_dicts[host][0]
            self.__security = smtp_dicts[host][1]
            return [self.__host, self.__port, self.__security]

    def set_host(self, host, port, security):
        self.__host = host
        self.__port = port
        self.__security = security

    def connect(self):
        if self.__security == 'SSL':
            self.__server = SMTP_SSL(self.__host, self.__port)
        elif self.__security == 'STARTTLS':
            self.__server = SMTP(self.__host, self.__port)
            self.__server.ehlo()
            self.__server.starttls()
        else:
            self.__server = SMTP(self.__host, self.__port)
        self.__server.login(self.__user, self.__pwd)

    def quit(self):
        self.__server.quit()

    def send_email(self, to_addr, context, subject):
        msg = MIMEText(context, 'plain', 'utf-8')
        msg['From'] = '{}'.format(self.__user)
        msg['To'] = to_addr
        msg['Subject'] = subject
        try:
            self.connect()
            self.__server.sendmail(self.__user, to_addr, msg.as_string())
            self.__server.quit()
        except SMTPException:
            self.__server.quit()
            return False
        return True
