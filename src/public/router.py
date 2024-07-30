'''
En este archivo se deben definir los endpoints y esto va con sus respectivas rutas URL
'''
from fastapi import APIRouter

public = APIRouter()


@public.get("/app", tags=["public"])
def saludar():
    return "hola mundo"
