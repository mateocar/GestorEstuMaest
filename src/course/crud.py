''' aqui es el crud'''
from sqlalchemy.orm import Session
from . import models


def create_area(area_name: str, db: Session) -> models.Area:
    new_area = models.Area(area_name=area_name)
    db.session.add(new_area)
    db.session.commit()
    ## tener en cuenta que exite el metodo refresh pero no es obligatorio
    db.refresh(new_area)  
    return new_area
