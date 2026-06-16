#importants map and room code
import map as m
import Room as r
import random 
import item as i
import player as p
count = 0
#makes a class of each different map and 
Engine_Room = m.map("Engine_Room",[0,0], r.Engine_Room)
living_place = m.map("Living Place",[0,0],r.living_place)
command_center = m.map("Command Center",[0,0],r.command_center)
#make a player class as barbara
#variables
moving = True
playing = True
current_location = Engine_Room
