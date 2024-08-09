''' aqui es el crud'''
from typing import List, Dict
from fastapi import HTTPException
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
    
def update_area(id: int, area_name: str, db:Session)->models.Area:
    area_to_update = db.query(models.Area).filter(models.Area.id == id).first()# no es necesario el models.Area.id en el filtro solo poner id=id
    if not area_to_update:
        raise HTTPException(status_code = 404, detail = "nose encuentra el area")
    area_to_update.area_name = area_name
    db.commit()
    return area_to_update

def remove_area(id: int, db:Session) -> Dict[str, str]: #la flecha indica que es lo que devuelve la funcion 
    removed_area = db.query(models.Area).filter(models.Area.id == id).first()
    if not removed_area:
        raise HTTPException(status_code = 404, detail = "nose encuentra el area")
    db.delete(removed_area)
    db.commit()
    return {"message": "Area eliminada con exito"}


    