@echo off
REM Activar venv
.\venv\Scripts\activate
echo -> Entorno virtual activado.

REM Inicializar servidor en db 'tarea2', crear user 'cc5002' con privilegios,
REM tablas region-comuna comlpetadas, y cargar datos inventados


REM Ejecutar servidor Flask
flask run
echo -> Servidor Flask iniciado.