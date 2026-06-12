class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def  __str__(self):
        return(f"{self.name}")

# made an object for each engine room
boiler = Room("Boiler", "warms up the water")
fule_tank = Room("Fule Tank", "holds the luquids of the ship")
engine = Room("Engine", "makes ship move")
hyper_drive = Room("Hyper Drive", "makes ship move at light speed")
control_switch = Room("Control Switch", ("turns on all the expensive equipment"))
blueprint = Room("Blueprint", "tell the important poeple what the ship look like")
airlock = Room("Airlock", "place to go outside and die")
walk_way = Room("Walk Way", "were people walk across a brige")
salvage_compartment = Room("Salvage Compartment", "were you throw the scrap")
cooling_system = Room("Cooling System", "cools the engines down")
terminal = Room("Terminal", "big brother")
door = Room("Doors", "open it and go to living place")
vent = Room("Vents", "the imposter is sus")
#make an object for each living place
bed = Room("Bed","description")
kitchen = Room("Kitchen", "description")
locker = Room("Locker", "description")
med_bay = Room("Med Bay", "description")
table = Room("Table", "description")
shower = Room("Shower", "description")
cryo = Room("Cryo", "description")
life_support = Room("Life Support", "description")
science_lab = Room("Science Lab", "description")
stair = Room("Stair", "description")
elevator = Room("Elevator", "description")
#objects of each location in command center
office = Room("Office", "description")
computer = Room("Computer", "description")
navigation = Room("Nabigation", "description")
map_ = Room("Map", "description")
door = Room("Door", "description")
blank = Room("place holder", "description")

#making the rooms into a array
Engine_Room = [[engine,airlock,fule_tank,cooling_system,terminal],
               [hyper_drive,salvage_compartment,walk_way,control_switch,vent],
               [engine,vent,walk_way,boiler,door],
               [hyper_drive,salvage_compartment,walk_way,vent,blueprint],
               [engine,airlock,boiler,fule_tank,cooling_system,]]
living_place = [[blank,blank,blank,blank,blank],
                [blank,blank,blank,blank,blank],
                [stair,blank,blank,blank,elevator],
                [blank,blank,blank,blank,blank],
                [blank,blank,blank,blank,blank]]
command_center = [[blank,blank,blank,blank,blank],
                  [blank,blank,blank,blank,blank],
                  [door,blank,blank,blank,blank],
                  [blank,blank,blank,blank,blank],
                  [blank,blank,blank,blank,blank]]