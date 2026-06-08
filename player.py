import map as m
import Room as r
import global_variables as g
max_row = 4
mini_row = 0
mini_column = 0
max_column = 4



class Player:
    def __init__(self, name, game_map):
        self.location =  Engine_Room.getStart()
        self.name = name
        self.map = game_map

    def setMap(self,grid):
        self.map = grid
        self.location = Engine_Room.getStart()
        return grid


    def movement(self):
        print("which direction would you like to go:\n" \
              " - up\n" \
              " - down\n" \
              " - right\n" \
              " - left\n"
              " - back")
        direction = (input("Choice: "))
        #up
        if direction == "up":
            if self.location[0] > mini_row:
                    self.location[0] -= 1
                    tempRoom = Engine_Room.getMap()[self.location[0]][self.location[1]]
                    print(tempRoom.name)
                    print(tempRoom.description) 
            else:
                print("cant go that way twin")
                return
        #down
        elif direction == "down":
            if self.location[0] < max_row:
                self.location[0] += 1
                tempRoom = Engine_Room.getMap()[self.location[0]][self.location[1]]
                print(tempRoom.name)
                print(tempRoom.description) 
            else:
                print("cant go that way twin")
                return
        #right
        elif direction == "right":
            if self.location[1] < max_column:
                self.location[1] += 1
                tempRoom = Engine_Room.getMap()[self.location[0]][self.location[1]]
                print(tempRoom.name)
                print(tempRoom.description) 
            else:
                print("cant go that way twin")
                return
        #left
        elif direction == "left":
            if self.location[1] > mini_column:
                self.location[1] -= 1
                tempRoom = Engine_Room.getMap()[self.location[0]][self.location[1]]
                print(tempRoom.name)
                print(tempRoom.description) 
            else:
                print("cant go that way twin")
                return
        #goes back to action in main
        elif direction == "back":
            g.moving = False

        else:
            print("i have no clue what that means")

Engine_Room = m.map("Engine_Room",[0,0], r.Engine_Room)        



