from pydantic import BaseModel

from soldier import Soldier

class Room(BaseModel):
    number: int
    #max 8 soldiers
    occupants: list[Soldier]