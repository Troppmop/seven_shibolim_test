from pydantic import BaseModel

from models.dorm import Dorm
from models.soldier import Soldier

class Base(BaseModel):
    name: str
    dorms: list[Dorm]
    #all soldiers are automatically to be added to waiting list
    #then they will be sorted to dorms
    waiting_list: list[Soldier]
