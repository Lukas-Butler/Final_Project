class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def  __str__(self):
        return(f"{self.name}")

# made an object for each engine room
boiler = Room("Boiler", "description")
fule_tank = Room("Fule Tank", "description")
engine = Room("Engine", "description")
hyper_drive = Room("Hyper Drive", "description")
control_switch = Room("Control Switch", ("description"))
blueprint = Room("Blueprint", "description")
airlock = Room("Airlock", "description")
walk_way = Room("Walk Way", "description")
salvage_compartment = Room("Salvage Compartment", "description")
cooling_system = Room("Cooling System", "description")
terminal = Room("Terminal", "description")
door = Room("Doors", "description")
vent = Room("Vents", "description")
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