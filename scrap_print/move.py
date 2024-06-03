import os
import shutil

# Definir las rutas de la carpeta de origen y destino
source_folder = '/home/willian/Repositories/work_fiverr/scrap_print/temp'
destination_folder = '/home/willian/Repositories/work_fiverr/scrap_print/txts'

# Crear la carpeta de destino si no existe
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Obtener la lista de archivos en la carpeta de origen
files = os.listdir(source_folder)

# Mover cada archivo a la carpeta de destino
for filename in files:
    source_path = os.path.join(source_folder, filename)
    destination_path = os.path.join(destination_folder, filename)
    
    # Mover el archivo
    shutil.move(source_path, destination_path)

print("Todos los archivos han sido movidos.")
