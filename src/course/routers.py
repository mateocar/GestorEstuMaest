from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import  get_sessiondb
from . import crud, schema




course_router = APIRouter(tags=["course"])


@course_router.get("/areas", response_model = List[schema.Area])
def get_areas(db: Session = Depends(get_sessiondb)):
    areas = crud.get_areas(db)
    return areas
    
    
@course_router.get("/onlyareas", response_model= List[schema.OnlyArea])
def get_only_areas(db: Session = Depends(get_sessiondb)):
    only_areas = crud.get_areas(db)
    return only_areas

@course_router.post("/areas", response_model = schema.Area)
def create_area(area: schema.OnlyArea, db: Session = Depends(get_sessiondb)):
    print(area.area_name)
    db_area = crud.create_area(area_name = area.area_name, db = db)
    return db_area

@course_router.put("/area/{id}", response_model = schema.Area)
def update_area(id:int, area_name: str, db: Session = Depends(get_sessiondb)):
    updated_area = crud.update_area(id = id, area_name = area_name, db = db)
    return updated_area 

@course_router.delete("/area/{id}", response_model = schema.Response)
def delete_area(id: int, db: Session = Depends(get_sessiondb)):
    return crud.remove_area(id = id, db = db)