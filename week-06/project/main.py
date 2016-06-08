from maps import *
from gamescreen import *
from character import *
from statistic import *

class Play():
    def __init__(self):
        root = Tk()
        canvas = Canvas(width=1000, height=725, bg='black')

        joey = Hero(0,0,canvas,gameboard)

        game = Gamescreen(canvas)
        game.read_maps(ROWS,COLUMNS,gameboard)
        game.draw_gamescreen()

        skeleton_1 = Monster(8,7,canvas)
        skeleton_1.draw()

        skeleton_2 = Monster(5,7,canvas)
        skeleton_2.draw()

        skeleton_3 = Monster(3,4,canvas)
        skeleton_3.draw()

        boss = Boss(9,9,canvas)
        boss.draw()

        stat = Statistic(canvas,joey)
        stat.draw_hero_stat()

        controller =Controller(joey)
        root.bind('<KeyPress>', controller.hero_move)
        joey.draw()

        canvas.pack()
        root.mainloop()

Play()
