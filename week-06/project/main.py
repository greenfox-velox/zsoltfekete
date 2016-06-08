from maps import *
from gamescreen import *
from character import *

class Play():
    def __init__(self):
        root = Tk()
        canvas = Canvas(width=725, height=725)

        game = Gamescreen(canvas)
        game.read_maps(ROWS,COLUMNS,gameboard)
        game.draw_gamescreen()

        hero = Hero(0,0,canvas,gameboard)
        hero.draw()
        monster = Monster(5,6,canvas)
        monster.draw()
        boss = Boss(9,9,canvas)
        boss.draw()

        root.bind("<Down>", hero.move_down)
        root.bind("<Up>", hero.move_up)
        root.bind("<Right>", hero.move_right)
        root.bind("<Left>", hero.move_left)

        canvas.pack()
        root.mainloop()

Play()
