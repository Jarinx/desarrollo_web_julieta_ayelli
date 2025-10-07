from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Enum, Index, Text
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

Base = declarative_base()

# Resumen de relaciones:
#   |region| 1 ---< N |comuna|
#   |comuna| 1 ---< N |aviso_adopcion|
#   |aviso_adopcion| 1 ———< N |foto|
#   |aviso_adopcion| 1 ———< N |contactar_por|

class Region(Base):
    __tablename__ = 'region'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(200), nullable=False)

    comunas = relationship("Comuna", back_populates="region", cascade="all, delete-orphan")

class Comuna(Base):
    __tablename__ = 'comuna'
    __table_args__ = (
        Index('fk_comuna_region1_idx', 'region_id'),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(200), nullable=False)
    region_id = Column(Integer, ForeignKey('region.id'), nullable=False)

    region = relationship("Region", back_populates="comunas")
    avisos = relationship("AvisoAdopcion", back_populates="comuna", cascade="all, delete-orphan")

class AvisoAdopcion(Base):
    __tablename__ = 'aviso_adopcion'
    __table_args__ = (
        Index('fk_aviso_comuna1_idx', 'comuna_id'),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha_ingreso = Column(DateTime, nullable=False)
    comuna_id = Column(Integer, ForeignKey('comuna.id'), nullable=False)
    sector = Column(String(100), nullable=True)
    nombre = Column(String(200), nullable=False)
    email = Column(String(100), nullable=False)
    celular = Column(String(15), nullable=True)
    tipo = Column(Enum('gato', 'perro'), nullable=False)
    cantidad = Column(Integer, nullable=False)
    edad = Column(Integer, nullable=False)
    unidad_medida = Column(Enum('a', 'm'), nullable=False)
    fecha_entrega = Column(DateTime, nullable=False)
    descripcion = Column(String(500), nullable=True)

    comuna = relationship("Comuna", back_populates="avisos")
    fotos = relationship("Foto", back_populates="aviso", cascade="all, delete-orphan")
    contactos = relationship("ContactarPor", back_populates="aviso", cascade="all, delete-orphan")

class Foto(Base):
    __tablename__ = 'foto'
    __table_args__ = (
        Index('fk_foto_aviso1_idx', 'aviso_id'),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    ruta_archivo = Column(String(300), nullable=False)
    nombre_archivo = Column(String(300), nullable=False)
    aviso_id = Column(Integer, ForeignKey('aviso_adopcion.id'), nullable=False)

    aviso = relationship("AvisoAdopcion", back_populates="fotos")

class ContactarPor(Base):
    __tablename__ = 'contactar_por'
    __table_args__ = (
        Index('fk_contactar_por_aviso1_idx', 'aviso_id'),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(Enum('whatsapp', 'telegram', 'X', 'instagram', 'tiktok', 'otra'), nullable=False)
    identificador = Column(String(150), nullable=False)
    aviso_id = Column(Integer, ForeignKey('aviso_adopcion.id'), nullable=False)

    aviso = relationship("AvisoAdopcion", back_populates="contactos")