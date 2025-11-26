from models.soldier import Soldier

def create_soldier(row:list)->Soldier:
    soldier = Soldier(
        id=int(row[0]),
        first_name=row[1],
        last_name=row[2],
        gender=row[3],
        city=row[4],
        distance_km=int(row[5]),
        placement_status='not placed'
    )
    

    return soldier