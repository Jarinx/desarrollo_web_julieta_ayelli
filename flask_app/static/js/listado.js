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
