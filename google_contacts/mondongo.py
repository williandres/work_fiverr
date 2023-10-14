import os
import shutil
import csv

# Directorio donde se encuentran los archivos CSV originales
input_directory = "sources/contacts_final"

# Directorio donde se guardarán los archivos duplicados
output_directory = "sources/emails_duplicate"

# Obtener la lista de archivos CSV en el directorio de entrada
csv_files = [file for file in os.listdir(input_directory) if file.endswith(".csv")]

# Iterar a través de los archivos CSV en el directorio de entrada
for csv_file in csv_files:
    # Ruta completa del archivo de entrada
    input_file = os.path.join(input_directory, csv_file)

    # Ruta completa del archivo de salida (duplicado)
    output_file = os.path.join(output_directory, csv_file)

    # Duplicar el archivo
    shutil.copy(input_file, output_file)

    # Procesar el archivo duplicado
    with open(output_file, mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    # Eliminar la primera columna y agregar comillas dobles al principio y al final
    for i in range(len(rows)):
        row = rows[i]
        row.pop(0)  # Eliminar la primera columna
        # Agregar comillas dobles al principio y al final
        rows[i] = [cell.strip() + ',' for cell in row]

    # Guardar el archivo procesado
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

print("Archivos duplicados con éxito, primera columna eliminada y formato modificado.")


