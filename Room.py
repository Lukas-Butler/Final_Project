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
bed = Room("Bed","were people sleep")
kitchen = Room("Kitchen", "were you make a potato, fries, french fries, hashbrowns, mashed potatos")
locker = Room("Locker", "were you put your phone to not be addicted")
med_bay = Room("Med Bay", "were the sick get better")
table = Room("Table", "were you end frendships playing monopoly")
shower = Room("Shower", "were you clean your smelly self")
cryo = Room("Cryo", "were you go to bed for a long time")
life_support = Room("Life Support", "you dont want to be here this is were you die")
science_lab = Room("Science Lab", "were you figure out what that weird create you brought along lives")
workout_room = Room("Workout Room", "were you get ripped")
living_room = Room("Living Room", "were you hangout with friends")
stair = Room("Stair", "you enter engine room")
elevator = Room("Elevator", "you enter command center")

#objects of each location in command center
office = Room("Office", "were the important people go to talk about business")
computer = Room("Computer", "were you check to make sure the ship is going the right way")
navigation = Room("Nabigation", "tells you which planet your going to")
map_ = Room("Map", "shows the whole blueprints of the ship")
door = Room("Door", "brought you to living place")
cabin_light = Room("Cabin Lights", "makes it so you can see")
red_button = Room("Red Button", "if you push it the ship goes boom")
chair = Room("Chair"," were the navigator's seat")
switch = Room("Switch", "turns on the power")
vending_machine =Room("Vending Machine","were people go to fill up")

#making the rooms into a array
Engine_Room = [[engine,airlock,fule_tank,cooling_system,terminal],
               [hyper_drive,salvage_compartment,walk_way,control_switch,vent],
               [engine,vent,walk_way,boiler,door],
               [hyper_drive,salvage_compartment,walk_way,vent,blueprint],
               [engine,airlock,boiler,fule_tank,cooling_system,]]

living_place = [[science_lab,kitchen,med_bay,life_support,cryo],
                [shower,workout_room,locker,table,kitchen],
                [stair,bed,living_room,bed,elevator],
                [table,bed,kitchen,workout_room,shower],
                [locker,science_lab,med_bay,life_support,cryo]]

command_center = [[vending_machine,office,computer,navigation,switch],
                  [computer,cabin_light,switch,map_,red_button],
                  [door,chair,office,vending_machine,computer],
                  [switch,computer,cabin_light,vending_machine,map_],
                  [office,chair,cabin_light,computer,navigation]]