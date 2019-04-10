#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Jin Yanchao
# @Time   : 4/9/19 10:49 PM
# @File   : check_email.py
from tkinter import *
from tkinter import messagebox
from view import window

class CheckEmail(object):

    def __init__(self, sql):
        self.__window = window.Window('Check Email', 800, 600)
        self.__root_layout = self.__window.get_root_layout()
        self.__sql = sql
        self.__create()
        self.__start()

    def __create(self):
        self.__create_header()
        self.__create_table()

    def __create_header(self):
        frm_header = Frame(self.__root_layout)
        Label(frm_header, width=5).grid(row=0, column=0, sticky=E)
        Label(frm_header, text="题目", width=10).grid(row=0, column=1, sticky=W)
        e1 = Entry(frm_header, textvariable=v1, width=30)
        e1.grid(row=0, column=2, padx=1, pady=1)
        e2 = Button(frm_header, text='查询', command=lambda: self.__search(tv, e1), width=10)
        e2.grid(row=0, column=3, padx=1, pady=1)
        e3 = Button(frm_header, text='删除', command=lambda: self.__delrow(tv), width=10)
        e3.grid(row=0, column=4, padx=1, pady=1)
        Label(frm_header, width=5).grid(row=0, column=5, sticky=E)
        frm_header.pack()

    def __create_table(self):
        pass



    def __start(self):
        self.__window.get_window().resizable(0, 0)
        self.__window.start()
