from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_sessiondb
from .schemas import Student, OnlyStudent, Teacher, OnlyTeacher, Response
from .crud import students, teachers

person_router = APIRouter(tags=["persons"])


@person_router.post("/students", response_model=Student)
def create_student(student: OnlyStudent, db: Session = Depends(get_sessiondb)):
    print(student.student_name)
    db_student = students.create_student(
        student_name=student.student_name, age=student.age, db=db
    )
    return db_student


@person_router.get("/students", response_model=List[Student])
def get_students(db: Session = Depends(get_sessiondb)):
    studens = students.get_students(db)
    return studens


@person_router.get("/onlystudent", response_model=List[OnlyStudent])
def get_only_students(db: Session = Depends(get_sessiondb)):
    only_students = students.get_students(db)
    return only_students


@person_router.put("/student/{id}", response_model=Student)
def update_student(
    id: int, student_name: str, age: int, db: Session = Depends(get_sessiondb)
):
    updated_student = students.update_students(
        id=id, student_name=student_name, age=age, db=db
    )
    return updated_student


@person_router.delete("/student/{id}", response_model=Response)
def delete_student(id: int, db: Session = Depends(get_sessiondb)):
    return students.remove_student(id=id, db=db)


## rutas de profesores o teachers


@person_router.get("/teachers", response_model=List[Teacher])
def get_teachers(db: Session = Depends(get_sessiondb)):
    teacherss = teachers.get_teachers(db)
    return teacherss


@person_router.get("/onlyteachers", response_model=List[OnlyTeacher])
def get_only_teachers(db: Session = Depends(get_sessiondb)):
    only_teachers = teachers.get_teachers(db)
    return only_teachers


@person_router.post("/teachers", response_model=Teacher)
def create_teacher(teacher: OnlyTeacher, db: Session = Depends(get_sessiondb)):
    db_teacher = teachers.create_teacher(
        teacher_name=teacher.name, area=teacher.area, db=db
    )  # asi debe quedar la forma de los parametros cuando la liena supera mas de 80 caracteres
    return db_teacher


@person_router.put("/teacher/{id}", response_model=Teacher)
def update_teacher(
    id: int, teacher_name: str, area: str, db: Session = Depends(get_sessiondb)
):
    updated_teacher = teachers.update_teachers(
        id=id, teacher_name=teacher_name, area=area, db=db
    )
    return updated_teacher


@person_router.delete("/teacher/{id}", response_model=Response)
def remove_teacher(id: int, db: Session = Depends(get_sessiondb)):
    return teachers.remove_teacher(id=id, db=db)
