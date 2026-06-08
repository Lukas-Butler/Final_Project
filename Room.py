class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __str__(self):
        return(self.name)
    
bolier = Room("Bolier", "description")
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

Engine_Room = [[engine,airlock,bolier,fule_tank,cooling_system,walk_way],
               [hyper_drive,salvage_compartment,walk_way,control_switch,vent],
               [engine,vent,walk_way,bolier,terminal,door],
               [hyper_drive,salvage_compartment,walk_way,vent,blueprint],
               [engine,airlock,bolier,fule_tank,cooling_system,walk_way]]