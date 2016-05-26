from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300' ,bg='black')
canvas.pack()

w = 300
h = 300

red_line = canvas.create_line(w/2, 0, w/2, h/2, fill='red')
green_line = canvas.create_line(0, h/2, w/2, h/2, fill='green')

root.mainloop()
