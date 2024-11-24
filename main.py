from fastapi import FastAPI
from app.database.configuration import engine
from app.api.models.modelosApp import Usuario,Base
#Categoria,MetodoPago,Factura,Base
from app.api.routes.rutas import rutas

from starlette.responses import RedirectResponse
from starlette.middleware.cors import   CORSMiddleware
#ACTIVAR LA ORM
Base.metadata.create_all(bind=engine)




#VARIABLE PARA ADMINISTRAR LA APLICACION 
app=FastAPI()

#ACTIVANDO CORS

app.add_middleware(
    CORSMiddleware,
allow_origins=["*"],
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"]

)


#ACTIVO EL API
@app.get("/")
def main():
    return RedirectResponse(url="/docs")

app.include_router(rutas)

#APRENDETE LOS CODIGOS DE RESPUESTAS PARA TRABAJAR CON LOS FRONTED 
#(COD200(EXITO) (COD300(REDIRECCION)) (COD500) HAKEO O LA CAGO EL BACKEND)
#(COD404) NO ENCONTRADO (COD400 ERROR DE FROND O DEL CLIENTE)