from tkinter import *
root = Tk()
canvas = Canvas(root, width= 820, height= 670, bg= '#002530')
canvas.pack()

def delta(x, y ,size):
    height = (3/2)**(1/2)
    canvas.create_polygon(x, y, x+size, y,x+size/2 ,y+(size/height),  outline='#FFD300'  ,fill= '#002530')
    if size <= 5:
        pass
    else:
        dim = size / 2

        delta(x, y, dim)
        delta(x + dim* 2, y, dim)
        delta(x + dim , y + dim/height* 2, dim)

delta(10, 10 ,400)

root.mainloop()
