def validate_nombre(value):
    if value and (3 <= len(value)) and (len(value) <= 80):
        return True, ""
    return False, "Nombre: el nombre debe tener entre 3 y 80 caracteres."

def validate_texto(value):
    if value and (5 <= len(value)):
        return True, ""
    return False, "Texto: el texto debe tener mínimo 5 caracteres."

def validate_comentario(form_array):
    nombre = form_array[0]
    texto = form_array[1]

    valids = [
        ["nombre", validate_nombre(nombre)],
        ["texto", validate_texto(texto)],
    ]

    errores = []
    for v in valids:
        status, msg = v[1] 
        if not status:
            errores.append(msg)
    
    if len(errores) == 0:
        return True, []
    else:
        return False, errores