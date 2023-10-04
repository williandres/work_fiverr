import pandas as pd
import os

# Directorio que contiene los archivos CSV traducidos
translated_directory = 'trasnlated'

# Obtener la lista de archivos CSV en el directorio
csv_files = [filename for filename in os.listdir(translated_directory) if filename.endswith('.csv')]

# Crear una lista para almacenar los DataFrames de cada archivo
data_frames = []

# Leer cada archivo CSV y agregarlo a la lista
for filename in sorted(csv_files):
    file_path = os.path.join(translated_directory, filename)
    df = pd.read_csv(file_path)
    data_frames.append(df)

# Combinar los DataFrames verticalmente (concatenarlos)
combined_df = pd.concat(data_frames, ignore_index=True)


# Guardar el DataFrame combinado en un archivo CSV único
output_file_path = 'combined.csv'
combined_df.to_csv(output_file_path, index=False)

print(f'Todos los archivos CSV han sido unificados en "{output_file_path}".')
