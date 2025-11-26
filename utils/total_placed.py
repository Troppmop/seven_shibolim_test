from models.base import Base

def get_total(base: Base)->int:
    total = 0

    for dorm in base.dorms:
        for room in dorm.rooms:
            total += len(room.occupants)

    return total