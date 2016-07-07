from tile import *

ROWS = 10
COLUMNS = 10
gameboard = [
            [0,0,1,1,1,1,1,1,1,1],
            [1,0,1,0,1,0,1,0,0,1],
            [1,0,0,0,0,0,0,0,0,1],
            [1,1,0,1,1,1,1,0,1,1],
            [1,0,0,1,0,0,1,0,0,1],
            [1,1,0,1,0,1,1,0,1,1],
            [1,0,0,0,0,0,0,0,0,1],
            [1,1,0,0,0,0,0,1,0,1],
            [1,1,0,1,0,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1],
]

class Map():
    def __init__(self):
        self.ROWS = ROWS
        self.COLUMNS = COLUMNS
        self.gameboard =gameboard
        self.tile_map=[]

    def read_tile(self):
        for column in range(self.COLUMNS):
            for row in range(self.ROWS):
                self.create_list_for_gamescreen(row, column)

    def create_list_for_gamescreen(self, row, column):
        if self.gameboard[column][row] == 0 :
            self.tile_map.append(Floor(row,column))
        else:
            self.tile_map.append(Wall(row,column))

    def draw_tile(self, canvas):
        self.read_tile()
        for tile in self.tile_map:
            tile.draw(canvas)

    def is_the_next_tile_floor(self, next_x, next_y):
        try:
            if self.gameboard[next_y][next_x] == 0 and (next_y) >= 0 and (next_x) >= 0:
                return True
        except IndexError:
            return False

    def is_this_tile_occupied(self, hero_x, hero_y, monster_list):
        if self.get_the_enemy(hero_x, hero_y, monster_list) == False:
            return False
        else:
            return True

    def is_this_move_possible(self,hero_x,hero_y,next_x,next_y,monster_list):
        if self.is_this_tile_occupied(hero_x,hero_y,monster_list) == False and self.is_the_next_tile_floor(next_x,next_y):
            return True

    def  get_the_enemy(self, hero_x, hero_y, monster_list):
        if hero_x == monster_list[0][0] and hero_y == monster_list[0][1] :
            return 'self.boss'
        elif hero_x == monster_list[1][0] and hero_y == monster_list[1][1] :
            return 'self.skeleton_1'
        elif hero_x == monster_list[2][0] and hero_y == monster_list[2][1] :
            return 'self.skeleton_2'
        elif hero_x == monster_list[3][0] and hero_y == monster_list[3][1] :
            return 'self.skeleton_3'
        else:
            return False
