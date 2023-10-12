import os
import pandas as pd
import csv

# Ruta de la carpeta de entrada y salida
carpeta_entrada = 'sources/contacts_final'
carpeta_salida = 'sources/contacts_final2'

# Lista de correos a añadir
correos_a_anadir = ['hollis26@hotmail.com,', 'hollisamyamy@hotmail.com,', 'hollisterd@yahoo.com,']

# Recorremos todos los archivos CSV en la carpeta de entrada
for archivo in os.listdir(carpeta_entrada):
    if archivo.endswith(".csv"):
        # Ruta completa del archivo de entrada
        archivo_entrada = os.path.join(carpeta_entrada, archivo)

        # Ruta completa del archivo de salida
        archivo_salida = os.path.join(carpeta_salida, archivo)

        with open(archivo_entrada, 'r', newline='') as f_entrada, open(archivo_salida, 'w', newline='') as f_salida:
            reader = csv.reader(f_entrada)
            writer = csv.writer(f_salida)

            # Copiamos las filas del archivo original al archivo de salida
            for row in reader:
                writer.writerow(row)

            # Añadimos las filas de correo especificadas al archivo de salida
            for correo in correos_a_anadir:
                f_salida.write(correo + '\n')
