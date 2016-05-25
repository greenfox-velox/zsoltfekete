
from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300' ,bg='white')
canvas.pack()

w = 300
h = 300
line_number = 20;

def line(x,y,w,h):
    green_line = canvas.create_line(x, y, w, h, fill='green')

for i in range(0,line_number):
    x = i * w /(line_number-1)
    y = i * h /(line_number-1)
    line(0, y, x, h)
    line(x, 0, w, y)
root.mainloop()
