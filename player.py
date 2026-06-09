class Player:
    def __init__(self, location, name, game_map):
        self.name = name
        self.location = location
        self.map = game_map

    def current_room(self):
        row, col = self.location
        room = self.map.Rooms[row][col]
        print("you are in {room}")
        print(room.description)

    def movement(self):
        print("which direction would you like to go:\n" \
              " - up\n" \
              " - down\n" \
              " - right\n" \
              " - left")
        direction = (input("Choice: "))
        row, col = self.location
        #up
        if direction == "up":
            if row > 0:
                row -= 1
            else:
                print("cant go that way twin")
                return
        #down
        elif direction == "down":
            if row < len(self.map.rooms) - 1:
                row += 1
            else:
                print("cant go that way twin")
                return
        #right
        elif direction == "right":
            if col < len(self.map.rooms[0]) - 1:
                col += 1
            else:
                print("cant go that way twin")
                return
        #left
        elif direction == "left":
            if col > 0:
                col -= 1
            else:
                print("cant go that way twin")
                return
        else:
            print("i have no clue what that means")
            
        self.location = [row, col]
        self.current_room()
        



