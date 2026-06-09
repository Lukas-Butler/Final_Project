import player as p
import map as m
import Room as r

def action():
    while True:
        print("choose one of the following options")
        print(" - view the map (map)")
        print(" - move through the map (move)")
        print(" - quit the game (quit)")
        choice = input("Choice: ").lower()
        if choice == "map":
            Engine_Room.view_map()
        elif choice == "move":
            barbara.movement()
        elif choice == "quit":
            quit()
        else:
            print("not an option... try again")


barbara = p.Player([0,0],"Barbara", r.Engine_Room)
Engine_Room = m.map("Engine_Room",[2,4], r.Engine_Room)
action()
