class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __str__(self):
        return(self.name)
    
# made an object for each room
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

#making the rooms into a array
Engine_Room = [[engine,airlock,bolier,fule_tank,cooling_system,door],
               [hyper_drive,salvage_compartment,walk_way,control_switch,vent],
               [engine,vent,walk_way,bolier,terminal,door],
               [hyper_drive,salvage_compartment,walk_way,vent,blueprint],
               [engine,airlock,bolier,fule_tank,cooling_system,walk_way]]