from fastapi import FastAPI
from .public.router import public
from .exception import registrer_error_handlers

app = FastAPI(
    title="Gestor Estudiantes Maestros",
    version="1.0",
    description="creacion de una api para la gestion de estudiantes y maestros"
)

registrer_error_handlers(app)

app.include_router(public) 
