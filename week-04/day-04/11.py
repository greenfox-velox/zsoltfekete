from tkinter import *
root = Tk()
canvas = Canvas(root, width= 686, height= 686, bg= '#002530')
canvas.pack()

def fractal(x,y,size):
    canvas.create_rectangle(x, y, x + size, y + size ,outline= '#FFD300')
    if size <= 5:
        pass
    else:
        dim = size / 3
        fractal(x + dim, y, dim)
        fractal(x, y + dim, dim)
        fractal(x + dim * 2, y + dim, dim)
        fractal(x + dim, y + dim * 2, dim)
fractal(10, 10, 666)
root.mainloop()
