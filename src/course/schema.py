"""el esquema me permite adaptar como devolver el dato"""

from pydantic import BaseModel
from typing import List
from ..person.schemas import Student, Teacher


class Area(BaseModel):
    id: int
    area_name: str

    class Config:
        orm_mode: True


class OnlyArea(BaseModel):
    area_name: str

    class Config:
        orm_mode: True


class Response(BaseModel):
    message: str


class Course(BaseModel):
    id: int
    course_name: str
    area:  Area
    student: List[Student] = []
    teacher: Teacher