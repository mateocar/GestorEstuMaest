from sqlalchemy import Integer, Column, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database import Base
from ..person.models import Student, Teacher


class Area(Base):
    __tablename__ = "areas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    area_name = Column(String(20))
    description = Column(String(150))


class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, autoincrement=True)
    course_name = Column(String(20))
    area_id = Column(Integer, ForeignKey("areas.id"))
    teacher_id = Column(Integer, ForeignKey("teachers.id"))

    area = relationship("Area", back_populates="courses")#bacK_populates me indica la table madre por la cual se ingresa a la otra tabal para llenar datos 
    # course_student = relationship("course_students", back_populates="courses") NOTE
    student = relationship(
        Student, back_populates="courses", secondary="course_students"
    )
    # las relaciones de muchos a muchos  son para no poner las ids de las tablas
    teacher = relationship(Teacher, back_populates="courses")


class CourseStudents(Base):
    __tablename__ = "course_students"
    id = Column(Integer, primary_key=True, autoincrement=True)
    studen_id = Column(Integer, ForeignKey("students.id"))
    course_id = Column(Integer, ForeignKey("courses.id"))
    enrollment_date = Column(DateTime, default=datetime.now)

    student = relationship(Student, back_populates="course_students")
    course = relationship(Course, back_populates="course_students")
