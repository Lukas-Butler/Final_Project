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
            Engine_Room.view_map()
        elif choice == "move":
            while g.moving:
                print("which direction would you like to go: ")
                if barbara.location == [2,4] and barbara.map == Engine_Room:
                    pass
                if barbara.location == [2,0] and barbara.map == living_place:
                    pass
                if barbara.location == [2,4] and barbara.map == living_place:
                    pass
                if barbara.location == [2,0] and barbara.map == command_center:
                    pass
                barbara.movement()
        elif choice == "quit":
            g.playing = False
            quit()
        else:
            print("not an option... try again")

Engine_Room = m.map("Engine_Room",[2,4], r.Engine_Room)
living_place = m.map("Living Place",[2,2],r.living_place)
command_center = m.map("Command Center",[2,0],r.command_center)
barbara = p.Player("Barbara", Engine_Room)
action()