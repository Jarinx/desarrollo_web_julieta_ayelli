from flask import Flask, flash, request, render_template, redirect, url_for, jsonify
from database import db
from werkzeug.utils import secure_filename
import hashlib
import filetype # type: ignore
import os
import datetime as dt
from utils.validations import validate_form
import math

UPLOAD_FOLDER = r'static\uploads\avisos'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
CONTACT_METHODS = [
    ("whatsapp", "WhatsApp"),
    ("telegram", "Telegram"),
    ("X", "X"),
    ("instagram", "Instagram"),
    ("tiktok", "TikTok"),
    ("otra", "Otra"),
]

app = Flask(__name__)

app.secret_key = "s3cr3t_k3y"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# --- Helpers ---
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def fecha_entrega_min(minutes):
    fecha = dt.datetime.now() + dt.timedelta(minutes=minutes)
    return fecha.strftime("%Y-%m-%dT%H:%M")

# --- PORTADA ---
@app.route("/")
@app.route("/portada")
def portada():
    avisos, prev, next = db.get_avisos_adopcion(5, 1)
    return render_template("portada/portada.html", avisos=avisos)
    
# --- AVISO ADOPCION ---
@app.route("/form-adopcion", methods=["GET"])
def form_adopcion():
    submitted = request.args.get("submitted") == "1"
    entrega_min = fecha_entrega_min(180)

    return render_template(
        "form-adopcion/form-adopcion.html",
        submitted=submitted,
        error=None,
        form_array=None,
        entrega_min=entrega_min,
        contact_methods=CONTACT_METHODS,
        contactar_por_select=[],
        contactar_ids={}
    )
    
@app.route("/post-adopcion", methods=["POST"])
def post_aviso_adopcion():
    form = request.form

    # ¿donde?
    region = form.get("region") # [0]
    comuna = form.get("comuna") # [1]
    sector = form.get("sector") # [2]

    # ¿contacto?
    nombre = form.get("nombre") # [3]
    email = form.get("email") # [4]
    celular = form.get("celular") # [5]
    contactar_por_nombre = form.getlist("contactar-por") # [6] 
    contactar_por_ids = {name: form.get(f"contactar-{name}", "") for name in contactar_por_nombre}

    # ¿mascota?
    tipo = form.get("tipo-mascota") # [7]
    cantidad = form.get("cantidad") # [8]
    edad = form.get("edad") # [9]
    unidad_medida = form.get("unidad-edad") # [10]
    fecha_entrega = form.get("fecha-entrega") # [11]
    descripcion = form.get("descripcion") # [12]
    fotos = request.files.getlist("fotos") # [13]

    form_array = [
        region,
        comuna,
        sector,
        nombre,
        email,
        celular,
        [contactar_por_nombre, contactar_por_ids], # [6]
        tipo,
        cantidad,
        edad,
        unidad_medida,
        fecha_entrega,
        descripcion,
        fotos
    ]

    print("(app) Datos recibidos:", form_array)
    print("(app) Validez form:", validate_form(form_array))

    status, errores = validate_form(form_array)

    if status:
        # 1. guardar info del aviso en la db
        fecha_ingreso = dt.datetime.now()
        comuna_id = comuna
        if sector == "":
            sector = None
        nombre = nombre
        email = email
        if celular == "":
            celular = None
        tipo = tipo
        cantidad = int(cantidad)
        edad = int(edad)
        unidad_medida = unidad_medida
        fecha_entrega = fecha_entrega
        if descripcion == "":
            descripcion = None

        new_aviso_id = db.add_aviso_adopcion(
            fecha_ingreso,
            comuna_id,
            sector,
            nombre,
            email,
            celular,
            tipo,
            cantidad,
            edad,
            unidad_medida,
            fecha_entrega,
            descripcion)
        
        print("(app) Nuevo aviso ID:", new_aviso_id)

        # 2. guardar contactos en la db
        print("(app) Contactar_por lista:", contactar_por_nombre)
        for nombre in contactar_por_nombre:
            identificador = contactar_por_ids.get(nombre)
            new_contacto_id = db.add_contactar_por(nombre, identificador, new_aviso_id)
            print("(app) Nuevo contacto:", new_contacto_id, nombre, identificador)
        
        # 3. guardar fotos en la db
        print("(app) Fotos lista:", fotos)
        ruta_archivo = os.path.join(app.config["UPLOAD_FOLDER"], f"aviso_{new_aviso_id}")
        os.makedirs(ruta_archivo, exist_ok=True)
        print("(app) Ruta archivo fotos:", ruta_archivo)
        for foto in fotos:
            print("(app) Procesando foto:", foto.filename)
            # 3.i generar nombre random para cada foto
            _filename = hashlib.sha256(
                secure_filename(foto.filename) # nombre del archivo
                .encode("utf-8") # encodear a bytes
                ).hexdigest()
            _extension = filetype.guess(foto).extension
            nombre_archivo = f"{_filename}.{_extension}"
            print(f"(app) Nombre archivo foto generado: {nombre_archivo}")

            # 3.ii guardar foto en folder correspondiente
            foto.save(os.path.join(ruta_archivo, nombre_archivo))
            # foto.save(ruta_archivo)
            print(f"(app) Foto guardada en: {ruta_archivo}/{nombre_archivo}")

            # 3.iii guardar foto en la db
            new_foto_id = db.add_foto(ruta_archivo, nombre_archivo, new_aviso_id)
            print(f"(app) Nueva foto ID: {new_foto_id} guardada en: {ruta_archivo}/{nombre_archivo}")

        print("(app) AVISO CREADO EXITOSAMENTE!")

        return redirect(url_for("form_adopcion", submitted=1))
    
    # si hubo algún error en la validación
    new_entrega_min = fecha_entrega_min(180)
    return render_template(
        "form-adopcion/form-adopcion.html",
        errores=errores,
        form_array=form_array,
        entrega_min=new_entrega_min,
        contact_methods=CONTACT_METHODS,
        contactar_por_select=contactar_por_nombre,
        contactar_ids=contactar_por_ids
    )

# --- LISTADO ---
@app.route("/listado")
def listado():
    pag = int(request.args.get("pag", default=1))
    if pag < 1:
        pag = 1
    
    pag_items = 5

    avisos, prev, next = db.get_avisos_adopcion(pag_items, pag)
    total_avisos = len(avisos) + len(prev) + len(next)
    total_paginas = max(1, math.ceil(total_avisos/pag_items))

    if pag > total_paginas:
        pag = total_paginas

    return render_template(
        "listado/listado.html",
        avisos=avisos,
        pag=pag,
        total_paginas=total_paginas,
        has_prev=(pag > 1),
        has_next=(pag < total_paginas)
        )

@app.route("/aviso/<int:aviso_id>")
def aviso_detalle(aviso_id):
    aviso = db.get_aviso_detalle(aviso_id)
    return render_template("listado/detalle.html", aviso=aviso)

# --- ESTADISTICAS ---
@app.route("/estadisticas")
def estadisticas():
    return render_template("estadisticas/estadisticas.html")