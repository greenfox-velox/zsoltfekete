from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300' ,bg='white')
canvas.pack()

w = 300
h = 300
line_number = 60;
center_w = w/2
center_h = h/2

def green_line (x,y,w,h):
    green_line = canvas.create_line(x, y, w, h, fill='green')

for i in range(1,line_number):
    x = i * center_w /(line_number-1)

    y = (line_number-i)  * center_h /(line_number-1)
    green_line(center_w, y, x, center_h)
    y = (line_number-i)  * center_h /(line_number-1)
    green_line(center_w, center_h+y, x+center_w, center_h)
    y = (i)  * center_h /(line_number-1)
    green_line(x, center_h, center_w,center_h+y)
    y = i  * center_h /(line_number-1)
    green_line(center_w, y, x+center_w, center_h)

root.mainloop()
