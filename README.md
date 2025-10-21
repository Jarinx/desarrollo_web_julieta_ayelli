**Branches 'Tarea n' (n = {1, 2...})**: para las tareas

# Consideraciones generales:
- En zonas donde se pedía tener el link a la portada al final de la página, lo cambié para que estuviera en el header, ya que se me hacía más intuitivo y visualmente estético.

# Instrucciones generales:
Para correr la app correctamente, seguir en orden los pasos detallados a continuación.
### Ambiente (hacer lo siguiente desde root del repo):
1. Crear venv: `python -m venv .venv`
2. Activar venv: `.\.venv\Scripts\activate`
3. Instalar dependencias: `pip install -r requirements.txt`

### Inicializar server
Si se empieza desde el server vacío (no está creada la db 'tarea2' y tampoco el user 'cc5002'), ejecutar en la terminal (yo lo hice en Windows PowerShell):

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
Ejecutar en terminal: `.\run_app.bat`

