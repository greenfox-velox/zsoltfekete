# create a 300x300 canvas.
# fill it with a checkerboard pattern.

from tkinter import *

root = Tk()

canvas = Canvas(root, width='317', height='320' ,bg='white')
canvas.pack()

x = 0
y = 0
dim = 40

def box(x,y,dim):
    box = canvas.create_rectangle(x, y, x+dim, y+dim, fill = 'black')

for n in range(0,8):
    if n % 2 != 0:
        x=dim
    else:
        x=0

    for i in range(0,8):
        box(x,y,dim)
        x += dim * 2
    y += dim

root.mainloop()
