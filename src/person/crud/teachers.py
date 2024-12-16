from typing import Dict, List
from sqlalchemy.orm import Session
from ..models import Teacher
from ... import exception


def create_teacher(teacher_name: str, area: str, db: Session) -> Teacher:
    new_teacher = Teacher(name=teacher_name, area=area)
    db.add(new_teacher)
    db.commit()
    db.refresh(new_teacher)
    return new_teacher


def get_teachers(db: Session) -> List[Teacher]:
    return db.query(Teacher).all()


def update_teachers(id: int, teacher_name: str, area: str,
                    db: Session) -> Teacher:
    teacher_to_update = db.query(Teacher).filter(Teacher.id == id).first()
    if not teacher_to_update:
        raise exception.teacher_not_exist_handler(
            status_code=404, detail="El profesor no existe")
    teacher_to_update.name = teacher_name
    teacher_to_update.area = area
    db.commit()
    return teacher_to_update


def remove_teacher(id: int, db: Session) -> Dict[str, str]:
    removed_teacher = db.query(Teacher).filter(Teacher.id == id).first()
    if not removed_teacher:
        raise exception.teacher_not_exist_handler(
            status_code=404, detail="El profesor no existe")
    db.delete(removed_teacher)
    db.commit()
    return {"message": "Profesor eliminado con exito"}
