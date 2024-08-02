from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import get_setting


settings = get_setting()

engine = create_engine(settings.SQLACHEMY_DATABASE_URL)

SessioLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

Base = declarative_base()

def get_sessiondb(): # creacion funcion generadora de bases de datos o sesion 
    db = SessioLocal()
    try:
        yield db
    finally:
        db.close()