from tkinter import *
from maps import *

class Tile():
    def __init__(self,canvas,row,column):
        self.row = row
        self.column = column
        self.canvas =canvas
        self.size = 72

    def draw_image(self, picture):
        self.canvas.create_image( 5 + self.row * self.size , 5 + self.column * self.size , image=picture,anchor = NW)

class Floor(Tile):
    def __init__(self,canvas,row,column):
        super().__init__(canvas,row,column)
        self.photo_floor = PhotoImage(file = 'picture/stone.gif')

    def draw(self):
        self.draw_image(self.photo_floor)

class Wall(Tile):
    def __init__(self,canvas,row,column):
        super().__init__(canvas,row,column)
        self.photo_wall = PhotoImage(file = 'picture/wall.gif')

    def draw(self):
        self.draw_image(self.photo_wall)
