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
        



# Items in the game
scrap = Item("Scrap", "Scrap metal", 1)
goop = Item("Goop", "Strange Thick liquid", 2)
engine = Item("Engine", "Self explanatory", 3)
money = Item("Money", "Self explanatory, but just because I have to, its currency", 4)

rarity = [scrap, scrap, goop, goop, goop, goop, engine, # The rarity of the items
          engine, engine, money, money]
