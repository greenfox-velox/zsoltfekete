from tkinter import *
from maps import *

class Character():
    def __init__(self,row,column,canvas):
        self.row = row
        self.column = column
        self.canvas =canvas
        self.size = 72

    def draw_image(self,picture):
        self.canvas.create_image( 5 + self.row * self.size , 5 + self.column * self.size , image=picture,anchor = NW)

class Hero(Character):
    def __init__(self,row,column,canvas,gameboard):
        super().__init__(row,column,canvas)
        self.photo_hero_movement = PhotoImage(file = 'picture/herodown.gif')
        self.gameboard=gameboard

    def draw(self):
        self.draw_image(self.photo_hero_movement)

    def move_down(self,event):
        try:
            if self.gameboard[self.column+1][self.row] == 0:
                self.photo_hero_movement = PhotoImage(file = 'picture/herodown.gif')
                self.column += 1
                self.draw()
        except IndexError:
            pass

    def move_up(self,event):
        if self.gameboard[self.column-1][self.row] == 0:
            self.photo_hero_movement = PhotoImage(file = 'picture/heroup.gif')
            if self.column > 0 :
                self.column -= 1
            self.draw()

    def move_right(self,event):
        try:
            if self.gameboard[self.column][self.row+1] == 0:
                self.photo_hero_movement = PhotoImage(file = 'picture/heroright.gif')
                self.row += 1
                self.draw()
        except IndexError:
            pass

    def move_left(self,event):
        if self.gameboard[self.column][self.row-1] == 0:
            self.photo_hero_movement = PhotoImage(file = 'picture/heroleft.gif')
            if self.row > 0 :
                self.row -= 1
            self.draw()

class Monster(Character):
    def __init__(self,canvas,row,column):
        super().__init__(canvas,row,column)
        self.photo_monster = PhotoImage(file = 'picture/skeleton.gif')

    def draw(self):
        self.draw_image(self.photo_monster)

class Boss(Character):
    def __init__(self,canvas,row,column):
        super().__init__(canvas,row,column)
        self.photo_boss = PhotoImage(file = 'picture/boss.gif')

    def draw(self):
        self.draw_image(self.photo_boss)
