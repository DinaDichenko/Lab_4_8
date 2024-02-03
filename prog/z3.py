#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
напишите программу по описанию. Размеры многострочного текстового поля определяются значениями, введенными в однострочные текстовые поля. 
Изменение размера происходит при нажатии мышью на кнопку, а также при нажатии клавиши Enter. Цвет фона экземпляра Text светлосерый ( lightgrey ), 
когда поле не в фокусе, и белый, когда имеет фокус. Событие получения фокуса обозначается как <FocusIn> , потери – как <FocusOut> . Для справки: 
фокус перемещается по виджетам при нажатии Tab, Ctrl+Tab, Shift+Tab, а также при клике по ним мышью (к кнопкам последнее не относится).
"""
from tkinter import *


def size():
    try:
        width = int(ent1.get())
        height = int(ent2.get())
        text.config(width=width, height=height)
    except ValueError:
        pass


def on_focus_in(event):
    text.config(bg="white")


def on_focus_out(event):
    text.config(bg="lightgrey")


if __name__=='__main__':
    root = Tk()

    ent1 = Entry()
    ent1.pack()
    ent1.bind("<Return>", lambda event=None: size())

    ent2 = Entry()
    ent2.pack()
    ent2.bind("<Return>", lambda event=None: size())

    text = Text()
    text.pack()
    text.bind("<FocusIn>", on_focus_in)
    text.bind("<FocusOut>", on_focus_out)

    update_button = Button(text="Update Size", command=size)
    update_button.pack()

    root.mainloop()
