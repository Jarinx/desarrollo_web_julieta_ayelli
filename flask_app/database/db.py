from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
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

# --- DATABASE FUNCTIONS ---
def get_ultimos_avisos(limit=5):
    session = SessionLocal()
    avisos = (
        session.query(AvisoAdopcion)
        .order_by(AvisoAdopcion.fecha_ingreso.desc())
        .limit(limit)
        .all()
    )
    resultado = []
    for aviso in avisos:
        # Obtener la primera foto (si existe)
        foto = aviso.fotos[0].nombre_archivo
        resultado.append({
            "fecha": aviso.fecha_ingreso.strftime("%Y-%m-%d %H:%M"),
            "comuna": aviso.comuna.nombre,
            "sector": aviso.sector,
            "cantidad": aviso.cantidad,
            "tipo": aviso.tipo,
            "edad": f"{aviso.edad} {'año' if aviso.unidad_medida == 'a' else 'mes'}",
            "foto": foto,
            "alt": f"{aviso.cantidad} {aviso.tipo}(s)"
        })
    session.close()
    return resultado

def insert_reg_com(sql_path: str, force: bool = False) -> None:
    with engine.begin() as conn:
        existing = conn.execute(text("SELECT COUNT(*) FROM region")).scalar()
        if existing and not force:
            print(f"Saltado: ya existen {existing} regiones. Usa force=True para recargar.")
            return

        if force:
            # Limpiar respetando FKs
            conn.execute(text("SET FOREIGN_KEY_CHECKS=0"))
            conn.execute(text("TRUNCATE TABLE comuna"))
            conn.execute(text("TRUNCATE TABLE region"))
            conn.execute(text("SET FOREIGN_KEY_CHECKS=1"))

        # Leer y partir el script en sentencias (simples INSERTs terminados en ;)
        with open(sql_path, "r", encoding="utf-8") as f:
            script = f.read()

        statements = [s.strip() for s in script.split(";") if s.strip()]
        for stmt in statements:
            conn.exec_driver_sql(stmt)

def get_regiones():
    session = SessionLocal()
    regiones = session.query(Region).order_by(Region.nombre).all()
    session.close()
    return regiones

def get_comunas_por_region(region_id: int):
    session = SessionLocal()
    comunas = session.query(Comuna).filter(Comuna.region_id == region_id).order_by(Comuna.nombre).all()
    session.close()
    return comunas

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
        descripcion,
        contactos,
        fotos):
    
    allowed_contactos = {'whatsapp', 'telegram', 'x', 'instagram', 'tiktok', 'otra'}

    session = SessionLocal()

    new_aviso = AvisoAdopcion(
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
        descripcion=descripcion)
    
    session.add(new_aviso)
    session.commit()  

    for contacto in contactos:
        nombre = contacto.get("nombre").lower()
        ident = contacto.get("identificador", None).strip()
        if nombre in allowed_contactos and ident:
            new_contacto = ContactarPor(
                nombre=nombre,
                identificador=ident,
                aviso_id=new_aviso.id
            )
            session.add(new_contacto)

    for foto in fotos:
        ruta_archivo = foto.get("ruta_archivo")
        nombre_archivo = foto.get("nombre_archivo")
        if ruta_archivo and nombre_archivo:
            new_foto = Foto(
                ruta_archivo=ruta_archivo,
                nombre_archivo=nombre_archivo,
                aviso_id=new_aviso.id
            )
            session.add(new_foto)

    return new_aviso.id