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
        self.__window = window.Window('New Email', 500, 450)
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
        Button(frm_button, text='Send', width=8, height=1, font=('Arial', 12),
               command=lambda : self.__send(self.__server)).pack(side=LEFT, padx=40)
        Button(frm_button, text='Reset', width=8, height=1, font=('Arial', 12),
               command=self.__reset).pack(side=RIGHT, padx=40)
        frm_button.pack(side=TOP)

    def __create_header(self):
        frm_header = Frame(self.__root_layout)
        frm_h_left = Frame(frm_header)
        Label(frm_h_left, text='From : ', font=('Arial', 12)).grid(row=0, sticky=E)
        Label(frm_h_left, text='To : ', font=('Arial', 12)).grid(row=1, sticky=E)
        Label(frm_h_left, text='Subject : ', font=('Arial', 12)).grid(row=2, sticky=W)
        frm_h_left.pack(side=LEFT)
        frm_h_right = Frame(frm_header)
        Label(frm_h_right, text=self.__sender, width=35, font=('Verdana', 12)).grid(row=0)
        Entry(frm_h_right, textvariable=self.__receiver, width=35, font=('Verdana', 12)).grid(row=1)
        Entry(frm_h_right, textvariable=self.__subject, width=35, font=('Verdana', 12)).grid(row=2)
        frm_h_right.pack(side=RIGHT)
        frm_header.pack(side=TOP)

    def __create_context(self):
        frm_context = Frame(self.__root_layout)
        Label(frm_context, text='Context', font=('Arial', 12)).pack()
        self.__context = Text(frm_context, width=35, height=12, font=('Verdana', 14))
        self.__context.pack()
        frm_context.pack()

    def __send(self, server):
        rec_text = self.__receiver.get()
        if rec_text == '':
            messagebox.showerror('Error', 'Receiver could\'t be empty')
            return
        ti_text = self.__subject.get()
        con_text = self.__context.get(1.0, END)
        if server.send_email(rec_text, con_text, ti_text):
            messagebox.showinfo('Tips', 'Sent email successfully')
        else:
            messagebox.showwarning('Warning', 'Failed to send email')

    def __reset(self):
        self.__receiver.set('')
        self.__subject.set('')
        self.__context.delete(1.0, END)

    def __start(self):
        self.__window.get_window().resizable(0, 0)
        self.__window.start()
