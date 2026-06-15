class Item:
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
    def print_description(self):
        return(self.description)
    
scrap = Item("Scrap", "description", 1)
goop = Item("Goop", "description", 2)
engine = Item("Engine", "description", 3)
money = Item("Money", "description", 4)

rarity = [scrap, scrap, goop, goop, goop, goop, engine, 
          engine, engine, money, money]
