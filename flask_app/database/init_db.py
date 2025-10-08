from models import Base
from db import engine
import traceback

# Crea las tablas de la db

if __name__ == "__main__":
    try:
        Base.metadata.create_all(engine)
    except Exception as e:
        print("Error al crear las tablas:")
        traceback.print_exc()