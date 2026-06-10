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
                barbara.movement()
        elif choice == "quit":
            g.playing = False
            quit()
        else:
            print("not an option... try again")

barbara = p.Player("Barbara", r.Engine_Room)
Engine_Room = m.map("Engine_Room",[0,0], r.Engine_Room)
action()
