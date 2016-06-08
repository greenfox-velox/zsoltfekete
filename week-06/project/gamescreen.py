from maps import *
from tile import *

class Gamescreen():
    def __init__(self,canvas):
        self.canvas=canvas

    def read_maps(self,ROWS,COLUMNS,gameboard):
        self.M=[]
        for column in range(COLUMNS):
            for row in range(ROWS):
                self.create_list_for_gamescreen(row, column, gameboard)

    def create_list_for_gamescreen(self,row,column,gameboard):
        if gameboard[column][row] == 0 :
            self.M.append(Floor(self.canvas,row,column))
        else:
            self.M.append(Wall(self.canvas,row,column))

    def draw_gamescreen(self):
        for i in self.M:
            i.draw()
