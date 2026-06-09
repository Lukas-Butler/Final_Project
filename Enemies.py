import player as p
import Room as r
import random as rand

row = [0]
col = [0]

class Enemy:
    def __init__(self, species, location, r):
        self.species = species
        self.location = location


    def enemy_move(self, row, col):
        if rand.randrange(0,2) == 0:
            self.row[0] + rand.randrange(0,2)
        elif rand.randrange(0,1) == 1:
            self.col[0] + rand.randrange(0,2)


    def move(self, p.location, p.direction, row, col):
        if p.location == p.direction == "up":
            self.enemy_move(row, col)
        elif p.location == p.direction == "down":
            self.enemy_move(row, col)
        elif p.location == p.direction == "right":
            self.enemy_move(row, col)
        elif p.location == p.direction == "left":
            self.enemy_move(row, col)