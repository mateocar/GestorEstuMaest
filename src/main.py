from fastapi import FastAPI
from .exception import registrer_error_handlers
from .database import Base, engine
from .course import models as courses_models
from .person import models as persons_models
from .public.router import public
from .course.router import course_router

app = FastAPI(
    title="Gestor Estudiantes Maestros",
    version="1.0",
    description="creacion de una api para la gestion de estudiantes y maestros"
)


Base.metadata.create_all( bind = engine)

registrer_error_handlers(app)

app.include_router(public) 
app.include_router(course_router)
