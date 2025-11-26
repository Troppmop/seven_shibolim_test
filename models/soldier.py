from pydantic import BaseModel
from typing import Literal

class Soldier(BaseModel):
    id: int
    first_name: str
    last_name: str
    gender: Literal['male','female']
    distance_km: int
    placement_status: Literal['placed', 'not placed']
