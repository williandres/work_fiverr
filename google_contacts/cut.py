import csv
import os
from datetime import datetime
from dateutil import parser
"""
# Carpeta de origen que contiene los archivos CSV
carpeta_origen = "sources/contacts"

# Carpeta de destino para los archivos CSV separados
carpeta_destino = "sources/usa/"

archivos_de_origen = [os.path.join(carpeta_origen, archivo) for archivo in os.listdir(carpeta_origen) if archivo.endswith(".csv")]


print(archivos_de_origen)
print(len(archivos_de_origen))

"""

import os
import pandas as pd

# Ruta de la carpeta con los archivos CSV de entrada
carpeta_contactos = 'sources/contacts_fixed'

# Ruta de la carpeta para guardar los archivos divididos
carpeta_divididos = 'sources/contacts_final'

# Establece el número máximo de filas por archivo
filas_por_archivo = 3000

# Obtener la lista de archivos CSV en la carpeta de entrada
archivos_csv = [f for f in os.listdir(carpeta_contactos) if f.endswith('.csv')]


# Función para dividir un archivo CSV en archivos más pequeños
def dividir_csv(archivo):
    ruta_completa = os.path.join(carpeta_contactos, archivo)
    lector_csv = pd.read_csv(ruta_completa, iterator=True, chunksize=filas_por_archivo)
    i = 1

    for chunk in lector_csv:
        archivo_salida = os.path.join(carpeta_divididos, f'division_{i}_{archivo}')
        chunk.to_csv(archivo_salida, index=False)
        i += 1

# Procesar cada archivo CSV en la carpeta de entrada
for archivo_csv in archivos_csv:
    dividir_csv(archivo_csv)

print("División completa. Los archivos divididos se encuentran en la carpeta 'divided'.")



