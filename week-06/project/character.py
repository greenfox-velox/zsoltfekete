from tkinter import *
from maps import *
import random

class Character():
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.size = 72
        self.dice =random.randint(1,6)
        self.zero = 5

    def draw_image(self, picture, canvas):
        canvas.create_image( self.zero + self.row * self.size , self.zero + self.column * self.size , image=picture,anchor = NW)

    def hurt(self,strike_value):
        self.curHP=self.curHP-strike_value
        if self.curHP < 0 :
            self.die()

    def die(self):
        self.row = 11
        self.column = 11

class Hero(Character):
    def __init__(self,row,column):
        super().__init__(row,column)
        self.photo_hero_movement = PhotoImage(file = 'picture/herodown.gif')
        self.gameboard = gameboard
        self.level = 1
        self.maxHP = 20 + self.dice + self.dice + self.dice
        self.curHP = 30
        self.DP =self.dice+self.dice
        self.SP = 5 + self.dice

    def draw_character(self, canvas):
        self.draw_image(self.photo_hero_movement, canvas)

    def hero_down(self):
        self.turn_down()
        self.column += 1

    def turn_down(self):
        self.photo_hero_movement = PhotoImage(file = 'picture/herodown.gif')

    def hero_up(self):
        self.turn_up()
        self.column -= 1

    def turn_up(self):
        self.photo_hero_movement = PhotoImage(file = 'picture/heroup.gif')

    def hero_right(self):
        self.turn_right()
        self.row += 1

    def turn_right(self):
        self.photo_hero_movement = PhotoImage(file = 'picture/heroright.gif')

    def hero_left(self):
        self.turn_left()
        self.row -= 1

    def turn_left(self):
        self.photo_hero_movement = PhotoImage(file = 'picture/heroleft.gif')


class Monster(Character):
    def __init__(self,row,column):
        super().__init__(row,column)
        self.level = 1
        self.maxHP = 2 * self.level * self.dice
        self.curHP = self.maxHP
        self.DP = self.level / 2 * self.dice
        self.SP = self.level + self.dice
        self.photo_monster = PhotoImage(file = 'picture/skeleton.gif')

    def draw_character(self, canvas):
        self.draw_image(self.photo_monster, canvas)

class Boss(Character):
    def __init__(self,row,column):
        super().__init__(row,column)
        self.level = 1
        self.maxHP = (2 * self.level + 1) * self.dice
        self.curHP = self.maxHP
        self.DP = self.level * (1+ self.dice)/ 2
        self.SP = self.level * (1+ self.dice)
        self.photo_boss = PhotoImage(file = 'picture/boss.gif')

    def draw_character(self, canvas):
        self.draw_image(self.photo_boss, canvas)
