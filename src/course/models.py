from sqlalchemy import  Integer, Column, ForeignKey, String
from sqlalchemy.orm import relationship
from ..database import Base

class Area(Base):
    __tablename__ = "areas"
    id = Column(Integer, primary_key = True, autoincrement= True)
    area_name = Column(String(20))
    
    
class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer,primary_key = True, autoincrement= True)
    course_name = Column(String(20))
    area_id = Column(Integer, ForeignKey("areas.id"))
    studen_id = Column(Integer, ForeignKey("students.id"))
    teacher_id = Column(Integer, ForeignKey("teachers.id"))
    
    

    