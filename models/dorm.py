from pydantic import BaseModel

from room import Room

class Dorm(BaseModel):
    name: str
    #max 10 rooms
    rooms: list[Room]