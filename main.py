#imports of different python code
import player as p
import map as m
import Room as r
import global_variables as g

def introduction():
    print("Your Barbara, the best of the best, and your invading,"
    "a ship that has Viltrumites aliens on on and you need,"
    "to gather items to repair your ship. Don't get caught!")
    print('Press "c" to proceed')
    print('Press "q" to quit')
    choice = input("Choice: ").lower()
    if choice == "c":
        print("Radical!")
        p.playing = True
    elif choice == "q":
        p.playing = False
        quit()
    else:
        print("Hey! listen here pal, we aren't even in the game and yet your acting like a simpleton!, try again")
        introduction()


def action():
    while g.playing:
        g.moving = True
        print("choose one of the following options")
        print(" - view the map (map)")
        print(" - move through the map (move)")
        print(" - quit the game (quit)")
        choice = input("Choice: ").lower()
        # if the choice is map do this
        if choice == "map":
            #gets the current map the player is on and tabulates
            g.current_location.view_map()
        # if the choice is move do this
        elif choice == "move":
            while g.moving:
                print("which direction would you like to go: ")
                #if the player location is door and map on engine room do this
                if barbara.location == [2,4] and barbara.map == g.Engine_Room:
                   #makes the map to living place and makes them spawn at [2,1]
                   g.current_location = g.living_place
                   barbara.map = g.current_location
                   barbara.location = [2,1]
                #if the player location is stair and map on living place do this
                if barbara.location == [2,0] and barbara.map == g.living_place:
                   #makes the map to engine room and makes them spawn at [2,3]
                   g.current_location = g.Engine_Room
                   barbara.map = g.current_location
                   barbara.location = [2,3]
                #if the player location is elevator and map on living place do this
                if barbara.location == [2,4] and barbara.map == g.living_place:
                   #makes the map to command center and makes them spawn at [2,1]
                   g.current_location = g.command_center
                   barbara.map = g.current_location
                   barbara.location = [2,1]
                #if the player location is door and map on command center do this
                if barbara.location == [2,0] and barbara.map == g.command_center:
                   #makes the map to living place and makes them spawn at [2,3]
                   g.current_location = g.living_place
                   barbara.map = g.current_location
                   barbara.location = [2,3]
                #call on the movement script
                barbara.movement()
        #if the choice is quit od this
        elif choice == "quit":
            #make playing false and stop the game
            g.playing = False
            quit()
        #if choice does not equal any of those do this 
        else:
            print("not an option... try again")
#make a player class as barbara
barbara = p.Player("Barbara", g.Engine_Room)
introduction()
action()
