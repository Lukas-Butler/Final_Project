#imports 
import random as r
import player as p
import global_variables as g
#variables
col = 0
row = 0

class Item:
    def __init__(self, name, description, value, ):
        self.name = name
        self.description = description
        self.value = value

        self.location = 0
    #tells the description of the item
    def print_description(self):
        return f"You found a {self.description}."
    #spawns and item at  random location and says the location
    def spawn_item(self, item):
        row = r.randrange(0,5)
        col = r.randrange(0,5)
        spawn = [row,col]
        self.location = spawn
        print(f"{item.name} has spawned at{row,col}")



