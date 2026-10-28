import numpy as np
import pandas as pd
# Pedro Martinez 0093
# Datos matriz (4 x 3)
datos_alumno = [
    [100, 80, 10],
    [90, 70, 7],  
    [120, 100, 14],
    [80, 50, 2]
]

# poner nombre a las columnas
# y almacenar la tabla en la variable df dataframe
print("\n datos a partir de una matriz 4 x 3")
df = pd.DataFrame(datos_alumno, columns=["ci", "marcas", "paquetes"])
print(df)
# datos a partir de un diccionario
print("---datos a partir de un diccionario----")
alumno_diccionarios = {
    "Nombre":["Eliseo","Joel","Pedro","Nicole","Dilan","Jesse"],
    "califa":[60,90,100,80,70,50],  
    "edad" : [64,15,16,16,18,14],    
}
estudiantes = pd.DataFrame(alumno_diccionarios)

print(estudiantes)

print("Pedro Martinez 0093")