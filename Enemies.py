import player as p
import Room as r
import random as rand



class Enemy:
    def __init__(self, species, location, r):
        self.species = species
        self.location = location
        self.map = r

    def move (self, p.location, p.direction, row, col, map):
        if p.location == p.direction == "up":
            row[0] + rand.randrange(0,2) col[0] + rand.randrange(0,2)
        else:
            print("The enemy decided to not move")
        elif p.location == p.direction == "down":
            
        elif p.location == p.direction == "right":
            
        elif p.location == p.direction == "left":
            