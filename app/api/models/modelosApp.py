from sqlalchemy import Column,Integer,String,Float,Date

from sqlalchemy.ext.declarative import declarative_base

#crear una instancia de la base para crear tablas 
Base = declarative_base()

#Listado de modelos de la aplicacion 
#Usuario
class Usuario(Base):
    __tablename__='usuarios'
    id = Column(Integer,primary_key=True , autoincrement=True)
    nombre= Column(String(50))
    edad= Column (Integer)
    telefono= Column(String(14))
    correo =Column(String(20))
    contrasena= Column(String(10))
    fechaRegistro= Column(Date)
    ciudad= Column(String(50))

#GASTO
class Gastos(Base):
    __tablename__='gastos'
    id= Column(Integer,primary_key=True, autoincrement=True)
    monto = Column(Float)
    fecha= Column(Date)
    descripcion= Column(String(100))
    nombre= Column(String(50))

#CATEGORIA 
class Categoria(Base):
    __tablename__='categoria'
    id= Column(Integer,primary_key=True, autoincrement=True)
    nombreCategoria= Column(String(100))
    descripcion= Column(String(100))
    fotoIcono= Column(String(50))

#METODOS DE PAGO
class MetodoPago(Base):
    __tablename__='metodoPago'
    id= Column(Integer,primary_key=True, autoincrement=True)
    nombreMetodo= Column(String(80))
    descripcion= Column(String(100))
    fotoIcono=Column(String(100))
    entidad= Column (String(100))

#FACTURA
class Factura(Base):
    __tablename__='facturas'
    id= Column(Integer,primary_key=True, autoincrement=True)
    fecha= Column(Date)
    monto= Column(Float)
    descripcion= Column(String(100))
