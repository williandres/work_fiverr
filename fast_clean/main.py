import pandas as pd
import csv
import re

# Leer el archivo de Excel con múltiples hojas
archivo_excel = "sources/scool.xlsx"
xls = pd.ExcelFile(archivo_excel)

# Leer la primera hoja "OGC"
ogc_data = xls.parse("OGC", usecols="B", header=None, skiprows=1, nrows=45).iloc[:, 0].str.rstrip(',').tolist()


# Leer la segunda hoja "esemble" y dividir la cadena por ";"
esemble_df = pd.read_excel(xls, "ensemble", header=None, usecols="B", skiprows=1)
esemble_data = esemble_df.iloc[0, 0].split(";")

# Leer la tercera hoja "track" y dividir la cadena por ";"
track_df = pd.read_excel(xls, "track", header=None, usecols="B", skiprows=1)
track_data = track_df.iloc[0, 0].split(";")

# Leer la cuarta hoja "cheer" y dividir la cadena por ";"
cheer_df = pd.read_excel(xls, "cheer", header=None, usecols="B", skiprows=1)
cheer_data = cheer_df.iloc[0, 0].split(";")

all_data = ogc_data + esemble_data + track_data + cheer_data

#Csv Shit
# Crear una lista para almacenar los datos procesados
csv_data = []

# Procesar cada elemento de la lista all_data
for item in all_data:
    # Utilizar una expresión regular para extraer el nombre y el correo
    match = re.match(r'^(.*?) <(.*?)>$', item)
    if match:
        full_name = match.group(1).strip()
        correo = match.group(2)
        if ' ' in full_name:
            first_name, last_name = full_name.split(' ', 1)
        else:
            first_name = full_name
            last_name = ""
        csv_data.append([first_name, last_name, correo])
    else:
        csv_data.append(["", "", item])  # Si no se encuentra el patrón, colocar el valor completo en "Email"

# Nombre del archivo CSV de salida
csv_file = "sources/output.csv"

# Escribir los datos en un archivo CSV
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    # Escribir el encabezado
    writer.writerow(["First Name", "Last Name", "Email"])
    # Escribir los datos
    writer.writerows(csv_data)