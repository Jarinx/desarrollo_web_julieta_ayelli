**Branches 'Tarea n' (n = {1, 2...})**: para las tareas

**Consideraciones Tarea 1:**
- En zonas donde se pedía tener el link a la portada al final de la página, lo cambié para que estuviera en el header, ya que se me hacía más intuitivo y visualmente estético.
- Con respecto a los CSS: tengo el `theme.css`, donde separé todas las características generales de la aplicación para mantener coherencia entre las páginas. Luego, para cada CSS específico, puse reglas específicas a esa página.
- No hay Javascript para *portada* ni *estadísticas*, ya que no fue necesario.
- Los colores quedaron un poco oscuros, pero esto se corregirá para la próxima iteración.

## Consideraciones Tarea 2:
Si se empieza desde el server vacío (no está creada la db 'tarea2' y tampoco el user 'cc5002'), ejecutar en PowerShell, en el siguiente orden:

```bash
# --- CONECTARSE CON ROOT ---
$ mysql -uroot -p

# --- USER ---
$ CREATE USER 'cc5002'@'localhost' IDENTIFIED BY 'programacionweb';

$ GRANT ALL PRIVILEGES ON tarea2.* TO 'cc5002'@'localhost';

$ FLUSH PRIVILEGES; # para guardar cambios

$ SHOW GRANTS FOR 'cc5002'@'localhost'; # Para verificar que 'cc5002' tiene los privilegios

$ exit

# --- DB ---
$ cmd /c "mysql -ucc5002 -p < tarea2.sql"

$ cmd /c "mysql -ucc5002 -p tarea2 --default-character-set=utf8mb4 < region-comuna.sql" 

$ mysql -ucc5002 -p tarea2

# ya dentro de la db, ejecutar la query:
UPDATE comuna
SET nombre = "Lo Barnechea"
WHERE nombre = "Lo Barrenechea";
```

**Para correr la app con 1 solo comando (estando dentro de carpeta 'flask_app'):**
```bash
.\run_app.bat
``` 