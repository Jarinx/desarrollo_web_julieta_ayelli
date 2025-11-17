// Event listener general
document.addEventListener("DOMContentLoaded", () => {
  
  const modal = document.getElementById("modal-evaluacion");
  const btnCerrarModal = document.getElementById("btn-cerrar-modal");
  const btnConfirmarNota = document.getElementById("btn-confirmar-nota");
  const notasContainer = document.getElementById("notas-container");
  const botonesNota = notasContainer.querySelectorAll(".btn-nota");

  // Variables globales
  let notaSeleccionada = null;
  let avisoIdActual = null;

  // --- 1. MODAL ---
  const botonesEvaluar = document.querySelectorAll(".btn.evaluar");

  botonesEvaluar.forEach(boton => {
    boton.addEventListener("click", () => {
      avisoIdActual = boton.dataset.avisoId;
      
      // reset estado anterior
      notaSeleccionada = null;
      botonesNota.forEach(btn => btn.classList.remove("selected"));
      
      modal.style.display = "flex";
    });
  });

  // Event listener para los botones de nota
  notasContainer.addEventListener("click", (e) => {
    const botonClickeado = e.target.closest(".btn-nota");
    
    if (!botonClickeado) return;

    // quitar style 'selected' de todos los botones
    botonesNota.forEach(btn => btn.classList.remove("selected"));
    
    // poner style 'selected' solo al clickeado
    botonClickeado.classList.add("selected");
    
    notaSeleccionada = parseInt(botonClickeado.dataset.nota, 10);
  });

  // Event listener para "Agregar Nota"
  btnConfirmarNota.addEventListener("click", () => {
    if (notaSeleccionada === null) {
      alert("Debes seleccionar una nota del 1 al 7.");
      return;
    }
    
    // llamar a la API
    llamarApiParaEvaluar(avisoIdActual, notaSeleccionada);
    
    cerrarModal();
  });

  // Cerrar modal
  function cerrarModal() {
    modal.style.display = "none";
    notaSeleccionada = null;
    avisoIdActual = null;
  }
  btnCerrarModal.addEventListener("click", cerrarModal);
  modal.addEventListener("click", (e) => {
    if (e.target === modal) {
      cerrarModal();
    }
  });

  // --- 2. Función asíncrona con fetch---
  async function llamarApiParaEvaluar(avisoId, nota) {
    try {
      const respuesta = await fetch(`/api/avisos/${avisoId}/evaluar`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ nota: nota }),
      });

      if (!respuesta.ok) {
        const errorTexto = await respuesta.text();
        throw new Error(`Error del servidor: ${errorTexto}`);
      }

      const data = await respuesta.json();

      const celdaNota = document.getElementById(`nota-aviso-${avisoId}`);
      if (celdaNota) {
        celdaNota.textContent = data.nuevoPromedio;
      }

    } catch (error) {
      console.error("Error en el fetch:", error);
      alert(`No se pudo guardar la nota: ${error.message}`);
    }
  }
});