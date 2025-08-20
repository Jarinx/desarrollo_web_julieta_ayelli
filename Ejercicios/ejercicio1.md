# Ejercicio 1

**Nombre**: [tu nombre va aqui]

---

## Pregunta 1 (6 puntos)

# 1.1 (3 puntos)
Explique por que el realizar validaciones del input del usuario en el front-end es una facilidad pero no una medida de seguridad. 

**Respuesta**:

# 1.2 (3 puntos)
Explique en detalle el rol de **HTML, CSS y JavaScript** en la creación del front-end de una aplicación web. Especifique la función de cada tecnología y cómo se combinan para construir una interfaz interactiva y visualmente atractiva.

**Respuesta:**:



## Pregunta 2 (6 puntos)
A continuación, se presentan dos tareas prácticas:  

1. **(3 puntos)** Implementar un código que reciba un nombre ingresado por el usuario y muestre un mensaje de bienvenida.  
   - Si el usuario se llama **[Tu Nombre]**, debe mostrarse un mensaje especial en negrita y en color azul.  
   - El contenido debe actualizarse sin recargar la página.  

2. **(3 puntos)** Implementar un contador de calificación con dos botones para aumentar y disminuir la nota actual.  
   - La calificación debe tener valores apropiados.  
   - La calificación debe actualizarse sin recargar la página.  

### Código HTML:
```html
<div>
    <h3>Parte 1: Mensaje de Bienvenida</h3>
    <label for="nombre">Ingrese su nombre:</label>
    <input type="text" id="nombre">
    <button type="button" id="btn-enviar">Enviar</button>
    <p id="mensaje"></p>
</div>

<hr>

<div>
    <h3>Parte 2: Contador de Calificación</h3>
    <p>Nota actual: <span id="calificacion">1</span></p>
    <button type="button" id="btn-disminuir">Disminuir</button>
    <button type="button" id="btn-aumentar">Aumentar</button>
</div>
```

Implemente un sistema para modificar la nota actual, utilizando la plantilla disponible más abajo, y programe únicamente donde se le indica. Se espera que tras apretar un botón, la nota se actualice sin la necesidad de recargar la página. No está permitido modificar el HTML.

**Respuesta**:
```js
// Obtener elementos para el mensaje de bienvenida


// Obtener elementos para el contador


// Calificación inicial

// Función para mostrar mensaje de bienvenida
const mostrarMensaje = () => {

};

// Función para aumentar la calificación
const aumentarCalificacion = () => {

};

// Función para disminuir la calificación
const disminuirCalificacion = () => {

};

// Asignar eventos

```
