#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Jin Yanchao
# @Time   : 4/2/19 8:23 AM
# @File   : window.py
from tkinter import *


class Window(object):

    def __init__(self, window_name, window_width, window_height):
        self.__window = Tk()
        self.__window.title(window_name)
        screen_width = self.__window.winfo_screenwidth()
        screen_height = self.__window.winfo_screenheight()
        self.__window.geometry('%dx%d+%d+%d' %(window_width, window_height,
                                               (screen_width - window_width) / 2,
                                               (screen_height - window_height) / 2))
        self.__menubar = Menu(self.__window)
        self.__root_layout = Frame(self.__window)

    def get_window(self):
        return self.__window

    def get_menubar(self):
        return self.__menubar

    def get_root_layout(self):
        return self.__root_layout

    def set_menu(self, father_menu, index, menu_name, menu_dict):
        child_menu = Menu(father_menu, tearoff=False)
        for menu_list in menu_dict:
            if menu_list == '|':
                child_menu.add_separator()
            else:
                child_menu.add_command(label=menu_list[0], command=menu_list[1])
        father_menu.insert_cascade(index, label=menu_name, menu=child_menu)

    def start(self):
        self.__window.config(menu=self.__menubar)
        self.__root_layout.pack()
        self.__window.mainloop()
