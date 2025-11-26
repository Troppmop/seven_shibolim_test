from models.room import Room

def create_room(room_number:int)->Room:
    room = Room(
        number=room_number,
        occupants=[]
    )
    return room
