// Lógica del formulario de adopción
// *Requiere reg-com.js*

/* --- Regiones y comunas --- */
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

/* --- Fecha prefill --- */
let fechaInput = document.getElementById('fecha-entrega');

function prefillFecha() {
    const today = new Date();
    today.setMinutes(today.getMinutes() + 180);
    const pad = n => String(n).padStart(2, '0');
    const formattedDate = `${today.getFullYear()}-${pad(today.getMonth() + 1)}-${pad(today.getDate())}T${pad(today.getHours())}:${pad(today.getMinutes())}`;
    fechaInput.value = formattedDate;
    fechaInput.min = formattedDate;
}

/* --- Contactar-por checkboxes --- */


function contactarMulti() {
    let contactarChecked = Array.from(document.querySelectorAll('input[type="checkbox"]:checked'));
    let contactarUnchecked = Array.from(document.querySelectorAll('input[type="checkbox"]:not(:checked)'));

    if (contactarChecked.length > 5) {
        alert("Máximo 5 opciones de contacto");
        this.checked = false;
        return;
    }
    const wrap = document.getElementById('contactar-ids');

    // Eliminar campos correspondientes a checkboxes desmarcados
    contactarUnchecked.forEach(cb => {
        const value = cb.parentElement.textContent;
        const id = `contactar-${value}`;
        const existingInput = document.getElementById(id);
        if (existingInput) {
            existingInput.parentElement.remove();
        }
    });

    // Agregar campos solo si no existen ya
    contactarChecked.forEach(cb => {
        const value = cb.parentElement.textContent;
        const label = `${value} (ID o URL)`;
        const id = `contactar-${value}`;

        // Verificar si el campo ya existe
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

/* --- Inicializar --- */
document.addEventListener('DOMContentLoaded', () => {
    cargarRegiones();
    prefillFecha();
    
});
Array.from(document.querySelectorAll('input[type="checkbox"]')).forEach(cb => cb.addEventListener('change', contactarMulti));
