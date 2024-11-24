#Analisis de datos con panda(ANALISIS DESCPTIVO)
#1.Para analizar datos con panda necesitamos instalar e importar las herramientas
import pandas as pd



#2.Se optiene la fuente de datos
#Lista de datos
datos=[
    {'Nombre':'Estiliano Gallego','Ciudad':'Medellin','Edad':35},
    {'Nombre':'Rogelio parra','Ciudad':'Itagui','Edad':15},
    {'Nombre':'Armando casas','Ciudad':'Bello','Edad':55},
    {'Nombre':'Bob constructor','Ciudad':'Bogota','Edad':45},
    {'Nombre':'Marly Rastas','Ciudad':'Medellin','Edad':18},
     {'Nombre':'Estiliano Gallego','Ciudad':'Medellin','Edad':35},
    {'Nombre':'Rogelio parra','Ciudad':'Itagui','Edad':15},
    {'Nombre':'Armando casas','Ciudad':'Bello','Edad':55},
    {'Nombre':'Bob constructor','Ciudad':'Bogota','Edad':45},
    {'Nombre':'Marly Rastas','Ciudad':'Medellin','Edad':18},
     {'Nombre':'Estiliano Gallego','Ciudad':'Medellin','Edad':35},
    {'Nombre':'Rogelio parra','Ciudad':'Itagui','Edad':15},
    {'Nombre':'Armando casas','Ciudad':'Bello','Edad':55},
    {'Nombre':'Bob constructor','Ciudad':'Bogota','Edad':45},
    {'Nombre':'Marly Rastas','Ciudad':'Medellin','Edad':18},
     {'Nombre':'Estiliano Gallego','Ciudad':'Medellin','Edad':35},
    {'Nombre':'Rogelio parra','Ciudad':'Itagui','Edad':15},
    {'Nombre':'Armando casas','Ciudad':'Bello','Edad':55},
    {'Nombre':'Bob constructor','Ciudad':'Bogota','Edad':45},
    {'Nombre':'Marly Rastas','Ciudad':'Medellin','Edad':18},
     {'Nombre':'Estiliano Gallego','Ciudad':'Medellin','Edad':35},
    {'Nombre':'Rogelio parra','Ciudad':'Itagui','Edad':15},
    {'Nombre':'Armando casas','Ciudad':'Bello','Edad':55},
    {'Nombre':'Bob constructor','Ciudad':'Bogota','Edad':45},
    {'Nombre':'Marly Rastas','Ciudad':'Medellin','Edad':18},
     {'Nombre':'Estiliano Gallego','Ciudad':'Medellin','Edad':35},
    {'Nombre':'Rogelio parra','Ciudad':'Itagui','Edad':15},
    {'Nombre':'Armando casas','Ciudad':'Bello','Edad':55},
    {'Nombre':'Bob constructor','Ciudad':'Bogota','Edad':45},
    {'Nombre':'Marly Rastas','Ciudad':'Medellin','Edad':18},
     {'Nombre':'Estiliano Gallego','Ciudad':'Medellin','Edad':35},
    {'Nombre':'Rogelio parra','Ciudad':'Itagui','Edad':15},
    {'Nombre':'Armando casas','Ciudad':'Bello','Edad':55},
    {'Nombre':'Bob constructor','Ciudad':'Bogota','Edad':45},
    {'Nombre':'Marly Rastas','Ciudad':'Medellin','Edad':18},
     {'Nombre':'Estiliano Gallego','Ciudad':'Medellin','Edad':35},
    {'Nombre':'Rogelio parra','Ciudad':'Itagui','Edad':15},
    {'Nombre':'Armando casas','Ciudad':'Bello','Edad':55},
    {'Nombre':'Bob constructor','Ciudad':'Bogota','Edad':45},
    {'Nombre':'Marly Rastas','Ciudad':'Medellin','Edad':18},
     {'Nombre':'Estiliano Gallego','Ciudad':'Medellin','Edad':35},
    {'Nombre':'Rogelio parra','Ciudad':'Itagui','Edad':15},
    {'Nombre':'Armando casas','Ciudad':'Bello','Edad':55},
    {'Nombre':'Bob constructor','Ciudad':'Bogota','Edad':45},
    {'Nombre':'Marly Rastas','Ciudad':'Medellin','Edad':18},
     {'Nombre':'Estiliano Gallego','Ciudad':'Medellin','Edad':35},
    {'Nombre':'Rogelio parra','Ciudad':'Itagui','Edad':15},
    {'Nombre':'Armando casas','Ciudad':'Bello','Edad':55},
    {'Nombre':'Bob constructor','Ciudad':'Bogota','Edad':45},
    {'Nombre':'Marly Rastas','Ciudad':'Medellin','Edad':18},
     {'Nombre':'Estiliano Gallego','Ciudad':'Medellin','Edad':35},
    {'Nombre':'Rogelio parra','Ciudad':'Itagui','Edad':15},
    {'Nombre':'Armando casas','Ciudad':'Bello','Edad':55},
    {'Nombre':'Bob constructor','Ciudad':'Bogota','Edad':45},
    {'Nombre':'Marly Rastas','Ciudad':'Medellin','Edad':18},
     {'Nombre':'Estiliano Gallego','Ciudad':'Medellin','Edad':35},
    {'Nombre':'Rogelio parra','Ciudad':'Itagui','Edad':15},
    {'Nombre':'Armando casas','Ciudad':'Bello','Edad':55},
    {'Nombre':'Bob constructor','Ciudad':'Bogota','Edad':45},
    {'Nombre':'Marly Rastas','Ciudad':'Medellin','Edad':18},
     {'Nombre':'Estiliano Gallego','Ciudad':'Medellin','Edad':35},
    {'Nombre':'Rogelio parra','Ciudad':'Itagui','Edad':15},
    {'Nombre':'Armando casas','Ciudad':'Bello','Edad':55},
    {'Nombre':'Bob constructor','Ciudad':'Bogota','Edad':45},
    {'Nombre':'Marly Rastas','Ciudad':'Medellin','Edad':18},
     {'Nombre':'Estiliano Gallego','Ciudad':'Medellin','Edad':35},
    {'Nombre':'Rogelio parra','Ciudad':'Itagui','Edad':15},
    {'Nombre':'Armando casas','Ciudad':'Bello','Edad':55},
    {'Nombre':'Bob constructor','Ciudad':'Bogota','Edad':45},
    {'Nombre':'Marly Rastas','Ciudad':'Medellin','Edad':18},
     {'Nombre':'Estiliano Gallego','Ciudad':'Medellin','Edad':35},
    {'Nombre':'Rogelio parra','Ciudad':'Itagui','Edad':15},
    {'Nombre':'Armando casas','Ciudad':'Bello','Edad':55},
    {'Nombre':'Bob constructor','Ciudad':'Bogota','Edad':45},
    {'Nombre':'Marly Rastas','Ciudad':'Medellin','Edad':18},
     {'Nombre':'Estiliano Gallego','Ciudad':'Medellin','Edad':35},
    {'Nombre':'Rogelio parra','Ciudad':'Itagui','Edad':15},
    {'Nombre':'Armando casas','Ciudad':'Bello','Edad':55},
    {'Nombre':'Bob constructor','Ciudad':'Bogota','Edad':45},
    {'Nombre':'Marly Rastas','Ciudad':'Medellin','Edad':18},
     {'Nombre':'Estiliano Gallego','Ciudad':'Medellin','Edad':35},
    {'Nombre':'Rogelio parra','Ciudad':'Itagui','Edad':15},
    {'Nombre':'Armando casas','Ciudad':'Bello','Edad':55},
    {'Nombre':'Bob constructor','Ciudad':'Bogota','Edad':45},
    {'Nombre':'Marly Rastas','Ciudad':'Medellin','Edad':18},
     {'Nombre':'Estiliano Gallego','Ciudad':'Medellin','Edad':35},
    {'Nombre':'Rogelio parra','Ciudad':'Itagui','Edad':15},
    {'Nombre':'Armando casas','Ciudad':'Bello','Edad':55},
    {'Nombre':'Bob constructor','Ciudad':'Bogota','Edad':45},
    {'Nombre':'Marly Rastas','Ciudad':'Medellin','Edad':18},
     {'Nombre':'Estiliano Gallego','Ciudad':'Medellin','Edad':35},
    {'Nombre':'Rogelio parra','Ciudad':'Itagui','Edad':15},
    {'Nombre':'Armando casas','Ciudad':'Bello','Edad':55},
    {'Nombre':'Bob constructor','Ciudad':'Bogota','Edad':45},
    {'Nombre':'Marly Rastas','Ciudad':'Medellin','Edad':18},
     {'Nombre':'Estiliano Gallego','Ciudad':'Medellin','Edad':35},
    {'Nombre':'Rogelio parra','Ciudad':'Itagui','Edad':15},
    {'Nombre':'Armando casas','Ciudad':'Bello','Edad':55},
    {'Nombre':'Bob constructor','Ciudad':'Bogota','Edad':45},
    {'Nombre':'Marly Rastas','Ciudad':'Medellin','Edad':18},
     {'Nombre':'Estiliano Gallego','Ciudad':'Medellin','Edad':35},
    {'Nombre':'Rogelio parra','Ciudad':'Itagui','Edad':15},
    {'Nombre':'Armando casas','Ciudad':'Bello','Edad':55},
    {'Nombre':'Bob constructor','Ciudad':'Bogota','Edad':45},
    {'Nombre':'Marly Rastas','Ciudad':'Medellin','Edad':18}
    
]

#3. Se capturan los datos:
#Pandas utiliza una tabla tabulada que se llama DataFrame
datosOrdenados=pd.DataFrame(datos)

#print(datosOrdenados) 
#utilizando el head
#print(datosOrdenados.head(10))

#utilizando el tail
#print(datosOrdenados.tail())

#utilizando el info
#print(datosOrdenados.info())

#utilizando el describe
#print(datosOrdenados.describe())

#utilizando corchetes
#print(datosOrdenados[datosOrdenados['Edad']>=18])
#print(datosOrdenados['Nombre'])

#Elimina registros

#datosOrdenados.drop(0)
#print(datosOrdenados)

print(datosOrdenados.groupby('Ciudad').size())