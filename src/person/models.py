from sqlalchemy import Integer, Column, String
from ..database import Base



class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), index=True)
    age = Column(Integer)


class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))
    area = Column(String(15))
