#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Jin Yanchao
# @Time   : 4/2/19 8:28 AM
# @File   : new_email.py
from tkinter import *
from tkinter import messagebox
from view import window


class NewEmail(object):

    def __init__(self, server):
        self.__window = window.Window('New Email', '500x450')
        self.__menubar = self.__window.get_menubar()
        self.__root_layout = self.__window.get_root_layout()
        self.__server = server
        self.__sender = server.get_user()
        self.__receiver = StringVar()
        self.__subject = StringVar()
        self.__context = StringVar()
        self.__create()
        self.__start()

    def __create(self):
        # self.__window.set_menu(self.__menubar, 0, 'File', {})
        self.__create_button()
        self.__create_header()
        self.__create_context()

    def __create_button(self):
        frm_button = Frame(self.__root_layout)
        Button(frm_button, text='Send', width=6, height=1, font=('Arial', 10),
               command=lambda : self.__send_email(self.__server)).pack(side=LEFT)
        Button(frm_button, text='Reset', width=6, height=1, font=('Arial', 10)).pack(side=RIGHT)
        frm_button.pack(side=TOP)

    def __create_header(self):
        frm_header = Frame(self.__root_layout)
        frm_h_left = Frame(frm_header)
        Label(frm_h_left, text='   From:', font=('Arial', 12)).pack(side=TOP)
        Label(frm_h_left, text='     To:', font=('Arial', 12)).pack(side=TOP)
        Label(frm_h_left, text='Subject:', font=('Arial', 12)).pack(side=TOP)
        frm_h_left.pack(side=LEFT)
        frm_h_right = Frame(frm_header)
        Label(frm_h_right, text=self.__sender, width=30, font=('Verdana', 12)).pack()
        Entry(frm_h_right, textvariable=self.__receiver, width=30, font=('Verdana', 12)).pack()
        Entry(frm_h_right, textvariable=self.__subject, width=30, font=('Verdana', 12)).pack()
        frm_h_right.pack(side=RIGHT)
        frm_header.pack(side=TOP)

    def __create_context(self):
        frm_context = Frame(self.__root_layout)
        Label(frm_context, text='Context').pack()
        self.__context = Text(frm_context, width=34, height=6, font=('Verdana', 15))
        self.__context.pack()
        frm_context.pack()

    def __send_email(self, server):
        rec_text = self.__receiver.get()
        if rec_text == '':
            messagebox.showinfo('Error', 'Receiver could not be empty!')
            return
        ti_text = self.__subject.get()
        con_text = self.__context.get(1.0, END)
        if server.send_email(rec_text, con_text, ti_text):
            messagebox.showinfo('Tips', 'Sent email successfully')
        else:
            messagebox.showinfo('Warning', 'Failed to send email')

    def __start(self):
        self.__window.start()
