import player as p
import map as m
import Room as r
import global_variables as g

def action():
    while g.playing:
        g.moving = True
        print("choose one of the following options")
        print(" - view the map (map)")
        print(" - move through the map (move)")
        print(" - quit the game (quit)")
        choice = input("Choice: ").lower()
        if choice == "map":
            g.current_location.view_map()
        elif choice == "move":
            while g.moving:
                print("which direction would you like to go: ")
                if barbara.location == [2,4] and barbara.map == g.Engine_Room:
                   g.current_location = g.living_place
                   barbara.map = g.current_location
                   barbara.location = [2,1]
                if barbara.location == [2,0] and barbara.map == g.living_place:
                   g.current_location = g.Engine_Room
                   barbara.map = g.current_location
                   barbara.location = [2,3]
                if barbara.location == [2,4] and barbara.map == g.living_place:
                   g.current_location = g.command_center
                   barbara.map = g.current_location
                   barbara.location = [2,1]
                if barbara.location == [2,0] and barbara.map == g.command_center:
                   g.current_location = g.living_place
                   barbara.map = g.current_location
                   barbara.location = [2,3]
                barbara.movement()
        elif choice == "quit":
            g.playing = False
            quit()
        else:
            print("not an option... try again")
barbara = p.Player("Barbara", g.Engine_Room)
action()
