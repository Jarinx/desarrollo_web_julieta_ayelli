import re
import filetype # type: ignore
from datetime import datetime, timedelta

EMAIL_REGEX = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")  # patrón básico
CEL_REGEX = re.compile(r"^\+\d{3}\.\d{8}$")  # +NNN.NNNNNNNN

def validate_region(value):
    if value and (value.isdigit() > 0):
        return True, ""
    return False, "Región: debes seleccionar una región."

def validate_comuna(value):
    if value and (value.isdigit() > 0):
        return True, ""
    return False, "Comuna: debes seleccionar una comuna."

def validate_sector(value): #opcional
    if not value:
        return True, ""
    elif len(value) <= 100:
        return True, ""
    return False, "Sector: el sector no puede exceder 100 caracteres."           

def validate_nombre(value):
    if value and (3 <= len(value)) and (len(value) <= 200):
        return True, ""
    return False, "Nombre: el nombre debe tener entre 3 y 200 caracteres."

def validate_email(value):
    if not (len(value) <= 100):
        return False, "Email: el email no puede exceder 100 caracteres."
    if not ("@" in value) or not (EMAIL_REGEX.match(value)):
        return False, "Email: el email no tiene un formato válido."
    return True, ""

def validate_celular(value): #opcional
    if not value:
        return True, ""
    elif not CEL_REGEX.match(value):
        return False, "Celular: el número de celular no tiene un formato válido."
    return True, ""

def validate_tipo(value):
    if value:
        return True, ""
    return False, "Tipo: debes seleccionar un tipo de mascota."
    
def validate_cantidad(value):
    if value and (value.isdigit() >= 1):
        return True, ""
    return False, "Cantidad: la cantidad de mascotas debe ser mínimo 1."

def validate_edad(value):
    if value and (value.isdigit() >= 1):
        return True, ""
    return False, "Edad: la edad debe ser mínimo 1."

def validate_unidad_medida(value):
    if value in ['a', 'm']:
        return True, ""
    return False, "Unidad de edad: debes seleccionar una unidad de edad."

def validate_fecha_entrega(value, now=None):
    if not value:
        return False, "Fecha disponible para entrega: debes colocar una fecha de entrega."
    dt = datetime.strptime(value, "%Y-%m-%dT%H:%M")
    delta = now + timedelta(minutes=180)
    if dt >=  delta:
        return True, ""
    return False, "Fecha disponible para entrega: la fecha de entrega debe ser mayor a la fecha actual + 3 horas."
        
def validate_contactar_por(nombre, identificadores): #opcional
    if (len(nombre) > 5):
        return False, "Contactar por: solo puedes seleccionar hasta 5 opciones de contacto."
    for i in identificadores.values():
       if len(i) < 4 or len(i) > 50:
           return False, f"Contactar por: el identificador debe tener entre 4 y 50 caracteres."
    return True, ""

def validate_fotos(files):
    if not files or (len(files) > 5) or (len(files) < 1):
        return False, "Fotos: debes adjuntar entre 1 y 5 imágenes."
    
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
    ALLOWED_MIMETYPES = {"image/jpeg", "image/png", "image/gif"}

    for foto in files:
        # check if a file was submitted
        if foto is None:
            return False, "Fotos: debes adjuntar entre 1 y 5 imágenes."
        # check if the browser submitted an empty file
        if foto.filename == "":
            return False, "Fotos: debes adjuntar entre 1 y 5 imágenes."
        # check file extension
        ftype_guess = filetype.guess(foto)
        if ftype_guess.extension not in ALLOWED_EXTENSIONS:
            return False, "Fotos: formato de archivo no permitido."
        # check mimetype
        if ftype_guess.mime not in ALLOWED_MIMETYPES:
            return False, "Fotos: formato de archivo no permitido."

    return True, ""

def validate_aviso(form_array):

    # ¿dónde?
    region = form_array[0]
    comuna = form_array[1]
    sector = form_array[2]

    # ¿contacto?
    nombre = form_array[3]
    email = form_array[4]
    celular = form_array[5]
    contactar_por_nombre = form_array[6][0]
    contactar_por_ids = form_array[6][1]

    # ¿mascota?
    tipo = form_array[7]
    cantidad = form_array[8]
    edad = form_array[9]
    unidad_medida = form_array[10]
    fecha_entrega = form_array[11]
    #descripcion = form_array[12]
    fotos = form_array[13]

    valids = [
        ["Región",validate_region(region)],
        ["Comuna",validate_comuna(comuna)],
        ["Sector",validate_sector(sector)],
        ["Nombre",validate_nombre(nombre)],
        ["Email",validate_email(email)],
        ["Celular",validate_celular(celular)],
        ["Contactar por",validate_contactar_por(contactar_por_nombre, contactar_por_ids)],
        ["Tipo",validate_tipo(tipo)],
        ["Cantidad",validate_cantidad(cantidad)],
        ["Edad",validate_edad(edad)],
        ["Unidad de edad",validate_unidad_medida(unidad_medida)],
        ["Fecha disponible para entrega",validate_fecha_entrega(fecha_entrega, now=datetime.now())],
        ["Fotos",validate_fotos(fotos)]
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