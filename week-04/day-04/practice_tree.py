import tkinter as tk
import math
root = tk.Tk()

canvas = tk.Canvas(root, width=700, height=700, bg='#002530')
canvas.pack()

def tree(x1, y1, angle, length, number_of_repetitions):
    x2 = x1 + int(math.cos(math.radians(angle)) * length)
    y2 = y1 + int(math.sin(math.radians(angle)) * length)
    canvas.create_line(x1, y1, x2, y2, fill='#FFD300')
    if number_of_repetitions <= 0:
        pass
    else:
        tree( x2, y2, (angle - 25), length-5, number_of_repetitions - 1)
        tree( x2, y2, (angle + 25), length-5, number_of_repetitions - 1)
        tree( x2, y2, (angle), length, number_of_repetitions - 1)

def draw_tree(x1, y1, length ,number_of_repetitions):
    angle = 270
    tree( x1, y1, angle, length, number_of_repetitions)

draw_tree( 350, 600, 60, 8)

root.mainloop()
