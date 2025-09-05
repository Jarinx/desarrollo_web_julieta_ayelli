// Lógica del formulario de adopción
// *Requiere reg-com.js*

/* (1) PRESENTACIÓN
/* --- REGIONES Y COMUNAS --- */
let regionSelect = document.getElementById('region');
let comunaSelect = document.getElementById('comuna');

function cargarRegiones() {
 getRegiones().forEach(region => {
     const option = document.createElement('option');
     option.value = region.id;
     option.textContent = region.nombre;
     regionSelect.appendChild(option);
 });
 regionSelect.addEventListener('change', () => {
     const regionId = regionSelect.value;
     const comunas = getComunas(regionId);
     comunaSelect.innerHTML = '<option value="">-- Selecciona comuna --</option>';
     // agregar comunas según región seleccionada
     comunas.forEach(comuna => {
         const option = document.createElement('option');
         option.value = comuna;
         option.textContent = comuna;
         comunaSelect.appendChild(option);
     });
     comunaSelect.disabled = false;
});
}

/* --- FECHA PREFILL --- */
let fechaInput = document.getElementById('fecha-entrega');

function prefillFecha() {
    const today = new Date();
    today.setMinutes(today.getMinutes() + 180);
    const pad = n => String(n).padStart(2, '0');
    const formattedDate = `${today.getFullYear()}-${pad(today.getMonth() + 1)}-${pad(today.getDate())}T${pad(today.getHours())}:${pad(today.getMinutes())}`;
    fechaInput.value = formattedDate;
    fechaInput.min = formattedDate;
}

/* --- CONTACTAR-POR CHECKBOXES --- */
function contactarMulti() {
    let contactarChecked = Array.from(document.querySelectorAll('input[type="checkbox"]:checked'));
    let contactarUnchecked = Array.from(document.querySelectorAll('input[type="checkbox"]:not(:checked)'));

    // validación: máximo 5 opciones
    if (contactarChecked.length > 5) {
        alert("Solo puedes colocar 5 opciones de contacto.");
        this.checked = false;
        return;
    }

    const wrap = document.getElementById('contactar-ids');
    // red unchecked => eliminar  
    contactarUnchecked.forEach(cb => {
        const value = cb.value;
        const id = `contactar-${value}`;
        const existingInput = document.getElementById(id);
        if (existingInput) {
            existingInput.parentElement.remove();
        }
    });
    // red checked => agregar
    contactarChecked.forEach(cb => {
        const red = cb.parentElement.textContent;
        const value = cb.value;
        const label = `${red} (ID o URL)`;
        const id = `contactar-${value}`;
        // solo agregar si no fue checked antes
        if (!document.getElementById(id)) {
            const div = document.createElement('div');
            div.innerHTML = `
                <label for="${id}">${label}:</label>
                <input type="text" id="${id}" name="${id}" minlength="4" maxlength="50">
            `;
            wrap.appendChild(div);
        }
    });
}

/* --- FOTOS --- */
function agregarFoto() {
    const wrap = document.querySelector('#fotos');
    const fotoCount = wrap.querySelectorAll('input[type="file"]').length;
    if (fotoCount >= 5) {
        alert("Solo puedes subir un máximo de 5 fotos.");
        return;
    }
    const input = document.createElement('input');
    input.type = 'file';
    input.name = `foto-${fotoCount + 1}`;
    wrap.appendChild(input);
}

/* (2) VALIDACIÓN */
function validarForm() {
    const errors = [];

    /* -- ¿DONDE? -- */
    let region = regionSelect.value;
    if (!region) errors.push("Debes seleccionar una región."); 
    let comuna = comunaSelect.value;
    if (!comuna) errors.push("Debes seleccionar una comuna.");
    let sector = document.getElementById('sector').value;
    if (sector.length > 100) errors.push("El sector no puede exceder 100 caracteres.");

    /* -- ¿CONTACTO? -- */
    let nombre = document.getElementById('nombre').value;
    if (nombre.length < 3 || nombre.length > 200) errors.push("El nombre debe tener entre 3 y 200 caracteres."); 
    let email = document.getElementById('email').value;
    if (!email) errors.push("Debes ingresar un email.");
    else {
        if (email.length > 100) errors.push("El email no puede exceder 100 caracteres.");
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // patrón básico de email
        if (!emailPattern.test(email)) errors.push("El email no tiene un formato válido.");
    }
    let celular = document.getElementById('celular').value;
    if (celular) {
        const celularPattern = /^\+\d{3}\.\d{8}$/; // +código-país.número
        if (!celularPattern.test(celular)) errors.push("El número de celular no tiene un formato válido.");
    }
    let contactarChecked = Array.from(document.querySelectorAll('input[type="checkbox"]:checked'));
    if (contactarChecked.length > 5) errors.push("Solo puedes seleccionar hasta 5 opciones de contacto.");
    contactarChecked.forEach(cb => {
        const value = (document.getElementById(`contactar-${cb.value}`)?.value || '').trim();
        if (value.length && (value.length < 4 || value.length > 50)) {
            errors.push(`El ID/URL para ${cb.parentElement.textContent} debe tener entre 4 y 50 caracteres.`);
        }
    });

    /* -- ¿MASCOTA? -- */
    let tipo = document.querySelectorAll('input[for="tipo-mascota"]:checked');
    if (!tipo) errors.push("Debes seleccionar un tipo de mascota.");
    let cantidad = document.getElementById('cantidad').value;
    if (!cantidad || isNaN(cantidad) || cantidad < 1) {
        errors.push("La cantidad de mascotas debe ser mínimo 1.");
    }
    let edad = document.getElementById('edad').value;
    if (!edad || isNaN(edad) || edad < 1) {
        errors.push("La edad debe ser mínimo 1");
    }
    let unidad = document.querySelectorAll('input[for="unidad-edad"]:checked');
    if (!unidad) errors.push("Debes seleccionar una unidad de edad.");
    let fechaEntrega = document.getElementById('fecha-entrega').value;
    if (!fechaEntrega) errors.push("Debes seleccionar una fecha y hora de entrega.");
    else {
        const fechaPattern = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}$/;
        if (!fechaPattern.test(fechaEntrega)) errors.push("La fecha debe tener el formato año-mes-día hora:minuto.");
        else {
            const prefill = document.getElementById('fecha-entrega').min;
            if (fechaEntrega < prefill) errors.push("La fecha de entrega debe ser mayor a la fecha actual + 3 horas.");
        }
    }
    let fotos = document.getElementById('fotos').querySelectorAll('input[type="file"]');
    if (fotos.length < 1 || fotos.length > 5) errors.push("Se debe adjuntar al menos 1 una foto (máximo 5).");
    
    return errors;
}

/* (3) MODAL CONFIRMACIÓN */
function openConfirm() {
    document.getElementById('modal-confirm').style.display = 'flex';
}
function closeConfirm() {
    document.getElementById('modal-confirm').style.display = 'none';
}

function submitForm() {
    const errors = validarForm();
    if (errors.length) {
        mostrarErrores(errors);
        return;
    }
    mostrarErrores([]); // limpiar errores previos
    openConfirm();
}

function confirmarEnvio() {
    closeConfirm();
    document.getElementById('form-adopcion').classList.add('hidden');
    document.querySelector('#msg-aviso-recibido').style.display = 'block';
    window.scrollTo({top: 0, behavior: 'smooth'});
}

function cancelarEnvio() {
    closeConfirm();
}

/* --- EVENT LISTENERS --- */
document.addEventListener('DOMContentLoaded', () => {
    cargarRegiones();
    prefillFecha();
    Array.from(document.querySelectorAll('input[type="checkbox"]')).forEach(cb => cb.addEventListener('change', contactarMulti));
    document.querySelector('#btn-agregar-foto').addEventListener('click', agregarFoto);
    document.getElementById('btn-enviar').addEventListener('click', submitForm);
    document.getElementById('btn-confirm-si').addEventListener('click', confirmarEnvio);
    document.getElementById('btn-confirm-no').addEventListener('click', cancelarEnvio);
    document.addEventListener('keydown', (e) => {
        if (e.key === "Escape") closeConfirm();
    });    
});

/* --- ERRORES --- */
function mostrarErrores(errors) {
    const box = document.querySelector('#error-box');
    const list = document.querySelector('#error-list');
    if (errors.length === 0) {
        box.style.display = 'none';
        list.innerHTML = "";
        return;
    }
    list.innerHTML = "";
    errors.forEach(e => {
        const li = document.createElement('li');
        li.textContent = e;
        list.appendChild(li);
    });
    box.style.display = 'block';
    window.scrollTo({top: 0, behavior: 'smooth'});
}
