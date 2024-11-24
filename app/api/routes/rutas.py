from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List
from fastapi.params import Depends
from app.api.schemas.DTO import (
    UsuarioDTOPeticion,
    UsuarioDTORespuesta,
    GastoDTOPeticion,
    GastoDTORespuesta,
    CategoriaDTOPeticion,
    CategoriaDTORespuesta,
    MetodoPagoDTOPeticion,
    MetodoPagoDTORespuesta,
    FacturaDTOPeticion,
    FacturaDTORespuesta
)
from app.api.models.modelosApp import Usuario, Gastos, Categoria, MetodoPago, Factura
from app.database.configuration import sessionLocal

rutas = APIRouter()  # ENDPOINTS

# Función para establecer conexión con la base de datos
def getDataBase():
    basedatos = sessionLocal()
    try:
        yield basedatos
    except Exception as error:
        basedatos.rollback()
        raise error
    finally:
        basedatos.close()

# Servicios de la API basados en CRUD

@rutas.post("/usuarios", response_model=UsuarioDTORespuesta)
def guardarUsuario(datosPeticion: UsuarioDTOPeticion, db: Session = Depends(getDataBase)):
    try:
        usuario = Usuario(
            nombre=datosPeticion.nombre,
            edad=datosPeticion.edad,
            telefono=datosPeticion.telefono,
            correo=datosPeticion.correo,
            contrasena=datosPeticion.contrasena,
            fechaRegistro=datosPeticion.fechaRegistro,
            ciudad=datosPeticion.ciudad
        )
        db.add(usuario)
        db.commit()
        db.refresh(usuario)
        return usuario
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error al registrar el usuario {error}")

@rutas.post("/gastos", response_model=GastoDTOPeticion)
def guardarGasto(datosPeticion: GastoDTOPeticion, db: Session = Depends(getDataBase)):
    try:
        gastos = Gastos(
            monto=datosPeticion.monto,
            fecha=datosPeticion.fecha,
            nombre=datosPeticion.nombre,
            descripcion=datosPeticion.descripcion,
        )
        db.add(gastos)
        db.commit()
        db.refresh(gastos)
        return gastos
    except Exception as errores:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error al registrar el gasto {errores}")

@rutas.post("/categoria", response_model=CategoriaDTORespuesta)
def guardarCategoria(datosPeticion: CategoriaDTOPeticion, db: Session = Depends(getDataBase)):
    try:
        categoria = Categoria(
            nombreCategoria=datosPeticion.nombreCategoria,
            descripcion=datosPeticion.descripcion,
            fotoIcono=datosPeticion.fotoIcono
        )
        db.add(categoria)
        db.commit()
        db.refresh(categoria)
        return categoria
    except Exception as errores:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error al registrar la categoría {errores}")

@rutas.post("/metodoPago", response_model=MetodoPagoDTORespuesta)
def guardarMetodoPago(datosPeticion: MetodoPagoDTOPeticion, db: Session = Depends(getDataBase)):
    try:
        metodoPago = MetodoPago(
            nombreMetodo=datosPeticion.nombreMetodo,
            descripcion=datosPeticion.descripcion,
            fotoIcono=datosPeticion.fotoIcono,
            entidad=datosPeticion.entidad
        )
        db.add(metodoPago)
        db.commit()
        db.refresh(metodoPago)
        return metodoPago
    except Exception as errores:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error al registrar el método de pago {errores}")

@rutas.get("/usuarios", response_model=List[UsuarioDTORespuesta])
def buscarUsuarios(db: Session = Depends(getDataBase)):
    try:
        listadoDeUsuarios = db.query(Usuario).all()
        return [
            UsuarioDTORespuesta(
                id=usuario.id,
                nombre=usuario.nombre,
                telefono=usuario.telefono,
                ciudad=usuario.ciudad
            ) for usuario in listadoDeUsuarios
        ]
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error al obtener los usuarios {error}")

@rutas.post("/factura", response_model=FacturaDTORespuesta)
def guardarFactura(datosPeticion: FacturaDTOPeticion, db: Session = Depends(getDataBase)):
    try:
        factura = Factura(
            fecha=datosPeticion.fecha,
            monto=datosPeticion.monto,
            descripcion=datosPeticion.descripcion
        )
        db.add(factura)
        db.commit()
        db.refresh(factura)
        return factura
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error al registrar la factura {error}")

@rutas.get("/gastos", response_model=List[GastoDTORespuesta])
def buscarGastos(db: Session = Depends(getDataBase)):
    try:
        listadoDeGastos = db.query(Gastos).all()  # Corrección aquí
        return listadoDeGastos
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error al obtener los gastos {error}")

@rutas.get("/categoria", response_model=List[CategoriaDTORespuesta])
def buscarCategoria(db: Session = Depends(getDataBase)):
    try:
        listadoDeCategoria = db.query(Categoria).all()  # Corrección aquí
        return listadoDeCategoria
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error al obtener las categorías {error}")

@rutas.get("/metodoPago", response_model=List[MetodoPagoDTORespuesta])
def buscarMetodoPago(db: Session = Depends(getDataBase)):
    try:
        listadoDeMetodoPago = db.query(MetodoPago).all()  
        return listadoDeMetodoPago
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error al obtener los métodos de pago {error}")
