from tabulate import tabulate as t
class map:    
    def __init__(self, name, start, grid):
        self.name = name
        self.starting_coordinates = start
        self.grid = grid

    def view_map(self):
        print(t(self.grid,tablefmt="double_grid"))