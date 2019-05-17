#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 09:41:45 2019

@author: usama
"""

from tkinter import *
import BackEnd

def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])

def view_command():
    list1.delete(0,END)
    for row in BackEnd.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in BackEnd.searchEntry(title_text.get(),production_text.get(),year_text.get(),imdb_text.get()):
        list1.insert(END,row)

def add_command():
    BackEnd.addEntry(title_text.get(),production_text.get(),year_text.get(),imdb_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),production_text.get(),year_text.get(),imdb_text.get()))
    
def delete_command():
    BackEnd.deleteEntry(selected_tuple[0])
    
def update_command():
    BackEnd.updateEntry(selected_tuple[0],title_text.get(),production_text.get(),year_text.get(),imdb_text.get())

win = Tk()

win.wm_title('MoviesDB')

#Labels
l1 = Label(win, text='Title')
l1.grid(row=0, column=0)
l2 = Label(win, text='Production House')
l2.grid(row=0, column=2)
l3 = Label(win, text='year')
l3.grid(row=1, column=0)
l4 = Label(win, text='IMDB Rating')
l4.grid(row=1, column=2)

#TextBoxes
title_text = StringVar()
e1 = Entry(win, textvariable=title_text)
e1.grid(row=0, column=1)

production_text = StringVar()
e2 = Entry(win, textvariable=production_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(win, textvariable=year_text)
e3.grid(row=1, column=1)

imdb_text = StringVar()
e4 = Entry(win, textvariable=imdb_text)
e4.grid(row=1, column=3)

#ListBox
list1=Listbox(win, height=12,width=60)
list1.grid(row=2,column=1,rowspan=6,columnspan=3)

#ScrollBar
sb1=Scrollbar(win)
sb1.grid(row=2,column=4,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

#Buttons
b1=Button(win,text="View all", width=12,command=view_command)
b1.grid(row=2,column=0)
b2=Button(win,text="Search entry", width=12,command=search_command)
b2.grid(row=3,column=0)
b3=Button(win,text="Add entry", width=12,command=add_command)
b3.grid(row=4,column=0)
b4=Button(win,text="Update selected", width=12,command=update_command)
b4.grid(row=5,column=0)
b5=Button(win,text="Delete selected", width=12,command=delete_command)
b5.grid(row=6,column=0)
b6=Button(win,text="Close", width=12,command=win.destroy)
b6.grid(row=7,column=0)

win.mainloop()