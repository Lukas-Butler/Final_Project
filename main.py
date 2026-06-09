import player as p
import Room as r

def action():
    print("choose one of the following options")
    print(" - view the map (map)")
    print(" - move thourgh the map (move)")
    print(" - quite the game (quit)")
    choice = input("Choice: ").lower()
    if choice == "map":
        pass
    elif choice == "move":
        barbara.movement()
    elif choice == "quit":
        quit()
    else:
        print("not an option... try again")


barbara = p.Player([0,0],"Barbara", r.Engine_Room)
action()
