from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300' ,bg='white')
canvas.pack()

def box(postion):
    dim = 20
    box = canvas.create_rectangle(position, position, position+dim, position+dim, fill = 'purple')

for position in range(10, 200, 20):
    box(position)

root.mainloop()
