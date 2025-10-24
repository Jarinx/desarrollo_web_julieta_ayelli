// listado.js — toggle de vistas + modal de imagen

function mostrarDetalle() {
  document.getElementById("lista").classList.add("hidden");
  document.getElementById("detalle").classList.remove("hidden");
  window.scrollTo({ top: 0, behavior: "smooth" });
}

document.getElementById("volverListado")?.addEventListener("click", (e) => {
  e.preventDefault();
  document.getElementById("detalle").classList.add("hidden");
  document.getElementById("lista").classList.remove("hidden");
});

// ---- Modal ----
const modal     = document.getElementById("imgModal");
const imgGrande = document.getElementById("imgGrande");

function abrirModal(src) {
  imgGrande.src = src;
  modal.style.display = "flex";
}
function cerrarModal() {
  modal.style.display = "none";
  imgGrande.src = "";
}

// Miniaturas → abrir modal con SU MISMO src
document.getElementById("detFotos")?.addEventListener("click", (e) => {
  const thumb = e.target.closest(".foto-thumb");
  if (thumb) abrirModal(thumb.src);
});

// Botones/cierre
document.getElementById("cerrarModal")?.addEventListener("click", cerrarModal);
modal?.addEventListener("click", (e) => { if (e.target === modal) cerrarModal(); });
document.addEventListener("keydown", (e) => { if (e.key === "Escape") cerrarModal(); });

document.addEventListener('click', (e) => {
  const row = e.target.closest('tr.clickable');
  if (!row) return;
  const href = row.dataset.href;
  if (href) window.location = href;
});

  // Paginación con input
document.addEventListener('DOMContentLoaded', () => {
  const input = document.getElementById('input-ir-pagina');
  const btnIr = document.getElementById('btn-ir-pagina');
  const pagerNav = document.querySelector('nav.pager');

  if (!input || !btnIr || !pagerNav) return;

  // total_paginas viene del servidor, lo "inyectamos" en JS vía data-attr:
  const totalPaginas = '{{ total_paginas | int }}';
  const baseUrl = pagerNav.dataset.baseUrl; // ej: "/listado"

  btnIr.addEventListener('click', () => {
    let destino = parseInt(input.value, 10);

    // Validación básica en front:
    if (isNaN(destino)) return;
    if (destino < 1) destino = 1;
    if (destino > totalPaginas) destino = totalPaginas;

    // Navegar:
    // Construimos /listado?pag=N
    const url = `${baseUrl}?pag=${destino}`;
    window.location = url;
  });

  // UX: enter en el input también dispara el botón
  input.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') {
      e.preventDefault();
      btnIr.click();
    }
  });
});