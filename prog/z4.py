#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Создайте на холсте подобное изображение
"""
from tkinter import *

root = Tk()
c = Canvas(root, width=200, height=200, bg="white")
c.pack()

c.create_polygon(100, 10, 20, 90, 180, 90, fill="lightblue")
c.create_rectangle(150, 190, 50, 70, fill="lightblue", outline="lightblue")
c.create_oval(160, 10, 200, 50, fill="orange", outline="orange")
num_arcs = 20

for i in range(num_arcs):
    start_x = i * 10
    end_x = start_x + 20
    c.create_arc(
        start_x,
        500,
        end_x,
        170,
        start=130,
        extent=-60,
        style=ARC,
        outline="green",
        width=2,
    )

root.mainloop()
