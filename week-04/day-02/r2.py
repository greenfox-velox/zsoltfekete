from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300' ,bg='white')
canvas.pack()

dim = 10
pos = 0
def box(pos,dim):
    box = canvas.create_rectangle(pos, pos, pos+dim, pos+dim, fill = 'purple')

for n in range(1, 7):
    pos += dim
    dim += 10
    box(pos,dim)

root.mainloop()
