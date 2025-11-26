#import models for type checking
from models.base import Base
from models.soldier import Soldier

#import dal functions
from dal.soldier_dal import create_soldier
from dal.dorm_dal import create_dorm
from dal.room_dal import create_room

#set constants
MAX_ROOM_OCCUPANCY = 8

def place(base:Base, data:list)->Base:
    

    #generates and adds dorms to base
    dormA = create_dorm("A")
    dormB = create_dorm("B")
    base.dorms.append(dormA)
    base.dorms.append(dormB)

    #generates and attaches rooms to dorms
    for dorm_index in range(len(base.dorms)):
        for room_index in range(10):
            base.dorms[dorm_index].rooms.append(create_room(room_index))
    
    #adds soldiers from data to waiting list
    for line in data:
        base.waiting_list.append(create_soldier(line))
    
    #key function for list sorting method
    def sort_key(e: Soldier)->int:
        return e.distance_km

    #sort waiting list by distance
    base.waiting_list.sort(key=sort_key)

    #place soldiers based on need out of distance
    for dorm_i in range(len(base.dorms)):
        for room_i in range(len(base.dorms[dorm_i].rooms)):
            for bed_index in range(MAX_ROOM_OCCUPANCY):
                base.dorms[dorm_i].rooms[room_i].occupants.append(base.waiting_list.pop())
                base.dorms[dorm_i].rooms[room_i].occupants[-1].placement_status = 'placed'
    
    return base