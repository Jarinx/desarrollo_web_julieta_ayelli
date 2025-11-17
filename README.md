**Branches 'Tarea n' (n = {1, 2...})**: para las tareas

# Consideraciones generales Tarea 4:
- Cambié el nombre de la base de datos de `tarea2` a `tarea4` para esta última tarea.
- Junté los archivos `tarea4.sql`, `tabla-comentario.sql` y `tabla-nota.sql` en un solo archivo llamado `schema.sql`, y junté `region-comuna.sql` y `data-invent.sql` (datos que yo inventé) en un solo archivo llamado `data.sql`. Estos dos archivos conjuntos están en la carpeta `tarea4/src/main/resources`.
- En la carpeta `tarea4/src/main/java/webdev/tarea4/controller` está el controlador `EvaluacionController.java`, que implementa la ruta `/evaluaciones` para mostrar el listado de avisos para evaluar, y `/api/avisos/{id}/evaluar` para agregar las notas. 

# Ejecución Tarea 4:
1. Ir a carpeta: `tarea4/src/main/java/webdev/tarea4`
2. Ejecutar la clase `Tarea4Application.java` como aplicación Java.
3. Abrir el navegador en la URL: `http://localhost:8080/evaluaciones` para ver el listado de avisos a evaluar.