
# create a 300x300 canvas.
# fill it with four different size and color rectangles.

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300' ,bg='black')
canvas.pack()

w = 300
h = 300
box_w1 =w/3
box_w2 =w/5
box_h1 =h/3

box = canvas.create_rectangle(0, 0, box_w1, box_h1, fill='green', outline = 'green' )
box = canvas.create_rectangle(0, box_w1, w, box_h1, fill='red', outline = 'red' )
box = canvas.create_rectangle(0, box_h1, box_w2, h, fill='yellow', outline = 'yellow' )
box = canvas.create_rectangle(box_w2, box_h1, w, h, fill='purple', outline = 'purple' )

root.mainloop()
