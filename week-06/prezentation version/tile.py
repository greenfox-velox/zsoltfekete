from tkinter import *

class Tile():
    def __init__(self,row,column):
        self.row = row
        self.column = column
        self.size = 72
        self.photo_floor = PhotoImage(file = 'picture/stone.gif')
        self.photo_wall = PhotoImage(file = 'picture/wall.gif')

    def draw_tile(self, picture, canvas):
        canvas.create_image( 5 + self.row * self.size , 5 + self.column * self.size , image = picture,anchor = NW)

class Floor(Tile):
    def __init__(self,row,column):
        super().__init__(row,column)

    def draw(self,canvas):
        self.draw_tile(self.photo_floor, canvas)

class Wall(Tile):
    def __init__(self,row,column):
        super().__init__(row,column)

    def draw(self,canvas):
        self.draw_tile(self.photo_wall, canvas)
