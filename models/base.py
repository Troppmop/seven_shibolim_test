from pydantic import BaseModel

from dorm import Dorm
from soldier import Soldier

class Base(BaseModel):
    name: str
    dorms: list[Dorm]
    waiting_list: list[Soldier]
