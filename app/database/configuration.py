from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine

#Conexion a la BD
#nombreBD
dataBaseName="gestionbd"

#usuarioBD
userName="root"

#Contraseña del usuario
userPassword=""

#PUERTO DE CONEXION
conexionPort="3306"

#servidor conexion
serverConnection="localhost"

#CREANDO LA CONEXION
connectionToDataBase=f"mysql+mysqlconnector://{userName}:{userPassword}@{serverConnection}:{conexionPort}/{dataBaseName}"

engine=create_engine(connectionToDataBase)
sessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)


