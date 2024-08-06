'''el esquema me permite adaptar como devolver el dato '''
from pydantic import BaseModel


class Area(BaseModel):
    id: int
    area_name: str
    class Config:
        orm_mode: True
    
class OnlyArea(BaseModel):
    area_name: str
    class Config:
        orm_mode: True
        

    

    