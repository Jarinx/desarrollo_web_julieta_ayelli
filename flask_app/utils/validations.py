import re
import filetype
from datetime import datetime, timedelta

EMAIL_REGEX = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")  # patrón básico
CEL_REGEX = re.compile(r"^\+\d{3}\.\d{8}$")  # +NNN.NNNNNNNN

def validate_region(value):
    return value and value > "0"

def validate_comuna(value):
    return value and value > "0"    

def validate_sector(value):
    if not value:
        return True
    return len(value) <= 100

def validate_nombre(value):
    return value and 3 <= len(value) <= 200

def validate_email(value):
    return "@" in value and len(value) <= 100 and EMAIL_REGEX.match(value)

def validate_celular(value):
    return value and CEL_REGEX.match(value)

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
        
def validate_contactar_por(checked, value):
    if (len(checked) > 5):
        return False
    
    for s in checked:
        if len(value) < 4 or len(value) > 50:
            return False
        
    return True

def validate_fotos(files):
    if not files or len(files) > 5 or len(files) < 1:
        return False
    
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}
    ALLOWED_MIMETYPES = {"image/jpeg", "image/png"}

    for foto in files:
        # check file extension
        ftype_guess = filetype.guess(foto)
        if ftype_guess.extension not in ALLOWED_EXTENSIONS:
            return False
        # check mimetype
        if ftype_guess.mime not in ALLOWED_MIMETYPES:
            return False

    return True

def validate_form(form_dict, files_dict):
    errors = []

    # ¿Dónde?
    if not validate_region(form_dict.get("region")):
        errors.append("Región: debes seleccionar una región.")
    if not validate_comuna(form_dict.get("comuna")):
        errors.append("Comuna: debes seleccionar una comuna.")
    if not validate_sector(form_dict.get("sector")):
        errors.append("Sector: el sector no puede exceder 100 caracteres.")

    # Contacto
    if not validate_nombre(form_dict.get("nombre")):
        errors.append("Nombre: el nombre debe tener entre 3 y 200 caracteres.")
    if not validate_email(form_dict.get("email")):
        errors.append("Email: el email no tiene un formato válido o excede 100 caracteres.")
    if not validate_celular(form_dict.get("celular")):
        errors.append("Celular: el número de celular no tiene un formato válido.")

    selected = form_dict.getlist("contactar_por") if hasattr(form_dict, "getlist") else form_dict.get("contactar_por", [])
    ids_map = {}
    for key in (selected or []):
        ids_map[key.lower()] = (form_dict.get(f"contactar-{key}", "") or "").strip()
    errors += validate_contactar_por(selected, ids_map)

    # Mascota
    if not validate_tipo(form_dict.get("tipo-mascota")):
        errors.append("Tipo: debes seleccionar un tipo de mascota.")
    if not validate_cantidad(form_dict.get("cantidad")):
        errors.append("Cantidad: la cantidad de mascotas debe ser mínimo 1.")
    if not validate_edad(form_dict.get("edad")):
        errors.append("Edad: la edad debe ser mínimo 1.")
    if not validate_unidad_medida(form_dict.get("unidad-edad")):
        errors.append("Unidad de edad: debes seleccionar una unidad de edad.")
    if not validate_fecha_entrega(form_dict.get("fecha-entrega")):
        errors.append("Fecha disponible para entrega: debe tener formato válido y ser mayor a la fecha actual + 3 horas.")

    # Fotos (buscamos múltiples nombres posibles)
    files = []
    if hasattr(files_dict, "getlist"):
        files += files_dict.getlist("fotos")  # caso name="fotos"
    # soporta foto-1, foto-2, ...
    for k in getattr(files_dict, "keys", lambda: [])():
        if str(k).startswith("foto"):
            f = files_dict.get(k)
            if f:
                files.append(f)
    errors += validate_fotos(files)

    return (len(errors) == 0), errors