import os
import shutil

# Define las rutas de las carpetas de origen y la carpeta de destino
source_dirs = ['sources/csvs_ia', 'sources/csvs_ia2', 'sources/csvs_ia3', 'sources/csvs_ia4']
destination_dir = '/home/willian/Repositories/work_fiverr/web_scrap/sources/csv'

# Crea la carpeta de destino si no existe
if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)

# Inicializa un contador para renombrar los archivos
file_counter = 1

# Recorre cada carpeta de origen
for source_dir in source_dirs:
    # Recorre cada archivo en la carpeta de origen
    for filename in os.listdir(source_dir):
        # Define la ruta completa del archivo origen
        file_path = os.path.join(source_dir, filename)
        
        # Solo mover si es un archivo (omitir directorios)
        if os.path.isfile(file_path):
            # Define el nuevo nombre del archivo en la carpeta de destino
            new_filename = f"archivo_{file_counter}{os.path.splitext(filename)[1]}"
            destination_path = os.path.join(destination_dir, new_filename)
            
            # Mueve el archivo a la carpeta de destino con el nuevo nombre
            shutil.move(file_path, destination_path)
            
            # Incrementa el contador de archivos
            file_counter += 1

print("Archivos movidos y renombrados exitosamente.")
