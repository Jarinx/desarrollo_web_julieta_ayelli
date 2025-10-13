from flask import Flask, flash, request, render_template, redirect, url_for, jsonify
from database import db
from werkzeug.utils import secure_filename
import hashlib
import filetype # type: ignore
import os
from database import db
import datetime
from utils.validations import validate_form

UPLOAD_FOLDER = 'static/uploads/avisos'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)

app.secret_key = "s3cr3t_k3y"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# --- Helpers ---
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# --- PORTADA ---
@app.route("/")
@app.route("/portada")
def portada():
    avisos = db.get_avisos_adopcion(5)
    return render_template("portada/portada.html", avisos=avisos)
    
# --- AVISO ADOPCION ---
@app.route("/form-adopcion", methods=["GET"])
def form_adopcion():
    return render_template("form-adopcion/form-adopcion.html")
    
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
    contactar_por = form.getlist("contactar-por") # [6] 

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
        contactar_por,
        tipo,
        cantidad,
        edad,
        unidad_medida,
        fecha_entrega,
        descripcion,
        fotos
    ]

    print("Datos recibidos:", form_array)

    if validate_form(form_array):
        # primero guardar info del aviso en la db
        fecha_ingreso = datetime.datetime.now()
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
        #contactos = contactar_por
        #fotos = fotos

        new_aviso_id = db.create_form_adopcion(
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
        
        print("Nuevo aviso ID:", new_aviso_id)

    print("Validez form:", validate_form(form_array))
            
    return render_template("form-adopcion/form-adopcion.html")
            





            # después guardar fotos bajo el id del aviso
            # for f in fotos:
            #     _filename = hashlib.sha256(
            #         secure_filename(f.filename) # nombre del archivo
            #         .encode("utf-8") # encodear a bytes
            #         ).hexdigest()
            #     _extension = filetype.guess(f).extension
            #     img_filename = f"{_filename}.{_extension}"
            
            #     f.save(os.path.join(app.config["UPLOAD_FOLDER"], img_filename))
        

        









# --- LISTADO ---
@app.route("/listado")
def listado():
    return render_template("listado/listado.html")

# --- ESTADISTICAS ---
@app.route("/estadisticas")
def estadisticas():
    return render_template("estadisticas/estadisticas.html")