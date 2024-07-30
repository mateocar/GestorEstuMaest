from fastapi import FastAPI
from .public.router import public

app = FastAPI(
    title="Gestor Estudiantes Maestros",
    version="1.0",
    description="creacion de una api para la gestion de estudiantes y maestros"
)

app.include_router(public)
