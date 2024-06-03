import os
import csv

def merge_csv_files(folder_path, output_file):
    # Verificar si la carpeta existe
    if not os.path.exists(folder_path):
        print(f"La carpeta {folder_path} no existe.")
        return

    # Lista para almacenar todos los datos
    all_data = []

    # Iterar sobre los archivos en la carpeta
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.csv'):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'r', newline='', encoding='utf-8-sig') as csv_file:
                csv_reader = csv.reader(csv_file)
                # Saltar el encabezado si es el primer archivo
                next(csv_reader)
                for row in csv_reader:
                    all_data.append(row)

    # Escribir todos los datos en un solo archivo CSV
    with open(output_file, 'w', newline='', encoding='utf-8') as csv_output:
        csv_writer = csv.writer(csv_output)
        # Escribir el encabezado
        csv_writer.writerow(['First Name', 'Last Name', 'Street Address', 'City, State', 'ZIP', 'Phone'])
        # Escribir los datos
        csv_writer.writerows(all_data)

    print(f"Se han fusionado todos los archivos CSV en {output_file}.")

# Especifica la carpeta que contiene los archivos CSV y el nombre del archivo de salida
carpeta = 'csvs'
archivo_salida = 'compilacion.csv'

# Llama a la función para fusionar los archivos CSV
merge_csv_files(carpeta, archivo_salida)
