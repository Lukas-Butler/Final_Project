class Item:
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
        
    def print_description(self):
        return(self.description)
    
scrap = Item("Scrap", "description", 1)
goo = Item("Goo", "description", 2)
engine = Item("Engine", "description", 3)
money = Item("Money", "description", 4)

rarity = [scrap, scrap, goo, goo, goo, goo, engine, 
          engine, engine, money, money]

