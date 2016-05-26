# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# fill the canvas with lines from the edges, every 20 px, to the center.

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300' ,bg='black')
canvas.pack()

w = 300
h = 300

def line(x,y):
    center_1 = w/2
    center_2 = h/2
    green_line = canvas.create_line(x, y, center_1, center_2, fill='green')

for n in range(16):
    x = n * 20
    y = n * 20
    line(x,0)
    line(x,300)
    line(0,y)
    line(300,y)

root.mainloop()
