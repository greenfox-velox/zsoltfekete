from tkinter import *
root = Tk()
canvas = Canvas(root, width= 820, height= 670, bg= '#002530')
canvas.pack()

def hexagon(x, y ,size):
    h =size/(3/2)**(1/2)
    canvas.create_polygon( x, y, x + size/2 , y - h, x+ 3/2 * size, y - h, x+2 * size, y, x+ 3/2 * size, y + h, x + size/2, y + h, outline='#FFD300'  ,fill= '#002530')
    if size <= 5:
        pass
    else:
        dim = size / 3
        h = h / 1.5
        hexagon(x, y, dim)
        hexagon(x + size / 3, y - h, dim)
        hexagon(x + size, y - h, dim)
        hexagon(x + 4 * size / 3, y, dim)
        hexagon(x + size, y + h, dim)
        hexagon(x + size / 3, y + h, dim)
hexagon(100, 300 ,300)
root.mainloop()
