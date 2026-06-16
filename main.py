##############################################################################
# Title: Mini Map
# Name: Lukas,Svannah,Kaleb
# Class: CS30
# Date: 7 june, 2026
# Version: 2.8
##############################################################################
""" move around map nd collect items on a move limit """
##############################################################################
# Imports and Global Variables -----------------------------------------------
import global_variables as g
import bag as b
import map as m
import player as p
import item as i
import random as r
import highscore as h
import item as i
# Functions ------------------------------------------------------------------
def introduction(): # Starts the game and tells the player the story
    print("Your Barbara, the best of the best, and your invading,\n"
    "a ship that has Viltrumites aliens on and you need,\n"
    "to gather items to repair your ship. Don't get caught!")
    print("items will spawn every 10 movements and then \n" 
    "will disaper after another 10 movements so move fast \n" 
    "to grabe them and don't miss out")
    h.getHighScore()
    print(f"Current high score: {h.highScore}")
    # Options for the player to choose from
    print('Press "c" to proceed')
    print('Press "q" to quit')
    choice = input("Choice: ").lower()  #The player picks an option
    if choice == "c": # 'C' starts the game
        print("Radical!")
        p.playing = True
    elif choice == "q": # 'Q' quits the game
        print("Fine! like I care! see ya loser!")
        p.playing = False
        quit()
    else:
        # If the player doesnt comply with the instructions, They get 
        # insulted and the intro repeats
        print("Hey! listen here pal, we aren't even in the game and " \
        "yet your acting like a simpleton!, try again")
        introduction()


def action(): # The actual game itself
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
            treasure = r.choice(rarity)
            found.spawn_item(treasure)
            while g.moving:
                print("which direction would you like to go: ")
                #if the player and the item are on the same location 
                # put it the players bag
                if barbara.location == found.location:
                    barbara.keep(treasure)
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
                #after 10 movements spawn an item
                if g.count >= 10:
                    treasure = r.choice(rarity)
                    found.spawn_item(treasure)
                    g.count = 0
                #call on the movement script
                barbara.movement()
                #print the players loction
                print(f"barbara is at location {barbara.location}")
                g.count += 1
        elif choice == "quit":
            #make playing false and stop the game
            g.playing = False
        #if choice does not equal any of those do this 
        else:
            print("not an option... try again")

def ending():
    barbara.calculate_score()
    print("you go back to your ship and repair it")

#make a player class as barbara
barbara = p.Player("Barbara", g.Engine_Room, 10)
# Items in the game
scrap = i.Item("Scrap", "Scrap metal", 1,  )
goop = i.Item("Goop", "Strange Thick liquid", 2,  )
engine = i.Item("Engine", "Self explanatory", 3,  )
money = i.Item("Money", "Self explanatory, but just" \
"because I have to, its currency", 4, )
rarity = [scrap, scrap, goop, goop, goop, goop, engine, # The rarity of the items
          engine, engine, money, money]
found = r.choice(rarity)
introduction()
action()
ending()