package webdev.tarea4.model;

import jakarta.persistence.*;
import jakarta.validation.constraints.Max;
import jakarta.validation.constraints.Min;

// Resumen de relaciones:
//    |aviso_adopcion| 1 ———< N |nota|

@Entity
@Table(name = "nota")
public class Nota {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @ManyToOne
    @JoinColumn(name = "aviso_id", nullable = false) 
    private AvisoAdopcion aviso;

    @Min(1) // nota mínima 1
    @Max(7) // nota máxima 7
    @Column(nullable = false)
    private Integer nota;

    // Getters y Setters
    public Integer getId() {
        return id;
    }
    public Integer getNota() {
        return nota;
    }
    public Integer getAvisoId() {
        return aviso.getId();
    }
    public void setNota(Integer nota) {
        this.nota = nota;
    }
    public void setAviso(AvisoAdopcion aviso) {
        this.aviso = aviso;
    }

    
}
