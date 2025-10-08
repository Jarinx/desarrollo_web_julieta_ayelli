from models import Base
from db import engine

# Crea las tablas de la db

if __name__ == "__main__":
    Base.metadata.create_all(engine)