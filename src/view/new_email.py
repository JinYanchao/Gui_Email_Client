#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Jin Yanchao
# @Time   : 4/2/19 8:28 AM
# @File   : new_email.py
from tkinter import *
from tkinter import messagebox
import datetime
from view import window, check_email


class NewEmail(object):

    def __init__(self, server, database, item_text=None):
        self.__window = window.Window('New Email', 500, 450)
        self.__root_layout = self.__window.get_root_layout()
        self.__database = database
        self.__server = server
        self.__receiver = StringVar()
        self.__subject = StringVar()
        self.__context = Text()
        if item_text is not None:
            self.__sender = item_text[1]
            self.__receiver.set(item_text[2])
            self.__subject.set(item_text[3])
            self.__create(item_text[4])
        else:
            self.__sender = server.get_user()
            self.__create()

    def __create(self, text=None):
        self.__create_button()
        self.__create_header()
        if text is not None:
            self.__create_context(text)
        else:
            self.__create_context()

    def __create_button(self):
        frm_button = Frame(self.__root_layout)
        frm_button_lift = Frame(frm_button)
        Button(frm_button_lift, text='Send', width=8, height=1, font=('Arial', 12),
               command=self.__save).pack(side=LEFT, padx=5, pady=1)
        Button(frm_button_lift, text='Reset', width=8, height=1, font=('Arial', 12),
               command=self.__reset).pack(side=RIGHT, padx=5, pady=1)
        frm_button_lift.pack(side=LEFT, padx=10)
        frm_button_right = Frame(frm_button)
        Button(frm_button_right, text='Save', width=8, height=1, font=('Arial', 12),
               command=self.__save).pack(side=LEFT, padx=5, pady=1)
        Button(frm_button_right, text='Check', width=8, height=1, font=('Arial', 12),
               command=self.__check).pack(side=RIGHT, padx=5, pady=1)
        frm_button_right.pack(side=RIGHT, padx=10)
        frm_button.pack(side=TOP)

    def __create_header(self):
        frm_header = Frame(self.__root_layout)
        Label(frm_header, text='From : ', font=('Arial', 12)).grid(row=0, column=0, sticky=E)
        Label(frm_header, text='To : ', font=('Arial', 12)).grid(row=1, column=0, sticky=E)
        Label(frm_header, text='Subject : ', font=('Arial', 12)).grid(row=2, column=0, sticky=W)
        Label(frm_header, text=self.__sender, width=35, font=('Verdana', 12)).grid(row=0, column=1)
        Entry(frm_header, textvariable=self.__receiver, width=35, font=('Verdana', 12)).grid(row=1, column=1)
        Entry(frm_header, textvariable=self.__subject, width=35, font=('Verdana', 12)).grid(row=2, column=1)
        frm_header.pack(side=TOP)

    def __create_context(self, text=None):
        frm_context = Frame(self.__root_layout)
        Label(frm_context, text='Context', font=('Arial', 12)).pack()
        self.__context = Text(frm_context, width=35, height=12, font=('Verdana', 14))
        if text is not None:
            self.__context.insert(0.0, text)
        self.__context.pack()
        frm_context.pack()

    def __send(self):
        rec_text = self.__receiver.get()
        if rec_text == '':
            messagebox.showerror('Error', 'Receiver could\'t be empty')
            return
        ti_text = self.__subject.get()
        con_text = self.__context.get(0.0, END)
        if self.__server.send_email(rec_text, con_text, ti_text):
            messagebox.showinfo('Info', 'Send email successfully')
        else:
            messagebox.showwarning('Warning', 'Fail to send email')

    def __reset(self):
        if messagebox.askokcancel('Notice', 'Are you sure to reset all text?'):
            self.__receiver.set('')
            self.__subject.set('')
            self.__context.delete(0.0, END)

    def __save(self):
        dbsql = 'insert into draft(sender, receiver, subject, context, p_date)values(%s, %s, %s, %s, %s)'
        values = (self.__sender, self.__receiver.get(), self.__subject.get(),
                  self.__context.get(0.0, END), datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        self.__database.ins_data(dbsql, values)

    def __check(self):
        self.__window.get_window().destroy()
        global check_window
        check_window = check_email.CheckEmail(self.__server, self.__database, 'draft')
        check_window.create()
        check_window.start()

    def start(self):
        self.__window.get_window().resizable(0, 0)
        self.__window.start()
