import player as p
import random as rand
import map as m
import Room as r

#Base row and column
row = [0]
col = [0]

class Enemy: # A class for the enemy in the game
    def __init__(self, species, location, row, col):
        self.species = species
        self.location = location
        self.row = row
        self.col = col

    def enemy_move(self, row, col): # A function that randomly moves the enemy around the map
        if rand.randrange(0,2) == 0:
            self.row[0] + rand.randrange(0,2)
        elif rand.randrange(0,1) == 1:
            self.col[0] + rand.randrange(0,2)

    def move(self, direction, row, col, room, map): #The funtion that makes the enemy move when the player moves
        if p.direction == "up":
            self.enemy_move(row, col)
        elif p.direction == "down":
            self.enemy_move(row, col)
        elif p.direction == "right":
            self.enemy_move(row, col)
        elif p.direction == "left":
            self.enemy_move(row, col)

        if 0 <= row< len(map) and 0 <= col < len(map[0]): # Keeps the enemy on the map
            Enemy["row"] = row
            Enemy["col"] = col
            map()