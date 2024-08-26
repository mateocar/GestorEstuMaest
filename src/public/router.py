"""
En este archivo se deben definir los endpoints y esto va con sus respectivas rutas URL
"""

from fastapi import APIRouter
from ..exception import StudenNotExist

public = APIRouter()


@public.get("/error", tags=["public"])
def example_error():
    raise StudenNotExist()


@public.get("/app", tags=["public"])
def saludar():
    return "hola mundo"
