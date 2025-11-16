**Branches 'Tarea n' (n = {1, 2...})**: para las tareas

# Consideraciones generales:
- En zonas donde se pedía tener el link a la portada al final de la página, lo cambié para que estuviera en el header, ya que se me hacía más intuitivo y visualmente estético.
- En el listado de avisos, hay paginación por botones y por input.
- Con respecto a las fotos: cada aviso al ser agregado crea una subcarpeta dentro de `static\uploads\avisos`, y ahí se van guardando las fotos correspondientes a cada aviso. Se guardan en tamaño original, y luego se adecúa el tamaño (según lo pedido en el enunciado) con CSS.
- Cambié el nombre de la base de datos de `tarea2` a `tarea4` para esta última tarea.

# Instrucciones para correr la aplicación:
Para correr la app correctamente, seguir en orden los pasos detallados a continuación.
### Ambiente (desde root del repo):
1. Crear venv: `python -m venv .venv`
2. Activar venv: `.\.venv\Scripts\activate`
3. Instalar dependencias: `pip install -r requirements.txt`

### Inicializar server
Si se empieza desde el server vacío (no está creada la db 'tarea4' y tampoco el user 'cc5002'), ejecutar en la terminal (yo lo hice en Windows PowerShell):

**1. Conectarse con user root:** `mysql -uroot -p`

**2. Crear user *cc5002*:**

```sql
CREATE USER 'cc5002'@'localhost' IDENTIFIED BY 'programacionweb';

GRANT ALL PRIVILEGES ON tarea4.* TO 'cc5002'@'localhost';

FLUSH PRIVILEGES; -- para guardar cambios

SHOW GRANTS FOR 'cc5002'@'localhost'; -- para verificar que 'cc5002' tiene los privilegios
```

**3. Salir:** `exit`

**4. Crear la db *tarea4* e insertar tablas adicionales:**

```powershell
# (1) Ejecutar dentro de carpeta 'flask_app\database':
cmd /c "mysql -ucc5002 -p < tarea4.sql" # ejecuta tarea4.sql

# (2) Ejecutar dentro de carpeta 'flask_app\database\helpers':
cmd /c "mysql -ucc5002 -p tarea4 --default-character-set=utf8mb4 < region-comuna.sql" # ejecuta region-comuna.sql

cmd /c "mysql -ucc5002 -p tarea4 --default-character-set=utf8mb4 < tabla-comentario.sql" # ejecuta tabla-comentario.sql

cmd /c "mysql -ucc5002 -p tarea4 --default-character-set=utf8mb4 < tabla-nota.sql" # ejecuta tabla-nota.sql
```

**5. Entrar a db *tarea4* con user *cc5002*:** `mysql -ucc5002 -p tarea4`

**6. Corregir datos:**

```sql
UPDATE comuna
SET nombre = "Lo Barnechea"
WHERE nombre = "Lo Barrenechea";
```

**7. Salir:** `exit`

**8. Cargar datos inventados:**

*En `data-invent.sql` hice 6 avisos con información inventada, para poder visualizar la app con datos ya ingresados.*

```powershell
# Ejecutar dentro de carpeta 'flask_app\database\helpers':
cmd /c "mysql -ucc5002 -p tarea4 --default-character-set=utf8mb4 < data-invent.sql" # ejecuta data-invent.sql
```

### Correr app:
Ejecutar en terminal dentro de `flask_app`: `flask run`

