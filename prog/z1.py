#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
напишите программу, состоящую из двух списков Listbox . В первом будет, например, перечень товаров, заданный программно. 
Второй изначально пуст, пусть это будет перечень покупок. При клике на одну кнопку товар должен переходить из одного списка в другой. 
При клике на вторую кнопку – возвращаться (человек передумал покупать). Предусмотрите возможность множественного выбора элементов списка и их перемещения.
"""
from tkinter import *


def add_box(name):
    for i in (
        "apple",
        "banabas",
        "carrot",
        "bread",
        "butter",
        "meat",
        "potapo",
        "milk",
        "tomato",
        "pineapple",
    ):
        name.insert(0, i)


def box_to_box2():
    selected_indices = box.curselection()
    for i in selected_indices:
        selected_element = box.get(i)
        box2.insert(END, selected_element)

    for i in reversed(selected_indices):
        box.delete(i)


def box2_to_box():
    selected_indices = box2.curselection()
    for i in selected_indices:
        selected_element = box2.get(i)
        box.insert(END, selected_element)

    for i in reversed(selected_indices):
        box2.delete(i)


if __name__=='__main__':
    root = Tk()

    box = Listbox(selectmode=MULTIPLE)
    box.pack(side=LEFT)
    add_box(box)


    f = Frame()
    f.pack(side=LEFT, padx=10)
    Button(f, text=">>>", command=box_to_box2).pack(fill=X)
    Button(f, text="<<<", command=box2_to_box).pack(fill=X)

    box2 = Listbox(selectmode=MULTIPLE)
    box2.pack(side=LEFT)

    root.mainloop()
