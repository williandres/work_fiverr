import pandas as pd
import os

# Directorio que contiene los archivos CSV
directory = 'sources/1-513 (csv not cleaned)'

# Lista para almacenar los DataFrames
dfs = []

# Leer todos los archivos CSV en la carpeta
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        file_path = os.path.join(directory, filename)
        df = pd.read_csv(file_path)
        dfs.append(df)

# Concatenar todos los DataFrames en uno solo
all_data = pd.concat(dfs, ignore_index=True)

# Crear la columna "Street Address"
all_data['Street Address'] = (
    all_data['House Number'].astype(str) + ' ' +
    all_data['Pre-directional'].fillna('') + ' ' +
    all_data['Street'] + ' ' +
    all_data['Street Suffix'] + ' ' +
    all_data['Post-directional'].fillna('') + ' ' +
    all_data['Apartment Number'].fillna('')
).str.replace(' +', ' ')

# Crear la columna "City, State"
all_data['City, State'] = all_data['City'] + ', ' + all_data['State']

# Seleccionar las columnas necesarias
reduced_data = all_data[['First Name', 'Last Name', 'Street Address', 'City, State', 'Zip Code', 'Phone Number']]

# Renombrar las columnas
reduced_data.columns = ['First Name', 'Last Name', 'Street Address', 'City, State', 'ZIP', 'Phone']

# Filtrar las filas donde "Phone" es distinto a 'Not Available'
final_data = reduced_data[reduced_data['Phone'] != 'Not Available']

# Guardar el DataFrame resultante en un nuevo archivo CSV
final_data.to_csv('manual.csv', index=False)
