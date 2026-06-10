import player as p
import random as rand

row = [0]
col = [0]


class Enemy:
    def __init__(self, species, location, row, col):
        self.species = species
        self.location = location
        self.row = row
        self.col = col


    def enemy_move(self, row, col):
        if rand.randrange(0,2) == 0:
            self.row[0] + rand.randrange(0,2)
        elif rand.randrange(0,1) == 1:
            self.col[0] + rand.randrange(0,2)


    def move(self, direction, row, col, map):
        if p.direction == "up":
            self.enemy_move(row, col)
        elif p.direction == "down":
            self.enemy_move(row, col)
        elif p.direction == "right":
            self.enemy_move(row, col)
        elif p.direction == "left":
            self.enemy_move(row, col)
