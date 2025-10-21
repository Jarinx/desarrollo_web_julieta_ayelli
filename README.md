**Branches 'Tarea n' (n = {1, 2...})**: para las tareas

**Consideraciones Tarea 1:**
- En zonas donde se pedía tener el link a la portada al final de la página, lo cambié para que estuviera en el header, ya que se me hacía más intuitivo y visualmente estético.
- Con respecto a los CSS: tengo el `theme.css`, donde separé todas las características generales de la aplicación para mantener coherencia entre las páginas. Luego, para cada CSS específico, puse reglas específicas a esa página.
- No hay Javascript para *portada* ni *estadísticas*, ya que no fue necesario.
- Los colores quedaron un poco oscuros, pero esto se corregirá para la próxima iteración.

## Consideraciones Tarea 2:
### Ambiente:
1. Instalar dependencias (desde root del repo): `pip install -r requirements.txt`
2. Actualizar dependencias: `pip freeze > requirements.txt`

### Inicializar server
Si se empieza desde el server vacío (no está creada la db 'tarea2' y tampoco el user 'cc5002'), ejecutar en la terminal de PowerShell en el siguiente orden:

**1. Conectarse con user root:** `mysql -uroot -p`

**2. Crear user *cc5002*:**

```sql
CREATE USER 'cc5002'@'localhost' IDENTIFIED BY 'programacionweb';

GRANT ALL PRIVILEGES ON tarea2.* TO 'cc5002'@'localhost';

FLUSH PRIVILEGES; -- para guardar cambios

SHOW GRANTS FOR 'cc5002'@'localhost'; -- para verificar que 'cc5002' tiene los privilegios
```

**3. Salir:** `exit`

**4. Crear la db *tarea2*:**

```powershell
cmd /c "mysql -ucc5002 -p < tarea2.sql" # ejecuta tarea2.sql

cmd /c "mysql -ucc5002 -p tarea2 --default-character-set=utf8mb4 < region-comuna.sql" # ejecuta region-comuna.sql

cmd /c "mysql -ucc5002 -p tarea2 --default-character-set=utf8mb4 < data-invent.sql" # ejecuta data-invent.sql
```

**5. Entrar a db *tarea2* con user *cc5002*:** `mysql -ucc5002 -p tarea2`

**6. Corregir datos:**

```sql
UPDATE comuna
SET nombre = "Lo Barnechea"
WHERE nombre = "Lo Barrenechea";
```

**7. Salir:** `exit`

### Correr app:
Ejecutar en terminal de PowerShell (desde root del repo): `.\run_app.bat`

