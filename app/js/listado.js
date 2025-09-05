/* listado.js — render de tabla, detalle y modal de fotos */

// Datos de ejemplo (5 filas). Ajusta rutas a tu carpeta ../images/
const AVISOS = [
  {
    id: 1,
    fechaPublicacion: "2025-09-03 10:30",
    fechaEntrega: "2025-09-06 12:00",
    comuna: "Providencia",
    sector: "Parque Bustamante",
    cantidad: 7, tipo: "perros", edad: 1, unidadEdad: "meses",
    contacto: { nombre: "María López", email: "maria@example.com" },
    fotos: ["../images/cachorros.jpg","../images/puppy-pasto.jpg","../images/american-bullys.jpg"]
  },
  {
    id: 2,
    fechaPublicacion: "2025-09-02 17:00",
    fechaEntrega: "2025-09-05 09:30",
    comuna: "Providencia",
    sector: "Cenco Costanera",
    cantidad: 3, tipo: "perros", edad: 4, unidadEdad: "años",
    contacto: { nombre: "Juan Pérez", email: "juan@example.com" },
    fotos: ["../images/american-bullys.jpg"]
  },
  {
    id: 3,
    fechaPublicacion: "2025-09-02 15:45",
    fechaEntrega: "2025-09-04 18:00",
    comuna: "Las Condes",
    sector: "Escuela Militar",
    cantidad: 1, tipo: "gato", edad: 3, unidadEdad: "meses",
    contacto: { nombre: "Carla Díaz", email: "carla@example.com" },
    fotos: ["../images/kitten.jpg","../images/gato-dormido.jpg"]
  },
  {
    id: 4,
    fechaPublicacion: "2025-09-02 11:11",
    fechaEntrega: "2025-09-07 11:00",
    comuna: "Las Condes",
    sector: "Mallplaza Los Dominicos",
    cantidad: 1, tipo: "gato", edad: 3, unidadEdad: "años",
    contacto: { nombre: "Luis Soto", email: "luis@example.com" },
    fotos: ["../images/gato-dormido.jpg"]
  },
  {
    id: 5,
    fechaPublicacion: "2025-08-31 19:20",
    fechaEntrega: "2025-09-03 16:00",
    comuna: "Lo Barnechea",
    sector: "Santuario Del Valle",
    cantidad: 1, tipo: "perro", edad: 2, unidadEdad: "meses",
    contacto: { nombre: "Ana Rivas", email: "ana@example.com" },
    fotos: ["../images/puppy-pasto.jpg"]
  }
];

const $ = s => document.querySelector(s);
const $$ = s => Array.from(document.querySelectorAll(s));

/* ------ Render tabla ------ */
function renderTabla() {
  const tbody = $("#tablaAvisos tbody");
  tbody.innerHTML = "";
  AVISOS.forEach(a => {
    const tr = document.createElement("tr");
    tr.dataset.id = a.id;
    tr.innerHTML = `
      <td>${a.fechaPublicacion}</td>
      <td>${a.fechaEntrega}</td>
      <td>${a.comuna}</td>
      <td>${a.sector}</td>
      <td>${a.cantidad} ${a.tipo} / ${a.edad} ${a.unidadEdad}</td>
      <td>${a.contacto.nombre}</td>
      <td>${a.fotos.length}</td>
    `;
    tr.addEventListener("click", () => mostrarDetalle(a.id));
    tbody.appendChild(tr);
  });
}

/* ------ Detalle ------ */
function mostrarDetalle(id) {
  const a = AVISOS.find(x => x.id === id);
  if (!a) return;

  $("#detTitulo").textContent = `Detalle — ${a.cantidad} ${a.tipo} en ${a.comuna}`;
  const info = $("#detInfo");
  info.innerHTML = `
    <li><strong>Fecha publicación:</strong> ${a.fechaPublicacion}</li>
    <li><strong>Fecha entrega:</strong> ${a.fechaEntrega}</li>
    <li><strong>Comuna:</strong> ${a.comuna}</li>
    <li><strong>Sector:</strong> ${a.sector}</li>
    <li><strong>Mascotas:</strong> ${a.cantidad} ${a.tipo}</li>
    <li><strong>Edad:</strong> ${a.edad} ${a.unidadEdad}</li>
    <li><strong>Total fotos:</strong> ${a.fotos.length}</li>
  `;

  const contacto = $("#detContacto");
  contacto.innerHTML = `
    <li><strong>Nombre:</strong> ${a.contacto.nombre}</li>
    <li><strong>Email:</strong> ${a.contacto.email}</li>
  `;

  const fotos = $("#detFotos");
  fotos.innerHTML = "";
  a.fotos.forEach((src, i) => {
    const img = document.createElement("img");
    img.src = src;
    img.alt = `Foto ${i+1} de ${a.tipo}`;
    img.width = 320; img.height = 240; // 320×240 como exige el enunciado
    img.addEventListener("click", () => abrirModal(src));
    fotos.appendChild(img);
  });

  $("#lista").classList.add("hidden");
  $("#detalle").classList.remove("hidden");
}

/* ------ Volver al listado ------ */
$("#volverListado").addEventListener("click", (e) => {
  e.preventDefault();
  $("#detalle").classList.add("hidden");
  $("#lista").classList.remove("hidden");
  window.scrollTo({ top: 0, behavior: "smooth" });
});

/* ------ Modal imagen 800×600 ------ */
function abrirModal(src) {
  const modal = $("#imgModal");
  const img = $("#imgGrande");
  img.src = src;
  modal.style.display = "flex";
}
function cerrarModal() {
  $("#imgModal").style.display = "none";
  $("#imgGrande").src = "";
}
$("#cerrarModal").addEventListener("click", cerrarModal);
document.addEventListener("keydown", (e)=>{ if(e.key === "Escape") cerrarModal(); });
$("#imgModal").addEventListener("click", (e)=>{ if(e.target.id === "imgModal") cerrarModal(); });

/* ------ Init ------ */
document.addEventListener("DOMContentLoaded", renderTabla);
