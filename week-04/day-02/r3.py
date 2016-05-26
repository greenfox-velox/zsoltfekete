
from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300' ,bg='white')
canvas.pack()

w = 300
h = 300
line_number = 20;

def green_line (x,y,w,h):
    green_line = canvas.create_line(x, y, w, h, fill='green')

def purple_line (x,y,w,h):
    purple_line = canvas.create_line(x, y, w, h, fill='purple')

for i in range(0,line_number):
    x = i * w /(line_number-1)
    y = i * h /(line_number-1)
    green_line(0, y, x, h)
    purple_line(x, 0, w, y)
root.mainloop()
