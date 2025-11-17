package webdev.tarea4.controller;

import webdev.tarea4.model.*;
import webdev.tarea4.repository.*;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;
import java.util.Optional;

@Controller
public class EvaluacionController {
    @Autowired
    private AvisoAdopcionRepository avisoRepo;

    @Autowired
    private NotaRepository notaRepo;

    // Ruta listado evaluaciones de avisos de adopción
    @GetMapping("/evaluaciones")
    public String mostrarEvaluaciones(Model model) {
        List<AvisoAdopcion> avisos = avisoRepo.findAll(); 
        
        model.addAttribute("avisos", avisos); // pasar lista de avisos al template
        
        return "evaluacion"; // buscar en 'resources/templates/evaluacion.html'
    }

    // API REST para agregar nota
    @PostMapping("/api/avisos/{id}/evaluar")
    @ResponseBody
    public ResponseEntity<?> agregarNota(@PathVariable("id") Integer avisoId, 
                                         @RequestBody Map<String, Integer> payload) {
        Optional<AvisoAdopcion> avisoOpt = avisoRepo.findById(avisoId);
        if (!avisoOpt.isPresent()) {
            return ResponseEntity.notFound().build(); // error 404 si no existe el aviso
        }

        Integer valorNota = payload.get("nota");
        if (valorNota == null || valorNota < 1 || valorNota > 7) {
            return ResponseEntity.badRequest().body("Nota debe ser un entero entre 1 y 7.");
        }

        AvisoAdopcion aviso = avisoOpt.get();

        Nota nuevaNota = new Nota();
        nuevaNota.setNota(valorNota);
        nuevaNota.setAviso(aviso);
        notaRepo.save(nuevaNota);

        AvisoAdopcion avisoUpdate = avisoRepo.findById(avisoId).get();
        String nuevoPromedio = avisoUpdate.getPromedioNota();

        return ResponseEntity.ok(Map.of("nuevoPromedio", nuevoPromedio));
    }
}
