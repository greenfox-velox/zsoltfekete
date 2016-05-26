from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300' ,bg='black')
canvas.pack()

w = 300
h = 300
center_1 = w/2
center_2 = h/2

green_line = canvas.create_line(0, 0, center_1, center_2, fill='green')
green_line = canvas.create_line(0, w, center_1, center_2, fill='green')
green_line = canvas.create_line(h, w, center_1, center_2, fill='green')
green_line = canvas.create_line(h, 0, center_1, center_2, fill='green')

root.mainloop()
