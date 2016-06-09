from maps import *
from tile import *
from character import *
from statistic import *
import random

class Game():
    def __init__(self,canvas):
        self.canvas = canvas
        self.joey = Hero(0,0)
        self.game_map = Map()
        self.dice =random.randint(1,6)
        self.skeleton_1 = Monster(8,7)
        self.skeleton_2 = Monster(5,7)
        self.skeleton_3 = Monster(3,4)
        self.boss = Boss(9,9)
        self.stat = Statistic(self.joey,self.skeleton_1,self.skeleton_2,self.skeleton_3,self.boss,self.canvas)
        self.monster_position =[(self.boss.row,self.boss.column),(self.skeleton_1.row,self.skeleton_1.column),(self.skeleton_2.row,self.skeleton_2.column),(self.skeleton_3.row,self.skeleton_3.column)]

    def draw_all(self):
        self.game_map.draw_tile(self.canvas)
        self.joey.draw_character(self.canvas)
        self.skeleton_1.draw_character(self.canvas)
        self.skeleton_2.draw_character(self.canvas)
        self.skeleton_3.draw_character(self.canvas)
        self.boss.draw_character(self.canvas)
        self.stat.draw_hero_stat()

    def keypress(self,event):
        if event.keysym == 'Up':
            self.move_up()

        elif event.keysym == 'Down':
            self.move_down()

        elif event.keysym == 'Right':
            self.move_right()

        elif event.keysym == 'Left':
            self.move_left()

        elif event.keysym == 'space':
            self.start_the_battle()

    def start_the_battle(self):
        if self.game_map.is_this_tile_occupied(self.joey.row,self.joey.column,self.monster_position):
            self.strike(self.game_map.get_the_enemy(self.joey.row,self.joey.column,self.monster_position))

    def strike(self,attacker):
        if attacker == 'self.boss':
            self.stat.draw_skeleton_boss
            self.strike_1=self.joey.SP+self.dice+self.dice
            self.strike_2=self.boss.SP+self.dice+self.dice
            if self.strike_1 > self.boss.DP:
                self.boss.hurt(self.strike_1)
            if self.strike_2+self.dice+self.dice > self.joey.DP:
                self.joey.hurt(self.strike_2)


        elif attacker == 'self.skeleton_1':
            self.stat.draw_skeleton_stat_1()
            self.strike_1=self.joey.SP+self.dice+self.dice
            self.strike_2=self.skeleton_1.SP+self.dice+self.dice
            if self.strike_1 > self.skeleton_1.DP:
                self.skeleton_1.hurt(self.strike_1)
            if self.strike_2+self.dice+self.dice > self.joey.DP:
                self.joey.hurt(self.strike_2)


        elif attacker == 'self.skeleton_2':
            self.stat.draw_skeleton_stat_2()
            self.strike_1=self.joey.SP+self.dice+self.dice
            self.strike_2=self.skeleton_2.SP+self.dice+self.dice
            if self.strike_1 > self.skeleton_2.self.DP:
                self.skeleton_2.hurt(self.strike_1)
            if self.strike_2+self.dice+self.dice > self.joey.DP:
                self.joey.hurt(self.strike_2)

        elif attacker == 'self.skeleton_3':
            self.stat.draw_skeleton_stat_3()
            self.strike_1=self.joey.SP+self.dice+self.dice
            self.strike_2=self.skeleton_3.SP+self.dice+self.dice
            if self.strike_1 > self.skeleton_3.DP:
                self.skeleton_3.hurt(self.strike_1)
            if self.strike_2+self.dice+self.dice > self.joey.DP:
                self.joey.hurt(self.strike_2)


    def move_up(self):
        if self.game_map.is_this_move_possible(self.joey.row,self.joey.column,self.joey.row,self.joey.column-1,self.monster_position):
            self.joey.hero_up()
        else:
            self.joey.turn_up()
        self.joey.draw_character(self.canvas)

    def move_down(self):
        if self.game_map.is_this_move_possible(self.joey.row,self.joey.column,self.joey.row,self.joey.column+1,self.monster_position):
            self.joey.hero_down()
        else:
            self.joey.turn_down()
        self.joey.draw_character(self.canvas)

    def move_right(self):
        if self.game_map.is_this_move_possible(self.joey.row,self.joey.column,self.joey.row+1,self.joey.column,self.monster_position):
            self.joey.hero_right()
        else:
            self.joey.turn_right()
        self.joey.draw_character(self.canvas)

    def move_left(self):
        if self.game_map.is_this_move_possible(self.joey.row,self.joey.column,self.joey.row-1,self.joey.column,self.monster_position):
            self.joey.hero_left()
        else:
            self.joey.turn_left()
        self.joey.draw_character(self.canvas)
