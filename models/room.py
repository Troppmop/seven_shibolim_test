from pydantic import BaseModel

from models.soldier import Soldier

class Room(BaseModel):
    number: int
    #max 8 soldiers
    occupants: list