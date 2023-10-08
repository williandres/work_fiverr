import csv
import os
from datetime import datetime
from dateutil import parser
import io

csv.field_size_limit(10000000000000)

# Carpeta de origen que contiene los archivos CSV
carpeta_origen = "sources/shiet/"

# Carpeta de destino para los archivos CSV separados
carpeta_destino = "sources/usa/"

# Encabezado deseado para los archivos de destino
encabezado = [
    "Name", "Given Name", "Additional Name", "Family Name", "Yomi Name",
    "Given Name Yomi", "Additional Name Yomi", "Family Name Yomi",
    "Name Prefix", "Name Suffix", "Initials", "Nickname", "Short Name",
    "Maiden Name", "Birthday", "Gender", "Location", "Billing Information",
    "Directory Server", "Mileage", "Occupation", "Hobby", "Sensitivity",
    "Priority", "Subject", "Notes", "Language", "Photo", "Group Membership",
    "E-mail 1 - Type", "E-mail 1 - Value", "Phone 1 - Type", "Phone 1 - Value",
    "Phone 2 - Type", "Phone 2 - Value", "Address 1 - Type", "Address 1 - Formatted",
    "Address 1 - Street", "Address 1 - City", "Address 1 - PO Box",
    "Address 1 - Region", "Address 1 - Postal Code", "Address 1 - Country",
    "Address 1 - Extended Address", "Organization 1 - Type", "Organization 1 - Name",
    "Organization 1 - Yomi Name", "Organization 1 - Title", "Organization 1 - Department",
    "Organization 1 - Symbol", "Organization 1 - Location", "Organization 1 - Job Description"
]




# Función para limpiar caracteres nulos de una línea
def limpiar_caracteres_nulos(line):
    return line.replace('\x00', '')

# Función para leer un archivo CSV y agregar filas al archivo destino
def agregar_filas_desde_csv(origen_csv, destino_csv, limite_filas=11000):
    codificaciones = ['utf-8', 'latin-1', 'utf-16']
    for codificacion in codificaciones:
        try:
            with open(origen_csv, mode='r', newline='', encoding=codificacion) as origen_file:
                # Leer el contenido del archivo y limpiar caracteres nulos
                contenido = limpiar_caracteres_nulos(origen_file.read())
                # Crear un objeto StringIO para tratar el contenido como un archivo
                contenido_csv = io.StringIO(contenido)
                reader = csv.reader(contenido_csv)

                # Inicializar contadores
                fila_actual = 0
                archivo_destino_numero = 1

                # Crear un conjunto para rastrear filas duplicadas
                filas_duplicadas = set()

                # Crear un nuevo archivo de destino
                destino_csv_actual = os.path.join(carpeta_destino, f'contacts{origen_csv[-7:]}_{archivo_destino_numero}.csv')
                with open(destino_csv_actual, mode='w', newline='', encoding='utf-8') as destino_file:
                    writer = csv.writer(destino_file)
                    writer.writerow(encabezado)

                while True:
                    # Leer la siguiente fila del archivo origen
                    try:
                        row = next(reader)
                    except StopIteration:
                        # Se llegó al final del archivo origen
                        break

                    # Verificar si la fila es duplicada
                    fila_como_cadena = ",".join(row)
                    if fila_como_cadena in filas_duplicadas:
                        continue  # Saltar fila duplicada

                    # Añadir filas al archivo destino actual
                    with open(destino_csv_actual, mode='a', newline='', encoding='utf-8') as destino_file:
                        writer = csv.writer(destino_file)
                        if len(row) == 18:
                            try:
                                parser.parse(row[12])
                                date = row[12]
                            except:
                                date = None

                            fix = [row[1] + " " + row[2],
                                   row[1],
                                   None,
                                   row[2],
                                   None, None, None, None, None, None, None, None, None, None,
                                   date,
                                   row[11],
                                   None,  None,  None, None,  None,  None, None,  None,  None, None,  None,  None, None,
                                   "* Home",
                                   row[0],
                                   "Mobile",
                                   row[10],
                                   None, None,
                                   "Home",
                                   row[3] + " " + row[4] + " " + row[5] + ", " + row[6] + " " + row[8],
                                   row[3],
                                   row[4],
                                   None,
                                   row[5],
                                   row[8],
                                   row[7],
                                   None, None, None, None, None, None, None, None, None
                                   ]

                            writer.writerow(fix)
                            fila_actual += 1
                            filas_duplicadas.add(fila_como_cadena)

                    # Crear un nuevo archivo de destino si se alcanza el límite de filas
                    if fila_actual % limite_filas == 0:
                        archivo_destino_numero += 1
                        destino_csv_actual = os.path.join(carpeta_destino, f'contacts{origen_csv[-7:]}_{archivo_destino_numero}.csv')
                        with open(destino_csv_actual, mode='w', newline='', encoding='utf-8') as destino_file:
                            writer = csv.writer(destino_file)
                            writer.writerow(encabezado)
                    
                break  # Salir del bucle si la codificación funciona
        except UnicodeDecodeError:
            print(f"No se pudo abrir '{origen_csv}' con la codificación '{codificacion}'.")






# Listar todos los archivos CSV en la carpeta de origen
archivos_de_origen = [os.path.join(carpeta_origen, archivo) for archivo in os.listdir(carpeta_origen) if archivo.endswith(".csv")]

# Agregar filas de todos los archivos de origen a los archivos de destino
for archivo_origen in archivos_de_origen:
    print(archivo_origen)
    agregar_filas_desde_csv(archivo_origen, carpeta_destino)

