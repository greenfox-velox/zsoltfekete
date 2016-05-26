# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a 50 long horizontal line from that point.
# draw 3 lines with that function.

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300' ,bg='black')
canvas.pack()

def line(x,y):
    length = 50
    green_line = canvas.create_line(x, y, x, y+length, fill='green')

line(40,50)
line(9,99)
line(222,111)

root.mainloop()
