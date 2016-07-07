from game import *

class Main():
    def __init__(self):
        root = Tk()
        canvas = Canvas(width=1000, height=725, bg='black')
        game = Game(canvas)
        game.draw_all()
        root.bind('<KeyPress>', game.keypress)
        canvas.pack()
        root.mainloop()
Main()
