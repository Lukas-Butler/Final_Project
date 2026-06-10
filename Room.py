class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __str__(self):
<<<<<<< HEAD
        return(f"{self.name}")


bolier = ("Bolier", "description")
fule_tank = ("Fule Tank", "description")
engine = ("Engine", "description")
hyper_drive = ("Hyper Drive", "description")
control_switch = ("Control Switch", ("description"))
blueprint = ("Blueprint", "description")
airlock = ("Airlock", "description")
walk_way =("Walk Way", "description")
salvage_compartment = ("Salvage Compartment", "description")
cooling_system =("Cooling System", "description")
terminal = ("Terminal", "description")
door = ("Doors", "description")
vent = ("Vents", "description")
#make an object for each living place
bed = ("Bed","description")
kitchen = ("Kitchen", "description")
locker = ("Locker", "description")
med_bay = ("Med Bay", "description")
table = ("Table", "description")
shower = ("Shower", "description")
cryo = ("Cryo", "description")
life_support = ("Life Support", "description")
science_lab = ("Science Lab", "description")
stair = ("Stair", "description")
elevator = ("Elevator", "description")
#objects of each location in command center
office = ("Office", "description")
computer = ("Computer", "description")
navigation = ("Nabigation", "description")
map_ = ("Map", "description")
door = ("Door", "description")

=======
        return(self.name)
    
    
# made an object for each engine room
bolier = ("Bolier", "description")
fule_tank = ("Fule Tank", "description")
engine = ("Engine", "description")
hyper_drive = ("Hyper Drive", "description")
control_switch = ("Control Switch", ("description"))
blueprint = ("Blueprint", "description")
airlock = ("Airlock", "description")
walk_way =("Walk Way", "description")
salvage_compartment = ("Salvage Compartment", "description")
cooling_system =("Cooling System", "description")
terminal = ("Terminal", "description")
door = ("Doors", "description")
vent = ("Vents", "description")
#make an object for each living place
bed = ("Bed","description")
kitchen = ("Kitchen", "description")
locker = ("Locker", "description")
med_bay = ("Med Bay", "description")
table = ("Table", "description")
shower = ("Shower", "description")
cryo = ("Cryo", "description")
life_support = ("Life Support", "description")
science_lab = ("Science Lab", "description")
stair = ("Stair", "description")
elevator = ("Elevator", "description")
#objects of each location in command center
office = ("Office", "description")
computer = ("Computer", "description")
navigation = ("Nabigation", "description")
map_ = ("Map", "description")
door = ("Door", "description")

>>>>>>> 394006d4271bb84867f0d4f54a57ad60fe889e3b
#making the rooms into a array
Engine_Room = [[engine,airlock,bolier,fule_tank,cooling_system,door],
               [hyper_drive,salvage_compartment,walk_way,control_switch,vent],
               [engine,vent,walk_way,bolier,terminal,door],
               [hyper_drive,salvage_compartment,walk_way,vent,blueprint],
               [engine,airlock,bolier,fule_tank,cooling_system,walk_way]]
living_place = []
command_center = []

<<<<<<< HEAD

=======
>>>>>>> 394006d4271bb84867f0d4f54a57ad60fe889e3b
