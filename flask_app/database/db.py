from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from database.models import Base, AvisoAdopcion, Foto, Comuna, Region, ContactarPor

DB_NAME = "tarea2"
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

# --- DATABASE FUNCTIONS ---
def get_avisos_adopcion(limit):
    session = SessionLocal()
    avisos = (
        session.query(AvisoAdopcion)
        .order_by(AvisoAdopcion.fecha_ingreso.desc())
        .limit(limit)
        .all()
    )
    resultado = []
    for aviso in avisos:
        foto = aviso.fotos[0].nombre_archivo
        resultado.append({
            "fecha": aviso.fecha_ingreso.strftime("%Y-%m-%d %H:%M"),
            "comuna": aviso.comuna.nombre,
            "sector": f"{'No proporcionado' if aviso.sector == None else aviso.sector}",
            "cantidad": aviso.cantidad,
            "tipo": f"{aviso.tipo+'s' if aviso.cantidad > 1 else aviso.tipo}",
            "edad": aviso.edad,
            "unidad_medida": plural_unidad(aviso.unidad_medida, aviso.edad),
            "foto": foto, # Obtener la primera foto (si existe)
            "alt": f"{aviso.cantidad} {aviso.tipo}(s)"
        })
    session.close()
    
    return resultado

def get_comuna_id_by_name(comuna):
    session = SessionLocal()
    comuna_id = session.query(Comuna.id).filter(Comuna.nombre == comuna).first()
    session.close()
    return comuna_id

def create_form_adopcion(
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
    
    allowed_contactos = {'whatsapp', 'telegram', 'X', 'instagram', 'tiktok', 'otra'}

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
    session = SessionLocal()
    session.add(new_aviso)
    session.commit()
    session.close()
    print("Creando aviso:", new_aviso)


    return new_aviso.id

    