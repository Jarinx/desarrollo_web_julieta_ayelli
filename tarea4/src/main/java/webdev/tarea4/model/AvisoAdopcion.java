package webdev.tarea4.model;

import jakarta.persistence.*;

import java.time.LocalDateTime;
import java.util.List;
import java.util.OptionalDouble;

// Resumen de relaciones:
//    |aviso_adopcion| 1 ———< N |nota|
//    |comuna| 1 ———< N |aviso_adopcion|

@Entity
@Table(name = "aviso_adopcion")
public class AvisoAdopcion {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @Column(nullable = false)
    private LocalDateTime fecha_ingreso;

    @Column(nullable = true)
    private String sector;

    @Column(nullable = false)
    private Integer cantidad;

    @Column(nullable = false)
    private String tipo;

    @Column(nullable = false)
    private Integer edad;

    @Column(nullable = false)
    private String unidad_medida;

    @ManyToOne
    @JoinColumn(name = "comuna_id", nullable = false)
    private Comuna comuna;

    @OneToMany(mappedBy = "aviso", cascade = CascadeType.ALL)
    private List<Nota> nota;

    // Getters y Setters
    public Integer getId() {
        return id;
    }
    public LocalDateTime getFecha_ingreso() {
        return fecha_ingreso;
    }
    public String getSector() {
        if (sector == null) {
            return "No proporcionado";
        }
        return sector;
    }
    public Integer getCantidad() {
        return cantidad;
    }
    public String getTipo() {
        if (cantidad == 1) {
            return tipo;
        } else {
            return tipo + "s";
        }
    }
    public Integer getEdad() {
        return edad;
    }
    public String getUnidad_medida() {
        if ("a".equals(unidad_medida)) {
            if (edad == 1) { return "año";} 
            else { return "años";}
        } else {
            if (edad == 1) { return "mes";}
            else { return "meses";}
        }
    }
    public Comuna getComuna() {
        return comuna;
    }
    public List<Nota> getNota() {
        return nota;
    }

    // Calcular la nota promedio
    @Transient
    public String getPromedioNota() {
        if (nota == null || nota.isEmpty()) {
            return "-";
        }
        
        OptionalDouble promedio = nota.stream()
                                      .mapToInt(Nota::getNota)
                                      .average();
                                      
        // format string con 1 decimal
        return promedio.isPresent() ? String.format("%.1f", promedio.getAsDouble()) : "-";
    }


}
