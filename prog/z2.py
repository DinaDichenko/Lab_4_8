#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
напишите программу по следующему описанию. Нажатие Enter в однострочном текстовом поле приводит к перемещению текста из него в список (экземпляр Listbox ). 
При двойном клике ( <Double-Button-1> ) по элементу-строке списка, она должна копироваться в текстовое поле.
"""
from tkinter import *


def enter(event):
    box.insert(END, ent.get())
    ent.delete(0, END)


def click(event):
    selected_element = box.get(box.curselection())
    ent.delete(0, END)
    ent.insert(END, selected_element)


if __name__=='__main__':
    root = Tk()

    ent = Entry(width=30)
    ent.pack()
    ent.bind("<Return>", enter)

    box = Listbox(width=30)
    box.pack()
    box.bind("<Double-1>", click)

    root.mainloop()
