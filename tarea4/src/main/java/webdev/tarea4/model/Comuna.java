package webdev.tarea4.model;

import jakarta.persistence.*;

// Resumen de relaciones:
//    |comuna| 1 ———< N |aviso_adopcion|

@Entity
@Table(name = "comuna")
public class Comuna {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @Column(nullable = false)
    private String nombre;

    @OneToMany(mappedBy = "comuna", cascade = CascadeType.ALL)
    private java.util.List<AvisoAdopcion> avisos;

    // Getters y Setters
    public Integer getId() {
        return id;
    }
    public String getNombre() {
        return nombre;
    }
    public java.util.List<AvisoAdopcion> getAvisos() {
        return avisos;
    }

}
