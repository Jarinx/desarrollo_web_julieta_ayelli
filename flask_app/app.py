from flask import Flask, request, render_template, redirect, url_for, session
from database import db
from werkzeug.utils import secure_filename
import hashlib
import filetype
import os
from database import db

UPLOAD_FOLDER = 'static/uploads'

app = Flask(__name__)

app.secret_key = "s3cr3t_k3y"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# --- PORTADA ---
@app.route("/portada", methods=["GET", "POST"])
def portada():
    if request.method == "GET":
        avisos = db.get_ultimos_avisos()
        return render_template("portada/portada.html", avisos=avisos)