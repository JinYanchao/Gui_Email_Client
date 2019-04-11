#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Jin Yanchao
# @Time   : 4/9/19 10:49 PM
# @File   : check_email.py
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from view import window, new_email


class CheckEmail(object):

    def __init__(self, server, database, table):
        self.__window = window.Window('Check Email', 800, 450)
        self.__root_layout = self.__window.get_root_layout()
        self.__server = server
        self.__database = database
        self.__table = table
        self.__var_search = StringVar()
        columns = ('ID', 'Sender', 'Receiver', 'Subject', 'Context', 'Date')
        self.__tree_view = ttk.Treeview(self.__root_layout, height=20, show='headings', columns=columns)
        self.__tree_view.bind('<Double-1>', self.__treeview_click)

    def create(self):
        self.__create_header()
        self.__create_table()

    def __create_header(self):
        Label(self.__root_layout, width=5).grid(row=0, column=0, sticky=E)
        Label(self.__root_layout, text='Subject', font=('Arial', 12), width=10).grid(row=0, column=1, sticky=W)
        var_entry = Entry(self.__root_layout, textvariable=self.__var_search, width=30)
        var_entry.grid(row=0, column=2, padx=1, pady=1)
        Button(self.__root_layout, text='Search', font=('Arial', 12),
               command=lambda: self.__search(var_entry), width=10).grid(row=0, column=3, padx=1, pady=1)
        Button(self.__root_layout, text='Delete', font=('Arial', 12),
               command=self.__del_row, width=10).grid(row=0, column=4, padx=1, pady=1)
        Label(self.__root_layout, width=5).grid(row=0, column=5, sticky=E)

    def __create_table(self):
        self.__tree_view.column('ID', width=100, anchor='center')
        self.__tree_view.column('Sender', width=100, anchor='center')
        self.__tree_view.column('Receiver', width=100, anchor='center')
        self.__tree_view.column('Subject', width=100, anchor='center')
        self.__tree_view.column('Context', width=200, anchor='center')
        self.__tree_view.column('Date', width=200, anchor='center')
        self.__tree_view.heading('ID', text='ID')
        self.__tree_view.heading('Sender', text='Sender')
        self.__tree_view.heading('Receiver', text='Receiver')
        self.__tree_view.heading('Subject', text='Subject')
        self.__tree_view.heading('Context', text='Context')
        self.__tree_view.heading('Date', text='Date')
        self.__tree_view.grid(row=1, columnspan=6, padx=1, pady=1)
        dbsql = 'select id, sender, receiver, subject, context, p_date from %s' % self.__table
        results = self.__database.sel_data(dbsql)
        self.__insert_to_tree(results)

    def __treeview_click(self, event):
        for item in self.__tree_view.selection():
            item_text = self.__tree_view.item(item, 'values')
            self.__window.get_window().destroy()
            global new_draft
            new_draft = new_email.NewEmail(self.__server, self.__database, item_text)
            new_draft.start()

    def __insert_to_tree(self, results):
        k = 0
        for row in results:
            self.__tree_view.insert('', k, values=(row[0],row[1],row[2],row[3],row[4],row[5]))
            k += 1

    def __del_tree(self):
        items = self.__tree_view.get_children()
        for item in items:
            self.__tree_view.delete(item)

    def __search(self, var_entry):
        self.__del_tree()
        dbsql = 'select id, sender, receiver, subject, context, p_date from %s '\
                % self.__table + 'where subject like "%s"' % var_entry.get()
        results = self.__database.sel_data(dbsql)
        if len(results) == 0:
            messagebox.showwarning('Waring', 'There is not a email with subject ' + var_entry.get())
            dbsql = 'select id, sender, receiver, subject, context, p_date from %s' % self.__table
            results = self.__database.sel_data(dbsql)
        self.__insert_to_tree(results)

    def __del_row(self):
        if messagebox.askokcancel('Notice', 'Are you sure to delete this data?'):
            item = self.__tree_view.selection()
            item_text = self.__tree_view.item(item, 'values')
            dbsql = 'delete from %s' % self.__table + ' where id=%s' % item_text[0]
            self.__database.refresh(dbsql)
            self.__del_tree()
            dbsql = 'select id, sender, receiver, subject, context, p_date from %s' % self.__table
            results = self.__database.sel_data(dbsql)
            self.__insert_to_tree(results)

    def start(self):
        self.__window.get_window().resizable(0, 0)
        self.__window.start()
