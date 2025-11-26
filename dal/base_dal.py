from models.base import Base

def create_base(base_name:str,)->Base:
    base = Base(
        name=base_name,
        dorms=[],
        waiting_list=[]
    )
    return base