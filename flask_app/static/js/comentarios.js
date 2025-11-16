// Elementos de la sección de comentarios
const listaComentarios = document.getElementById("lista-comentarios");
const sinComentariosMsg = document.getElementById("sin-comentarios");
const formComentario = document.getElementById("form-comentario");
const errorBox = document.getElementById("comentario-error");
const errorGlobalBox = document.getElementById("comentarios-error-global");

// helper para crear listado de comentarios
function listarComentarios(c) {
  const li = document.createElement("li");
  li.classList.add("comentario-item");
  li.innerHTML = `
    <p><i>Fecha: ${c.fecha}</i></p>
    <p><strong>${c.nombre}: </strong>${c.texto}</p>`;
  return li;
}

// cargar comentarios existentes
async function cargarComentarios() {
    try {
        const resp = await fetch(`/api/aviso/${AVISO_ID}/comentarios`);
        if (!resp.ok) {
            throw new Error("Respuesta no OK del servidor");
        }

        const data = await resp.json();
        const comentarios = data.comentarios || [];

        // resets
        listaComentarios.innerHTML = "";
        errorGlobalBox.style.display = "none";
        errorGlobalBox.textContent = "";

        if (comentarios.length === 0) {
            sinComentariosMsg.style.display = "block";
            return;
        }
        else {
            sinComentariosMsg.style.display = "none";
        }

        comentarios.forEach(c => {
            listaComentarios.appendChild(listarComentarios(c));
        });
    }
    catch (err) {
        console.error("Error al cargar comentarios:", err);

        errorGlobalBox.textContent =
        "No pudimos cargar los comentarios en este momento. Por favor recargue la página.";
        errorGlobalBox.style.display = "block";
    }
}

formComentario.addEventListener("submit", async (e) => {
  e.preventDefault();
  errorBox.style.display = "none";
  errorBox.textContent = "";

  const nombre = formComentario.nombre.value.trim();
  const texto = formComentario.texto.value.trim();

  // POST al server
  const resp = await fetch(`/api/aviso/${AVISO_ID}/comentarios`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: `{"nombre": "${nombre}", "texto": "${texto}"}`
  });

  const data = await resp.json();

  // falla validación del backend
  if (!resp.ok) {
    errorBox.style.display = "block";
    errorBox.textContent = "Por favor, corrija el error en: ";
    data.errores.forEach(err => {
        const list = document.createElement("ul");
        list.innerHTML = `<li>${err}</li>`;
        errorBox.appendChild(list);
    });
    return;
  }

  const nuevo = data.comentario;
  listaComentarios.prepend(listarComentarios(nuevo));
  sinComentariosMsg.style.display = "none";

  formComentario.reset();
});

cargarComentarios();