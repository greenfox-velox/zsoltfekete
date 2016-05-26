# create a 300x300 canvas.
# create a square drawing function that takes 2 parameters:
# the x and y coordinates of the square's top left corner
# and draws a 50x50 square from that point.
# draw 3 squares with that function.
from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300' ,bg='black')
canvas.pack()

def box(x,y):
    dim = 50
    box = canvas.create_rectangle(x, y, x+dim,y+dim, fill='green', outline = 'green' )

box(10,10)
box(20,190)
box(170,170)

root.mainloop()
