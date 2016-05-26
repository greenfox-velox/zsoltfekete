# create a 300x300 canvas.
# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.

from tkinter import *
import random

root = Tk()

canvas = Canvas(root, width='300', height='300' ,bg='black')
canvas.pack()

w = 300
h = 300

def box(dim):
    box_1 = (w - dim)/2
    box_2 = (h - dim)/2

    box = canvas.create_rectangle(box_1, box_2, box_1+dim, box_2+dim, fill = "#"+("%06x"%random.randint(0,16777215)))

for dim in range(300, 10, -10):
    box(dim)

root.mainloop()
