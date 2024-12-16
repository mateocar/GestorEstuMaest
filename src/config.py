import os
from pathlib import Path
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv(".env", override=True)


class DefaultSettings(BaseSettings):
    ENV_STATE: str = "Default"  # env state es el nombre global de la configuracion
    BASE_DIR: Path = Path(
        __file__
    ).parent.parent  # se graba la ruta del directorio actual y devuelve la ruta
    SECRET_KEY: str = ""
    SQLALCHEMY_DATABASE_URL: str = "default"  # define Direccion base datos
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = (
        False  # se le da seguimientos a las modificaiones de la BD
    )
    SHOW_SQLALCHEMY_LOG_MESSAGES: bool = False  # Mensaje de inicio

    class Config:
        env_file = ".env"


class DevSettins(DefaultSettings):
    ENV_STATE: str = "Dev"
    DEBUG_MODE: bool = True
    SQLALCHEMY_ECHO: bool = True  # devuelve mensajes en general


class PndSettings(DefaultSettings):
    ENV_STATE: str = "Pnd"
    DEBUG_MODE: bool = False
    SQLALCHEMY_ECHO: bool = False


class TestSettings(DefaultSettings):
    ENV_STATE: str = "Test"
    DEBUG_MODE: bool = True
    SQLALCHEMY_ECHO: bool = True


def get_setting() -> BaseSettings:
    env_state = os.getenv("ENV_STATE", "Dev")
    if env_state == "Dev":
        return DevSettins()
    elif env_state == "Pnd":
        return PndSettings()
    elif env_state == "Test":
        return TestSettings()
