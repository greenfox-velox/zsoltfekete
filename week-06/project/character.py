from tkinter import *
from maps import *
import random

class Character():
    def __init__(self,row,column,canvas):
        self.row = row
        self.column = column
        self.canvas =canvas
        self.size = 72
        self.dice = self.roll_dice()
        self.zero = 5

    def draw_image(self,picture):
        self.canvas.create_image( self.zero + self.row * self.size , self.zero + self.column * self.size , image=picture,anchor = NW)

    def roll_dice(self):
            random_dice = random.randint(1,6)
            return random_dice

class Hero(Character):
    def __init__(self,row,column,canvas,gameboard):
        super().__init__(row,column,canvas)
        self.photo_hero_movement = PhotoImage(file = 'picture/herodown.gif')
        self.gameboard = gameboard
        self.level = 1
        self.maxHP = 20 + self.dice + self.dice + self.dice
        self.curHP = 30
        self.DP =self.dice+self.dice
        self.SP = 5 + self.dice

    def draw(self):
        return self.draw_image(self.photo_hero_movement)

    def check_the_next_tile(self, next_x, next_y):
        try:
            if self.gameboard[self.column+next_y][self.row+next_x] == 0 and (self.column+next_y) >= 0 and self.row+next_x >= 0:
                return True
        except IndexError:
            return False

    def hero_down(self):
        self.photo_hero_movement = PhotoImage(file = 'picture/herodown.gif')
        if self.check_the_next_tile(0, 1):
            self.column += 1
        self.draw()

    def hero_up(self):
        self.photo_hero_movement = PhotoImage(file = 'picture/heroup.gif')
        if self.check_the_next_tile(0, -1):
            self.column -= 1
        self.draw()

    def hero_right(self):
        self.photo_hero_movement = PhotoImage(file = 'picture/heroright.gif')
        if self.check_the_next_tile(1, 0):
            self.row += 1
        self.draw()

    def hero_left(self):
        self.photo_hero_movement = PhotoImage(file = 'picture/heroleft.gif')
        if self.check_the_next_tile(-1, 0):
            self.row -= 1
        self.draw()

class Monster(Character):
    def __init__(self,canvas,row,column):
        super().__init__(canvas,row,column)
        self.photo_monster = PhotoImage(file = 'picture/skeleton.gif')
        self.level = 1
        self.maxHP = 2 * self.level * self.dice
        self.curHP = self.maxHP
        self.DP = self.level / 2 * self.dice
        self.SP = self.level + self.dice

    def draw(self):
        self.draw_image(self.photo_monster)

class Boss(Character):
    def __init__(self,canvas,row,column):
        super().__init__(canvas,row,column)
        self.level = 1
        self.maxHP = (2 * self.level + 1) * self.dice
        self.curHP = self.maxHP
        self.DP = self.level * (1+ self.dice)/ 2
        self.SP = self.level * (1+ self.dice)
        self.photo_boss = PhotoImage(file = 'picture/boss.gif')

    def draw(self):
        self.draw_image(self.photo_boss)
