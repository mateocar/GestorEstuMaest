from typing import List, Dict
from sqlalchemy.orm import Session
from ..models import Student
from ... import exception

def create_student(student_name: str, age:int, db: Session)->Student:
    new_student = Student(name = student_name, age = age)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

def get_students(db: Session)->List[Student]:
    return db.query(Student).all()

def update_students(id: int,student_name: str, age: str, db: Session)->Student:
    student_to_update = db.query(Student).filter(Student.id == id).first()
    if not student_to_update:
        raise exception.studen_not_exist_handler(status_code = 404, detail = "El estudiante no existe")
    student_to_update.name = student_name
    student_to_update.age = age
    db.commit()
    return student_to_update

def remove_student(id: int, db: Session)->Dict[str, str]:
    removed_student = db.query(Student).filter(Student.id == id).first()
    if not removed_student:
        raise exception.studen_not_exist_handler(status_code = 404, detail ="El estudiante no existe")
    db.delete(removed_student)
    db.commit()
    return {"message": "Estudiante eliminado con exito"}
    


