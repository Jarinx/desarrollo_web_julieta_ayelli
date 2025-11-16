from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from database.models import AvisoAdopcion, Foto, Comuna, ContactarPor, Comentario

DB_NAME = "tarea4"
DB_USERNAME = "cc5002"
DB_PASSWORD = "programacionweb"
DB_HOST = "localhost"
DB_PORT = 3306
DB_CHARSET = "utf8"

DATABASE_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine)

# -- helpers --
def plural_unidad(unidad, edad):
    if unidad == 'a':
        if edad > 1:
            return 'años'
        else:
            return 'año'
    elif unidad == 'm':
        if edad > 1:
            return 'meses'
        else:
            return 'mes'
    return unidad

# --- GET FROM DB FUNCTIONS ---
def get_avisos_adopcion(limit, pag):
    session = SessionLocal()
    offset = (pag-1) * limit

    # avisos desde 0 hasta offset
    prev = (
        session.query(AvisoAdopcion)
        .order_by(AvisoAdopcion.fecha_ingreso.desc())
        .all()[:offset]
    )
    # avisos desde offset hasta offset+5
    avisos = (
        session.query(AvisoAdopcion)
        .order_by(AvisoAdopcion.fecha_ingreso.desc())
        .limit(limit)
        .offset(offset)
        .all()
    )
    # avisos desde offset+5 hasta el último
    next = (
        session.query(AvisoAdopcion)
        .order_by(AvisoAdopcion.fecha_ingreso.desc())
        .offset(offset+limit)
        .all()
    )
    resultado = []
    for aviso in avisos:
        fotos = (
            session.query(Foto)
            .filter(Foto.aviso_id == aviso.id)
            .all()
        )
        fotos_list = []
        for f in fotos:
            fotos_list.append({
                "src": f"{f.ruta_archivo}/{f.nombre_archivo}",
                "alt": f"{aviso.cantidad} {aviso.tipo}(s)"
            })

        contactos = (
            session.query(ContactarPor)
            .filter(ContactarPor.aviso_id == aviso.id)
            .all()
        )
        contactos_list = []
        if contactos == []:
            contactos_list.append({
                "nombre": "No proporcionado",
                "identificador": "No proporcionado"
            })
        else:
            for c in contactos:
                contactos_list.append({
                    "nombre": c.nombre,
                    "identificador": c.identificador
                })

        resultado.append({
            "aviso_id": aviso.id,
            "fecha_ingreso": aviso.fecha_ingreso.strftime("%Y-%m-%d %H:%M"),
            "fecha_entrega": aviso.fecha_entrega.strftime("%Y-%m-%d %H:%M"),
            "comuna": aviso.comuna.nombre,
            "sector": f"{'No proporcionado' if aviso.sector == None else aviso.sector}",
            "nombre": aviso.nombre,
            "email": aviso.email,
            "celular": f"{'No proporcionado' if aviso.celular == None else aviso.celular}",
            "cantidad": aviso.cantidad,
            "tipo": f"{aviso.tipo+'s' if aviso.cantidad > 1 else aviso.tipo}",
            "edad": aviso.edad,
            "unidad_medida": plural_unidad(aviso.unidad_medida, aviso.edad),
            "descripcion": f"{'No proporcionado' if aviso.descripcion == None else aviso.descripcion}",
            "contactar_por": contactos_list,
            "total_fotos": len(fotos),
            "fotos": fotos_list
        })

    session.close()
    return resultado, prev, next

def get_aviso_detalle(aviso_id):
    session = SessionLocal()
    aviso = session.query(AvisoAdopcion).get(aviso_id)
    comuna_id = aviso.comuna_id
    region = session.query(Comuna).get(comuna_id).region.nombre

    fotos = (
            session.query(Foto)
            .filter(Foto.aviso_id == aviso.id)
            .all()
        )
    fotos_list = []
    for f in fotos:
        fotos_list.append({
            "src": f"{f.ruta_archivo}/{f.nombre_archivo}",
            "alt": f"{aviso.cantidad} {aviso.tipo}(s)"
        })
    contactos = (
        session.query(ContactarPor)
        .filter(ContactarPor.aviso_id == aviso.id)
        .all()
    )
    contactos_list = []
    if contactos == []:
        contactos_list.append({
            "nombre": "No proporcionado",
            "identificador": "No proporcionado"
        })
    else:
        for c in contactos:
            contactos_list.append({
                "nombre": c.nombre,
                "identificador": c.identificador
            })

    detalle = {
        "aviso_id": aviso.id,
        "fecha_ingreso": aviso.fecha_ingreso.strftime("%Y-%m-%d %H:%M"),
        "fecha_entrega": aviso.fecha_entrega.strftime("%Y-%m-%d %H:%M"),
        "region": region,
        "comuna": aviso.comuna.nombre,
        "sector": f"{'No proporcionado' if aviso.sector == None else aviso.sector}",
        "nombre": aviso.nombre,
        "email": aviso.email,
        "celular": f"{'No proporcionado' if aviso.celular == None else aviso.celular}",
        "cantidad": aviso.cantidad,
        "tipo": f"{aviso.tipo+'s' if aviso.cantidad > 1 else aviso.tipo}",
        "edad": aviso.edad,
        "unidad_medida": plural_unidad(aviso.unidad_medida, aviso.edad),
        "descripcion": f"{'No proporcionado' if aviso.descripcion == None else aviso.descripcion}",
        "contactar_por": contactos_list,
        "total_fotos": len(fotos),
        "fotos": fotos_list
    }

    session.close()
    return detalle

def get_comuna_id_by_name(comuna):
    session = SessionLocal()
    comuna_id = session.query(Comuna.id).filter(Comuna.nombre == comuna).first()
    session.close()
    return comuna_id

def get_avisos_por_dia():
    session = SessionLocal()

    avisos_x_dia = (
        session.query(func.date(AvisoAdopcion.fecha_ingreso).label("dia"),
                      func.count(AvisoAdopcion.id).label("avisos"))
                      .group_by(func.date(AvisoAdopcion.fecha_ingreso))
                      .order_by(func.date(AvisoAdopcion.fecha_ingreso))
                      .limit(30)
                      .all()
    )
    datos = []
    for a in avisos_x_dia:
        datos.append({
            "dia": str(a.dia),
            "avisos": a.avisos
        })

    session.close()
    return datos

def get_total_por_tipo():
    session = SessionLocal()

    total_x_tipo = (
        session.query(AvisoAdopcion.tipo.label("tipo"),
                      func.count(AvisoAdopcion.id).label("total"))
                      .group_by(AvisoAdopcion.tipo)
                      .all()
    )
    datos = []
    for a in total_x_tipo:
        datos.append({
            "tipo": a.tipo,
            "total": a.total
        })

    session.close()
    return datos

def get_por_mes_y_tipo():
    session = SessionLocal()
    mes_expr = func.date_format(AvisoAdopcion.fecha_ingreso, '%Y-%m')

    avisos_x_mes_tipo = (
        session.query(
            mes_expr.label("mes"),
            AvisoAdopcion.tipo.label("tipo"),
            func.count(AvisoAdopcion.id).label("avisos")
        )
        .group_by(mes_expr, AvisoAdopcion.tipo)
        .order_by(mes_expr.asc())
        .all()
    )
    datos = []
    for a in avisos_x_mes_tipo:
        datos.append({
            "mes": a.mes,
            "tipo": a.tipo,
            "avisos": a.avisos
        })

    session.close()
    return datos
    
def get_estadisticas():
    stats = {
        "avisos_por_dia": get_avisos_por_dia(),
        "total_por_tipo": get_total_por_tipo(),
        "por_mes_y_tipo": get_por_mes_y_tipo()
    }
    return stats

def get_comentarios(aviso_id):
    session = SessionLocal()
    comentarios = (
        session.query(Comentario)
        .filter(Comentario.aviso_id == aviso_id)
        .order_by(Comentario.id.desc())
        .all()
    )
    comentarios_list = []
    for c in comentarios:
        comentarios_list.append({
            "nombre": c.nombre,
            "texto": c.texto,
            "fecha": c.fecha.strftime("%Y-%m-%d %H:%M")
        })
    session.close()
    return comentarios_list

# --- ADD TO DB FUNCTIONS ---
def add_aviso_adopcion(
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
        descripcion):
    
    session = SessionLocal()

    new_aviso = AvisoAdopcion(fecha_ingreso=fecha_ingreso,
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
                                descripcion=descripcion)
    
    session.add(new_aviso)
    session.commit()
    id = new_aviso.id
    session.close()

    return id

def add_contactar_por(
        nombre,
        identificador,
        aviso_id):
    
    session = SessionLocal()
    
    new_contacto = ContactarPor(nombre=nombre,
                                identificador=identificador,
                                aviso_id=aviso_id)
    
    session.add(new_contacto)
    session.commit()
    id = new_contacto.id
    session.close()

    return id

def add_foto(
        ruta_archivo,
        nombre_archivo,
        aviso_id):
    
    session = SessionLocal()

    new_foto = Foto(ruta_archivo=ruta_archivo,
                    nombre_archivo=nombre_archivo,
                    aviso_id=aviso_id)
    
    session.add(new_foto)
    session.commit()
    id = new_foto.id
    session.close()

    return id

def add_comentario(
        nombre,
        texto,
        fecha,
        aviso_id):
    
    session = SessionLocal()

    new_comentario = Comentario(nombre=nombre,
                                texto=texto,
                                fecha=fecha,
                                aviso_id=aviso_id)
    
    session.add(new_comentario)
    session.commit()
    
    new_comentario_dict = {
        "nombre": new_comentario.nombre,
        "texto": new_comentario.texto,
        "fecha": new_comentario.fecha.strftime("%Y-%m-%d %H:%M"),
        "aviso_id": new_comentario.aviso_id
    }

    session.close()

    return new_comentario_dict