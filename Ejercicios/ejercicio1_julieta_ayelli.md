# Ejercicio 1

**Nombre**: Julieta Ayelli

---

## Pregunta 1 (6 puntos)

# 1.1 (3 puntos)

Explique por qué el realizar validaciones del input del usuario en el front-end es una facilidad pero no una medida de seguridad.

**Respuesta**: Porque están pensadas en mejorar la experiencia del usuario, es decir, decirle a él si lo que colocó está bien o mal antes de enviarlo al servidor. Por ejemplo, resaltar un input obligatorio que no fue llenado. El problema es que, como están codificadas en el front-end, son facilmente manipulables por usuarios maliciosos, por lo que no proveen seguridad real para toda la app web.

# 1.2 (3 puntos)

Explique en detalle el rol de **HTML, CSS y JavaScript** en la creación del front-end de una aplicación web. Especifique la función de cada tecnología y cómo se combinan para construir una interfaz interactiva y visualmente atractiva.

**Respuesta:**

- HTML provee el “esqueleto” de la página, estructurándola en bloques de distintos tipos (contenedores, botones, formularios, etc) *—> HTML es el organizador*
- CSS permite detallar cómo queremos que se vea nuestra página, es decir, su diseño visual. Trabaja sobre HTML *—> CSS es el estilista*
- JS se usa para añadirle dinamismo a la página. Para poder funcionar, se debe obtener el DOM de la página *—> JS es el mago*

## Pregunta 2 (6 puntos)

A continuación, se presentan dos tareas prácticas:

1. **(3 puntos)** Implementar un código que reciba un nombre ingresado por el usuario y muestre un mensaje de bienvenida.
    - Si el usuario se llama **Julieta**, debe mostrarse un mensaje especial en negrita y en color azul.
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
const nombre = document.getElementById("nombre");
const btnEnviar = document.getElementById("btn-enviar");
const mensaje = document.getElementById("mensaje");

// Obtener elementos para el contador
const calificacionVisual = document.getElementById("calificacion");
const btnDisminuir = document.getElementById("btn-disminuir");
const btnAumentar = document.getElementById("btn-aumentar");

// Calificación inicial
let calificacionVar = 1;

// Función para mostrar mensaje de bienvenida
const mostrarMensaje = () => {
    const nombreInput = nombre.value.trim();
    if (nombreInput === ""){ //si el usuario no ingresa su nombre
        mensaje.textContent = "Debe ingresar un nombre.";
        mensaje.style.color = "red";
        mensaje.style.fontWeight = "normal";
    }
    else if (nombreInput.toLowerCase() === "Julieta".toLowerCase()){
        mensaje.innerHTML = '<strong style="color:blue;">¡Bienvenida, ${nombreInput}!</strong>'
    }
    else {
        mensaje.textContent = '¡Hola, ${nombreInput}!';
        mensaje.style.color = "black";
        mensaje.style.fontWeight = "normal";
    }
};

// Función para aumentar la calificación
const aumentarCalificacion = () => {
    if (calificacionVar < 7){
        calificacionVar++;
        calificacionVisual.textContent = calificacionVar;
    }
};

// Función para disminuir la calificación
const disminuirCalificacion = () => {
    if (calificacionVar > 1){
        calificacionVar--;
        calificacionVisual.textContent = calificacionVar;
    }
};

// Asignar eventos
btnEnviar.addEventListener("click", mostrarMensaje);
btnAumentar.addEventListener("click", aumentarCalificacion);
btnDisminuir.addEventListener("click", disminuirCalificacion);

```