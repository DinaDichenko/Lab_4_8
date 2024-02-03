#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
в данной программе создается анимация круга, который движется от левой границы холста до правой.
Выражение c.coords(ball) возвращает список текущих координат объекта (в данном случае это ball). Третий элемент списка соответствует его второй координате x. 
Метод after вызывает функцию, переданную вторым аргументом, через количество миллисекунд, указанных первым аргументом. Изучите приведенную программу и самостоятельно 
запрограммируйте постепенное движение фигуры в ту точку холста, где пользователь кликает левой кнопкой мыши. 
Координаты события хранятся в его атрибутах x и y ( event.x , event.y ).
"""
from tkinter import *


def motion():
    current_coords = c.coords(ball)
    target_x, target_y = target_coords

    distance_x = target_x - current_coords[0]
    distance_y = target_y - current_coords[1]

    step_x = 1 if distance_x > 0 else -1
    step_y = 1 if distance_y > 0 else -1

    c.move(ball, step_x, step_y)

    if c.coords(ball)[0] != target_x or c.coords(ball)[1] != target_y:
        root.after(10, motion)


def on_click(event):
    global target_coords
    target_coords = (event.x, event.y)
    motion()


if __name__=='__main__':
    root = Tk()

    c = Canvas(root, width=300, height=200, bg="white")
    c.pack()

    ball = c.create_oval(0, 100, 40, 140, fill="green")
    c.bind("<Button-1>", on_click)

    root.mainloop()
