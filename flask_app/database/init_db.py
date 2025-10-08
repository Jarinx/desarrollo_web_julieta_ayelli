from models import Base
from db import engine, insert_reg_com
import traceback
import argparse

# Crea las tablas de la db

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--insert-sql", help="Ruta a region-comuna.sql")
    parser.add_argument("--force", action="store_true", help="Vacía y recarga region/comuna")
    args = parser.parse_args()

    try:
        Base.metadata.create_all(engine)
        if args.insert_sql:
            insert_reg_com(args.insert_sql, force=args.force)
    except Exception as e:
        print("Error al crear las tablas:")
        traceback.print_exc()