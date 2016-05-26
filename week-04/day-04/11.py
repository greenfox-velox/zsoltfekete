from tkinter import *

root = Tk()

canvas_width= 500
canvas_height= 500

canvas = Canvas(root, width= canvas_width, height= canvas_height)
canvas.pack()

x = canvas_width/3
y = canvas_height/3

def box():
    greenSquare = canvas.create_rectangle(1 * x, 0, 2 * x, 1 * y, fill ='green')
    greenSquare = canvas.create_rectangle(0, 1 * y, 1 * x, 2 * y, fill ='green')
    greenSquare = canvas.create_rectangle(2 * x, 1 * y, 3 * x, 2 * y, fill ='green')
    greenSquare = canvas.create_rectangle(1 * x, 2 * y, 2 * x, 3 * y, fill ='green')

root.mainloop()
print(box())


def fractal(n):
    if n <= 1:
        return box()
    else:
        return box()+fractal(x/3,y/3)

print (fractal(50))
