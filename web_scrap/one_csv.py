import os
import pandas as pd

# Definir la carpeta de origen y el archivo de destino
source_dir = 'sources/csv'
output_file = 'archivo_combinado.csv'

# Definir el encabezado deseado
header = ['First Name', 'Last Name', 'Street Address', 'City-State', 'Zip', 'Phone']

# Lista para almacenar los dataframes
dataframes = []

# Recorrer todos los archivos en la carpeta de origen
for filename in os.listdir(source_dir):
    # Verificar si el archivo es un CSV
    if filename.endswith('.csv'):
        file_path = os.path.join(source_dir, filename)
        
        try:
            # Leer el archivo CSV sin encabezado
            df = pd.read_csv(file_path, header=None)
            
            # Solo añadir el dataframe a la lista si no está vacío
            if not df.empty:
                dataframes.append(df)
        except pd.errors.EmptyDataError:
            print(f"El archivo {file_path} está vacío y será omitido.")
        except Exception as e:
            print(f"Ocurrió un error al leer el archivo {file_path}: {e}")

# Concatenar todos los dataframes en uno solo, si hay dataframes válidos
if dataframes:
    combined_df = pd.concat(dataframes, ignore_index=True)

    # Asignar el encabezado al dataframe combinado
    combined_df.columns = header

    # Guardar el dataframe combinado en un archivo CSV
    combined_df.to_csv(output_file, index=False)

    print("Archivos CSV combinados exitosamente en", output_file)
else:
    print("No se encontraron archivos CSV válidos para combinar.")
