#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Jin Yanchao
# @Time   : 4/10/19 5:20 PM
# @File   : main_window.py
from tkinter import *
from view import window


class MainWindow(object):

    def __init__(self, server, database):
        self.__window = window.Window('Main Window', 400, 300)
        self.__root_layout = self.__window.get_root_layout()
        self.__server = server
        self.__database = database

    def create(self):
        pass
