# create a 300x300 canvas.
# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# draw 3 squares with that function.

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300' ,bg='black')
canvas.pack()

w = 300
h = 300

def box(dim):

    box_1 = (w - dim)/2
    box_2 = (h - dim)/2
    box = canvas.create_rectangle(box_1, box_2, box_1+dim, box_2+dim, fill='green', )

box(200)
box(120)
box(50)

root.mainloop()
