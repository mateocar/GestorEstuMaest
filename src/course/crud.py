''' aqui es el crud'''
from typing import List
from sqlalchemy.orm import Session
from . import models


def create_area(area_name: str, db: Session) -> models.Area:
    new_area = models.Area(area_name=area_name)
    db.add(new_area)
    db.commit()
    ## tener en cuenta que exite el metodo refresh pero no es obligatorio
    db.refresh(new_area)  
    return new_area

def get_areas(db: Session) ->List[models.Area]:
    return db.query(models.Area).all()
    
