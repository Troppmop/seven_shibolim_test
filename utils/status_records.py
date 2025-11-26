from models.base import Base
from models.soldier import Soldier

def get_soldier_record(base:Base)-> list[dict]:
    soldier_records = []

    #add waiting soldiers to the records
    for soldier in base.waiting_list:
        record = {
            'soldier_name':soldier.first_name + " " + soldier.last_name,
            'status':soldier.placement_status,
            'note': 'soldier is on the waiting list' 
        }
        soldier_records.append(record)

    #add placed soldiers to the records
    for dorm in base.dorms:
        for room in dorm.rooms:
            for soldier in room.occupants:
                record = {
                    'soldier_name':soldier.first_name + " " + soldier.last_name,
                    'status':soldier.placement_status,
                    'dorm': dorm.name,
                    'room': room.number
                }
                soldier_records.append(record)

    return soldier_records