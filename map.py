from tabulate import tabulate as t
class map:
    def __init__(self, name, start, map):
        self.name = name
        self.starting_coordinates = start
        self.map = map
    def getMap(self):
        return self.map
    def view_map(self):
        print(t(self.map,tablefmt="double_grid"))
    def getStart(self):
        return self.starting_coordinates