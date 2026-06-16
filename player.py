#importants map,room and global varibal code
import map as m
import Room as r
import global_variables as g
import bag as b
import highscore as h
import random as r
import item as i
#variables
max_row = 4
mini_row = 0
mini_column = 0
max_column = 4

class Player:
    #what is need when a player object is needed and used
    def __init__(self, name, game_map, bagCapacity):
        self.location =  g.current_location.getStart()
        self.name = name
        self.map = game_map
        self.bag = b.Bag(bagCapacity)

    #get the map the player moves around on
    def setMap(self,game_map):
        self.map = game_map
        self.location = g.current_location.getStart()
        return game_map

    def movement(self): 
        print(" - up\n" \
            " - down\n" \
            " - right\n" \
            " - left\n"
            " - back")
        direction = (input("Choice: "))
        #if choice is up player goes up by one space if allowed
        if direction == "up":
            #check if the first location of player is less than mini_row do this
            if self.location[0] > mini_row:
                #make that location go down by 1
                self.location[0] -= 1
                #print the players current locations name and description
                tempRoom = g.current_location.getMap()[self.location[0]][self.location[1]]
                print(tempRoom.name)
                print(tempRoom.description) 
            #if players first location is the same or less then max_row do this
            else:
                print("cant go that way twin")
                return
        #if choice is down player goes down by one space if allowed
        elif direction == "down":
            #check if the first location of player is less than max_row do this
            if self.location[0] < max_row:
                #make that location go up by 1
                self.location[0] += 1
                #print the players current locations name and description
                tempRoom = g.current_location.getMap()[self.location[0]][self.location[1]]
                print(tempRoom.name)
                print(tempRoom.description) 
            #if players first location is the same or more then max_row do this
            else:
                print("cant go that way twin")
                return
        #if choice is right player goes right by one space if allowed
        elif direction == "right":
            #check if the second location of player is less than max_colum do this
            if self.location[1] < max_column:
                #make that location go up by 1
                self.location[1] += 1
                #print the players current locations name and description
                tempRoom = g.current_location.getMap()[self.location[0]][self.location[1]]
                print(tempRoom.name)
                print(tempRoom.description) 
            #if players second location is the same or more then max_colum do this
            else:
                print("cant go that way twin")
                return
        #if choice is left player goes left by one space if allowed
        elif direction == "left":
            #check if the second location of player is greater than mini_column do this
            if self.location[1] > mini_column:
                #make that location go down by 1
                self.location[1] -= 1
                #print the players current locations name and description
                tempRoom = g.current_location.getMap()[self.location[0]][self.location[1]]
                print(tempRoom.name)
                print(tempRoom.description) 
            #if players second location is the same or less then mini_colum do this
            else:
                print("cant go that way twin")
                return
        #if choice is back player goes back to action in main code
        elif direction == "back":
            g.moving = False
        #if choice does not equal any of those do this 
        else:
            print("i have no clue what that means")

    #grabs every item from your bag and then calculate the score
    def calculate_score(self):
        self.divers_score = self.bag.evaluate_loot()
        print(f"Total value of your loot: {self.divers_score}")
        print(f"Current high score: {h.highScore}")
        #if the new score is bigger then old high score do this
        if self.divers_score > int(h.highScore):
            #make that score the new highsocre
            h.newHighScore(str(self.divers_score))
            print(f"New high score: {self.divers_score}")
        else:
            print("better luck next time.")
    #says what item you found and adds it to bag
    def keep(self, item):
        print(f"you found {item.name}")
        self.bag.add_to_inventory(item)
