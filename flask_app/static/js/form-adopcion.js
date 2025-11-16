const form = document.getElementById('form-adopcion');

/* (1) PRESENTACIÓN
/* --- REGIONES Y COMUNAS --- */
let regionSelect = document.getElementById('region');
let comunaSelect = document.getElementById('comuna');

function cargarRegCom() {
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
         option.value = comuna.id;
         option.textContent = comuna.nombre;
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
function crearInputIdentificador(val, labelText) {
  const id = `contactar-${val}`;                
  if (document.getElementById(id)) return;       // no duplicar

  // el input va junto al <label> que contiene el checkbox
  // buscamos el <label> padre del checkbox con ese value
  const cb = document.querySelector(`#contactar-por input[type="checkbox"][value="${val}"]`);
  if (!cb) return;
  const wrap = cb.parentElement;

  const inp = document.createElement('input');
  inp.type = 'text';
  inp.id = id;
  inp.name = id;                          
  inp.minLength = 4;
  inp.maxLength = 50;
  inp.placeholder = `${labelText} (ID o URL)`;
  wrap.appendChild(inp);
}

function eliminarInputIdentificador(val) {
  const id = `contactar-${val}`;                 
  const existing = document.getElementById(id);
  if (existing) existing.remove();
}

function contactarInit() {
  // Si algunos vienen marcados (por Jinja al volver de error), dibuja sus inputs:
  document.querySelectorAll('#contactar-por input[type="checkbox"]:checked')
    .forEach(cb => {
      const labelText = cb.parentElement.textContent.trim();
      crearInputIdentificador(cb.value, labelText);
    });
}

function contactarDelegadoChange(e) {
  const cont = document.getElementById('contactar-por');
  if (!cont) return;

  // Solo reaccionar a cambios en checkboxes internos
  const target = e.target;
  if (!(target && target.matches('input[type="checkbox"]'))) return;

  const max = parseInt(cont.dataset.max || '5', 10);
  const checked = cont.querySelectorAll('input[type="checkbox"]:checked');

  // Enforce máximo
  if (checked.length > max) {
    target.checked = false; // revertimos el último click
    alert(`Solo puedes seleccionar hasta ${max} opciones de contacto.`);
    return;
  }

  // Crear/eliminar input de identificador al lado
  const labelText = target.parentElement.textContent.trim();
  if (target.checked) {
    crearInputIdentificador(target.value, labelText);
  } else {
    eliminarInputIdentificador(target.value);
  }
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
    input.name = 'fotos';
    wrap.appendChild(input);
    actualizarBotonesEliminarFoto();
}

function eliminarFoto(index) {
    const wrap = document.querySelector('#fotos');
    const inputs = wrap.querySelectorAll('input[type="file"]');
    // Evitar eliminar si solo queda 1 input
    if (inputs.length <= 1) return;
    if (inputs[index]) {
        wrap.removeChild(inputs[index]);
    }
}

// Agrega un botón "Eliminar" junto a cada input de foto
function actualizarBotonesEliminarFoto() {
    const wrap = document.querySelector('#fotos');
    const inputs = wrap.querySelectorAll('input[type="file"]');
    // Elimina botones previos
    wrap.querySelectorAll('.btn-eliminar-foto').forEach(btn => btn.remove());
    inputs.forEach((input, idx) => {
        let btn = document.createElement('button');
        btn.type = 'button';
        btn.textContent = 'X';
        btn.className = 'btn-eliminar-foto';
        btn.style.marginRight = '8px';
        btn.addEventListener('click', () => {
            eliminarFoto(idx);
            actualizarBotonesEliminarFoto();
        });
        input.after(btn);
    });
}

/* (2) VALIDACIÓN (solo para ux) */
function validarForm() {
    const errors = [];

    /* -- ¿DONDE? -- */
    let region = regionSelect.value;
    if (!region) errors.push("Región: debes seleccionar una región."); 
    let comuna = comunaSelect.value;
    if (!comuna) errors.push("Comuna: debes seleccionar una comuna.");
    let sector = document.getElementById('sector').value;
    if (sector.length > 100) errors.push("Sector: el sector no puede exceder 100 caracteres.");

    /* -- ¿CONTACTO? -- */
    let nombre = document.getElementById('nombre').value;
    if (nombre.length < 3 || nombre.length > 200) errors.push("Nombre: el nombre debe tener entre 3 y 200 caracteres."); 
    let email = document.getElementById('email').value;
    if (!email) errors.push("Email: debes ingresar un email.");
    else {
        if (email.length > 100) errors.push("Email: el email no puede exceder 100 caracteres.");
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // patrón básico de email
        if (!emailPattern.test(email)) errors.push("Email: el email no tiene un formato válido.");
    }
    let celular = document.getElementById('celular').value;
    if (celular) {
        const celularPattern = /^\+\d{3}\.\d{8}$/; // +código-país.número
        if (!celularPattern.test(celular)) errors.push("Celular: el número de celular no tiene un formato válido.");
    }
    let contactarChecked = Array.from(document.querySelectorAll('input[type="checkbox"]:checked'));
    if (contactarChecked.length > 5) errors.push("Contactar por: solo puedes seleccionar hasta 5 opciones de contacto.");
    contactarChecked.forEach(cb => {
        const value = (document.getElementById(`contactar-${cb.value}`)?.value || '').trim();
        if (value.length && (value.length < 4 || value.length > 50)) {
            errors.push(`Contactar por: el ID/URL para ${cb.parentElement.textContent} debe tener entre 4 y 50 caracteres.`);
        }
    });

    /* -- ¿MASCOTA? -- */
    let tipo = document.querySelector('input[name="tipo-mascota"]:checked');
    if (!tipo) errors.push("Tipo: debes seleccionar un tipo de mascota.");
    let cantidad = document.getElementById('cantidad').value;
    if (!cantidad || isNaN(cantidad) || cantidad < 1) {
        errors.push("Cantidad: la cantidad de mascotas debe ser mínimo 1.");
    }
    let edad = document.getElementById('edad').value;
    if (!edad || isNaN(edad) || edad < 1) {
        errors.push("Edad: la edad debe ser mínimo 1.");
    }
    let unidad = document.querySelector('input[name="unidad-edad"]:checked');
    if (!unidad) errors.push("Unidad de edad: debes seleccionar una unidad de edad.");
    let fechaEntrega = document.getElementById('fecha-entrega').value;
    if (!fechaEntrega) errors.push("Fecha disponible para entrega: debes seleccionar una fecha y hora de entrega.");
    else {
        const fechaPattern = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}$/;
        if (!fechaPattern.test(fechaEntrega)) errors.push("Fecha disponible para entrega: la fecha debe tener el formato año-mes-día hora:minuto.");
        else {
            const prefill = document.getElementById('fecha-entrega').min;
            if (fechaEntrega < prefill) errors.push("Fecha disponible para entrega: la fecha de entrega debe ser mayor a la fecha actual + 3 horas.");
        }
    }
    let fotosInputs = document.getElementById('fotos').querySelectorAll('input[type="file"]');
    let fotosFiles = Array.from(fotosInputs).reduce((acc, input) => acc + (input.files.length > 0 ? 1 : 0), 0);
    if (fotosFiles < 1) errors.push("Fotos: se debe adjuntar al menos 1 foto.");
    if (fotosFiles > 5) errors.push("Fotos: solo se aceptan un máximo de 5 fotos.");
    
    return errors;
}

/* (3) MODAL CONFIRMACIÓN */
function openConfirm() {
    document.getElementById('modal-confirm').style.display = 'flex';
}
function closeConfirm() {
    document.getElementById('modal-confirm').style.display = 'none';
}
// botón "Agregar este aviso de adopción"
function onFormSubmit() {
    const errors = validarForm();
    if (errors.length) {
        mostrarErrores(errors);
        return;
    }
    mostrarErrores([]); // limpiar errores previos
    openConfirm();
}
// modal confirmación: botón "Sí, estoy seguro" (el submit real)
function confirmarEnvio() {
    closeConfirm();
    form.submit();
}
// modal confirmación: botón "No, no estoy seguro, quiero volver al formulario"
function cancelarEnvio() {
    closeConfirm();
}

/* --- EVENT LISTENERS --- */
document.addEventListener('DOMContentLoaded', () => {
    cargarRegCom();
    prefillFecha();
    actualizarBotonesEliminarFoto();
    // Contactar por:
     contactarInit();
    const cont = document.getElementById('contactar-por');
    if (cont) cont.addEventListener('change', contactarDelegadoChange);
    // Fotos:
    document.querySelector('#btn-agregar-foto').addEventListener('click', agregarFoto);
    // Botón "Agregar este aviso de adopción":
    form?.addEventListener('submit', onFormSubmit);
    // Modal confirmación:
    document.getElementById('btn-confirm-si').addEventListener('click', confirmarEnvio);
    document.getElementById('btn-confirm-no').addEventListener('click', cancelarEnvio);
    document.addEventListener('keydown', (e) => {
        if (e.key === "Escape") closeConfirm();
    });    
});

/* --- ERRORES (para ux) --- */
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
