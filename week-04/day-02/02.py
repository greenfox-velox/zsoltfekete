from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300' ,bg='black')
canvas.pack()

p1 = 50
p2 = 50
p3 = 250
p4 = 250

red_line = canvas.create_line(p1, p2, p3, p1, fill='red')
blue_line = canvas.create_line(p3, p1, p4, p3, fill='blue')
green_line = canvas.create_line(p3, p4, p2, p4, fill='green')
white_line = canvas.create_line(p2, p4, p1, p2, fill='white')

root.mainloop()
