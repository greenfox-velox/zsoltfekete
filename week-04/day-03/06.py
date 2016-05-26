# create a 300x300 canvas.
# draw a green 10x10 square to its center.

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300' ,bg='black')
canvas.pack()

w = 300
h = 300
square_dimension = 10
box_1 = (w - square_dimension)/2
box_2 = (h - square_dimension)/2
box_3 = (w + square_dimension)/2
box_4 = (h + square_dimension)/2

box = canvas.create_rectangle(box_1, box_2, box_3, box_4, fill='green')

root.mainloop()
