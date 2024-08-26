from pydantic import BaseModel, Field


class Student(BaseModel):
    id: int
    student_name: str = Field(alias="name")
    age: int

    class Config:
        orm_mode: True


class OnlyStudent(BaseModel):
    student_name: str
    age: int

    class Config:
        orm_mode: True


class Teacher(BaseModel):
    id: int
    name: str
    area: str

    class Config:
        orm_mode: True


class OnlyTeacher(BaseModel):
    name: str
    area: str

    class Config:
        orm_mode: True


class Response(BaseModel):
    message: str
