class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __str__(self):
        return(f"{self.name}")
    
bolier = ("Bolier", "description")
fule_tank = ("Fule Tank", "description")
engine_1 = ("Engine", "description")
engine_2 = ("Engine", "description")
hyper_drive = ("Hyper Drive", "description")
control_switch = ("Control Switch", ("description"))
blueprint = ("Blueprint", "description")
airlock = ("Airlock", "description")


Engine_Room = [[engine_1],
               [airlock,bolier],
               [engine_2],
               [],
               []]