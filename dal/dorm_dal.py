from models.dorm import Dorm

def create_dorm(dorm_name:str,)->Dorm:
    dorm = Dorm(
        name=dorm_name,
        rooms=[]
    )
    return dorm