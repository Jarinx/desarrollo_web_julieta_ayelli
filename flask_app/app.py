from flask import Flask, flash, request, render_template, redirect, url_for, jsonify
from database import db
from werkzeug.utils import secure_filename
import hashlib
import filetype
import os
from database import db
import datetime

UPLOAD_FOLDER = 'static/uploads/avisos'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)

app.secret_key = "s3cr3t_k3y"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# --- Helpers ---
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def change_un_edad(unidad):
    if unidad == 'años':
        return 'a'
    elif unidad == 'meses':
        return 'm'

# --- PORTADA ---
@app.route("/")
@app.route("/portada")
def portada():
    avisos = db.get_ultimos_avisos()
    return render_template("portada/portada.html", avisos=avisos)
    
# --- AVISO ADOPCION ---
@app.route("/form-adopcion", methods=["GET", "POST"])
def form_adopcion():
    if request.method == "GET":
        regiones = db.get_regiones()
        return render_template("form-adopcion/form-adopcion.html", regiones=regiones)
    
    elif request.method == "POST":
        form = request.form

        # ¿donde?
        region_id = form.get("region")
        comuna_id = form.get("comuna")
        sector = form.get("sector")

        # contacto
        nombre = form.get("nombre")
        email = form.get("email")
        celular = form.get("celular")

        # mascota
        tipo = form.get("tipo-mascota")
        cantidad = form.get("cantidad")
        edad = form.get("edad")
        unidad_medida = change_un_edad(form.get("unidad-medida"))
        fecha_entrega_raw = form.get("fecha-entrega")
        fecha_entrega = datetime.strptime(fecha_entrega_raw, '%Y-%m-%dT%H:%M')
        descripcion = form.get("descripcion")

        fecha_ingreso = datetime.datetime.now()

        files = request.files
        ok, errores = db.validate_form(form, files)
        if ok:
            for f in files.getlist("fotos"):
                _filename = hashlib.sha256(
                    secure_filename(f.filename) # nombre del archivo
                    .encode("utf-8") # encodear a bytes
                    ).hexdigest()
                _extension = filetype.guess(f).extension
                img_filename = f"{_filename}.{_extension}"
            
                f.save(os.path.join(app.config["UPLOAD_FOLDER"], img_filename))

                db.create_form_adopcion(
                    fecha_ingreso=fecha_ingreso,
                    comuna_id=comuna_id,
                    sector=sector,
                    nombre=nombre,
                    email=email,
                    celular=celular,
                    tipo=tipo,
                    cantidad=cantidad,
                    edad=edad,
                    unidad_medida=unidad_medida,
                    fecha_entrega=fecha_entrega,
                    descripcion=descripcion,
                    contactos=[{"nombre": c, "identificador": form.get(f"contactar-{c}", "").strip()} for c in form.getlist("contactar-por")],
                    fotos=[]
                )


# --- LISTADO ---
@app.route("/listado")
def listado():
    return render_template("listado/listado.html")

# --- ESTADISTICAS ---
@app.route("/estadisticas")
def estadisticas():
    return render_template("estadisticas/estadisticas.html")