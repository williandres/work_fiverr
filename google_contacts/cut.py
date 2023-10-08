import csv
import os
from datetime import datetime
from dateutil import parser

# Carpeta de origen que contiene los archivos CSV
carpeta_origen = "sources/shiet/"

# Carpeta de destino para los archivos CSV separados
carpeta_destino = "sources/usa/"

archivos_de_origen = [os.path.join(carpeta_origen, archivo) for archivo in os.listdir(carpeta_origen) if archivo.endswith(".csv")]


print(archivos_de_origen)
print(len(archivos_de_origen))

"""
import pandas as pd

# Establece el número máximo de filas por archivo
filas_por_archivo = 10000

# Abre el archivo CSV original y crea un lector CSV
with open('sources/contacts.csv', 'r') as archivo_original:
    lector_csv = pd.read_csv(archivo_original, iterator=True, chunksize=filas_por_archivo)
    i = 1

    for chunk in lector_csv:
        archivo_salida = f'sources/results/division_{i}.csv'
        chunk.to_csv(archivo_salida, index=False)
        i += 1

print("División completa.")
"""

