<<<<<<< HEAD
=======

>>>>>>> 394006d4271bb84867f0d4f54a57ad60fe889e3b
import map as m
import Room as r
import global_variables as g
max_row = 4
mini_row = 0
mini_column = 0
max_column = 4
<<<<<<< HEAD

=======
>>>>>>> 394006d4271bb84867f0d4f54a57ad60fe889e3b
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
<<<<<<< HEAD
            if self.location[0] > mini_row:
                self.location[0] -= 1
                tempRoom = Engine_Room.getMap()[self.location[0]][self.location[1]]
                print(tempRoom[0])
                print(tempRoom[1])
=======
            if row > 0:
                row -= 1
>>>>>>> 394006d4271bb84867f0d4f54a57ad60fe889e3b
            else:
                print("cant go that way twin")
                return
        #down
        elif direction == "down":
<<<<<<< HEAD
            if self.location[0] < max_row:
                self.location[0] += 1
                tempRoom = Engine_Room.getMap()[self.location[0]][self.location[1]]
                print(tempRoom[0])
                print(tempRoom[1])
=======
            if row < len(self.map[0]) - 1:
                row += 1
>>>>>>> 394006d4271bb84867f0d4f54a57ad60fe889e3b
            else:
                print("cant go that way twin")
                return
        #right
        elif direction == "right":
<<<<<<< HEAD
            if self.location[1] < max_column:
                self.location[1] += 1
                tempRoom = Engine_Room.getMap()[self.location[0]][self.location[1]]
                print(tempRoom[0])
                print(tempRoom[1])
=======
            if col < len(self.map[0]) - 1:
                col += 1
>>>>>>> 394006d4271bb84867f0d4f54a57ad60fe889e3b
            else:
                print("cant go that way twin")
                return
        #left
        elif direction == "left":
            if self.location[1] > mini_column:
                self.location[1] -= 1
                tempRoom = Engine_Room.getMap()[self.location[0]][self.location[1]]
                print(tempRoom[0])
                print(tempRoom[1])
            else:
                print("cant go that way twin")
                return
        #goes back to action in main
        elif direction == "back":
            g.moving = False
        else:
            print("i have no clue what that means")
<<<<<<< HEAD
Engine_Room = m.map("Engine_Room",[0,0], r.Engine_Room)        

=======
>>>>>>> 394006d4271bb84867f0d4f54a57ad60fe889e3b



