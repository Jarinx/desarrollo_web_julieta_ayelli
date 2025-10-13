import re
import filetype # type: ignore
from datetime import datetime, timedelta

EMAIL_REGEX = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")  # patrón básico
CEL_REGEX = re.compile(r"^\+\d{3}\.\d{8}$")  # +NNN.NNNNNNNN

def validate_region(value):
    return value and value.isdigit() > 0

def validate_comuna(value):
    return value and value.isdigit() > 0

def validate_sector(value): #opcional
    if not value:
        return True
    return len(value) <= 100

def validate_nombre(value):
    return value and 3 <= len(value) <= 200

def validate_email(value):
    return "@" in value and len(value) <= 100 and EMAIL_REGEX.match(value)

def validate_celular(value): #opcional
    if not value:
        return True
    return CEL_REGEX.match(value)

def validate_tipo(value):
    if value:
        return True
    
def validate_cantidad(value):
    return value and value.isdigit() > 1

def validate_edad(value):
    return value and value.isdigit() > 1

def validate_unidad_medida(value):
    return value in ['a', 'm']

def validate_fecha_entrega(value, now=None):
    if not value:
        return False
    dt = datetime.strptime(value, "%Y-%m-%dT%H:%M")
    return dt >= now + timedelta(hours=3)
        
def validate_contactar_por(checked): #opcional
    if (len(checked) > 5):
        return False
    # for c in checked:
    #    if len(c.value) < 4 or len(c.value) > 50:
    #        return False
    return True

def validate_fotos(files):
    if not files or len(files) > 5 or len(files) < 1:
        return False
    
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
    ALLOWED_MIMETYPES = {"image/jpeg", "image/png", "image/gif"}

    for foto in files:
        # check file extension
        ftype_guess = filetype.guess(foto)
        if ftype_guess.extension not in ALLOWED_EXTENSIONS:
            return False
        # check mimetype
        if ftype_guess.mime not in ALLOWED_MIMETYPES:
            return False

    return True

def validate_form(form_array):

    # ¿dónde?
    region = form_array[0]
    comuna = form_array[1]
    # sector = form_array[2]

    # ¿contacto?
    nombre = form_array[3]
    email = form_array[4]
    celular = form_array[5]
    contactar_por = form_array[6]

    # ¿mascota?
    tipo = form_array[7]
    cantidad = form_array[8]
    edad = form_array[9]
    unidad_medida = form_array[10]
    fecha_entrega = form_array[11]
    # descripcion = form_array[12]
    #fotos = form_array[13]

    valids = [
        f"Region: {validate_region(region)}",
        f"Comuna: {validate_comuna(comuna)}",
        f"Nombre: {validate_nombre(nombre)}",
        f"Email: {validate_email(email)}",
        f"Celular: {validate_celular(celular)}",
        #validate_contactar_por(contactar_por),
        f"Tipo: {validate_tipo(tipo)}",
        f"Cantidad: {validate_cantidad(cantidad)}",
        f"Edad: {validate_edad(edad)}",
        f"Unidad de medida: {validate_unidad_medida(unidad_medida)}",
        f"Fecha de entrega: {validate_fecha_entrega(fecha_entrega, now=datetime.now())}"
        #validate_fotos(fotos)
    ]

    for v in valids:
        if not v:
            print("Validation failed:", v)
            return False
    return True