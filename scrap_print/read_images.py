import os
from PIL import Image
import shutil
import pytesseract

# Configuración personalizada para Tesseract
custom_config = r'--oem 3 --psm 6'

# Ruta de la carpeta con las imágenes
input_folder = 'sources/10075-17041 (imgs)'

# Ruta de la carpeta donde se guardarán los resultados
output_folder = 'temp'

# Obtener la lista de archivos .png en la carpeta de entrada
files = [f for f in os.listdir(input_folder) if f.endswith('.png')]
total_files = len(files)
processed_files = 0
errores = []
source_folder = 'sources/10075-17041 (imgs)'
destination_folder = 'backup/10075-17041 (imgs)b'

# Crear la carpeta de salida si no existe
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Procesar cada imagen en la carpeta de entrada
for filename in os.listdir(input_folder):
    if filename.endswith('.png'):
        # Ruta completa de la imagen
        image_path = os.path.join(input_folder, filename)
        
        # Abrir la imagen
        screenshot = Image.open(image_path)

        # Usar Tesseract para extraer el texto con la configuración personalizada
        text = pytesseract.image_to_string(screenshot, config=custom_config, lang='eng')
        
        # Nombre base de la imagen (sin extensión)
        base_name = os.path.splitext(filename)[0]
        
        
        # Ruta completa del archivo de texto de salida
        output_text_path = os.path.join(output_folder, f'{base_name}.txt')
        
        # Guardar el texto en un archivo .txt
        with open(output_text_path, 'w', encoding='utf-8') as file:
            file.write(text)

        # Contar las líneas del archivo de texto
        line_count = text.count('\n') + 1
        
        # Verificar si el archivo tiene menos de 25 líneas o más de 26 líneas
        if line_count < 25 or line_count > 26:
            print(f"El archivo {output_text_path} tiene {line_count} líneas.")
            errores.append(output_text_path)
        # Mover el archivo
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)

        shutil.move(source_path, destination_path)
        # Actualizar y mostrar el conteo de archivos procesados
        processed_files += 1
        print(f"Archivos procesados: {processed_files}/{total_files}")

print("Proceso completado.")
print(errores)
print('Numero de errores: ' + str(len(errores)))