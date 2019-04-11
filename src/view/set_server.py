#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Jin Yanchao
# @Time   : 4/10/19 9:30 PM
# @File   : set_server.py
import os
import json
from tkinter import *
from tkinter import messagebox
from smtplib import *
from view import window
from module import smtp_connect


class SetServer(object):

    def __init__(self):
        self.__window = window.Window('Set Server', 400, 220)
        self.__root_layout = self.__window.get_root_layout()

    def create(self):
        Label(self.__root_layout).grid(row=0, columnspan=4)
        Label(self.__root_layout, text='User', width=9, font=('Arial', 12)).grid(row=1, column=0, sticky=E, pady=1)
        Label(self.__root_layout, text='Password', width=9, font=('Arial', 12)).grid(row=2, column=0, sticky=E, pady=1)
        Label(self.__root_layout, text='Host', width=9, font=('Arial', 12)).grid(row=3, column=0, sticky=E, pady=1)
        Label(self.__root_layout, text='Port', width=9, font=('Arial', 12)).grid(row=4, column=0, sticky=E, pady=1)
        Label(self.__root_layout, text='Security', width=9, font=('Arial', 12)).grid(row=5, column=0, sticky=E, pady=1)
        var_user = StringVar()
        var_password = StringVar()
        var_host = StringVar()
        var_port = StringVar()
        var_security = StringVar()
        Entry(self.__root_layout, textvariable=var_user, width=27, font=('Verdana', 12))\
            .grid(row=1, column=1, columnspan=4, sticky=W, pady=1)
        entry_passwd = Entry(self.__root_layout, textvariable=var_password, width=27, font=('Verdana', 12))
        entry_passwd.grid(row=2, column=1, columnspan=4, sticky=W, pady=1)
        entry_passwd['show'] = '*'
        Entry(self.__root_layout, textvariable=var_host, width=27, font=('Verdana', 12))\
            .grid(row=3, column=1, columnspan=4, sticky=W, pady=1)
        Entry(self.__root_layout, textvariable=var_port, width=27, font=('Verdana', 12))\
            .grid(row=4, column=1, columnspan=4, sticky=W, pady=1)
        Entry(self.__root_layout, textvariable=var_security, width=27, font=('Verdana', 12))\
            .grid(row=5, column=1, columnspan=4, sticky=W, pady=1)
        Button(self.__root_layout, text='Confirm', width=8, height=1, font=('Arial', 12),
               command=lambda: self.__confirm(var_user.get(), var_password.get(), var_host.get(),
                                              var_port.get(), var_security.get())).grid(row=6, column=1, pady=1)
        Button(self.__root_layout, text='Cancel', width=8, height=1, font=('Arial', 12),
               command=self.__window.get_window().destroy).grid(row=6, column=2, pady=1)

    def __confirm(self, user, password, host, port, security):
        server = smtp_connect.SmtpConnect(user, password)
        server.set_host(host, port, security)
        try:
            server.connect()
            server.quit()
            file_path = os.path.join(os.path.abspath('.'), 'server.json')
            with open(file_path, 'w') as file:
                config = {'user': user, 'password': password, 'host': host, 'port': port, 'security': security}
                json_str = json.dumps(config)
                config_dicts = json.loads(json_str)
                json.dump(config_dicts, file)
                self.__window.get_window().destroy()
        except SMTPException:
            messagebox.showwarning('Waring', 'Fail to connect server')

    def start(self):
        self.__window.get_window().resizable(0, 0)
        self.__window.start()
