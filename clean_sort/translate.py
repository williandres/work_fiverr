import pandas as pd
import os

# Cargar el archivo CSV de traducciones
translation_file_path = 'trans.csv'
translation_df = pd.read_csv(translation_file_path)

# Restablecer el índice para asegurarse de que sea único
translation_df = translation_df.drop_duplicates(subset='English').set_index('English')

# Crear una función para agregar las traducciones a las especialidades
def add_translation(file_path):
    # Leer el archivo CSV ordenado en un DataFrame
    df = pd.read_csv(file_path)

    # Buscar las traducciones en el DataFrame de traducciones
    df['Spanish_Specialty'] = df['Specialty'].map(translation_df['Spanish'])

    # Concatenar la traducción en español con la especialidad en inglés
    df['Specialty'] = df.apply(lambda row: f"{row['Specialty']} / {row['Spanish_Specialty']}" if not pd.isnull(row['Spanish_Specialty']) else row['Specialty'], axis=1)

    # Eliminar la columna temporal 'Spanish_Specialty'
    df.drop(columns=['Spanish_Specialty'], inplace=True)

    # Guardar el DataFrame actualizado en un nuevo archivo CSV
    output_file_path = os.path.join('translated', os.path.basename(file_path))
    df.to_csv(output_file_path, index=False)

# Directorio que contiene los archivos CSV ordenados
sorted_directory = 'sorted'

# Crear un directorio para los archivos traducidos
os.makedirs('translated', exist_ok=True)

# Recorrer los archivos CSV ordenados en la carpeta "sorted"
for filename in os.listdir(sorted_directory):
    if filename.endswith('.csv'):
        file_path = os.path.join(sorted_directory, filename)
        add_translation(file_path)

print('Archivos traducidos y guardados en el directorio "translated".')