@echo off
REM Activar venv
.\venv\Scripts\activate
echo -> Entorno virtual activado.

REM init db
python database/init_db.py
echo -> Base de datos inicializada.

REM Ejecutar servidor Flask
flask run
echo -> Servidor Flask iniciado.