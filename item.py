import random as r
col = 0
row = 0
spawn = [col,row]
class Item:
    def __init__(self, name, description, value, location):
        self.name = name
        self.description = description
        self.value = value
        self.location = location

    def print_description(self):
        return(self.description)
    def spawn_item(self):
        row = r.randrange(0,5)
        col = r.randrange(0,5)
        

scrap = Item("Scrap", "description", 1,spawn)
goo = Item("Goo", "description", 2,spawn)
engine = Item("Engine", "description", 3,spawn)
money = Item("Money", "description", 4,spawn)

rarity = [scrap, scrap, goo, goo, goo, goo, engine, 
          engine, engine, money, money]
