import pandas as pd
import os

# Definir el orden personalizado de los tipos de proveedores
provider_order = {
    'Primary Care Provider': 0,
    'Specialist Provider': 1,
    'Ancillary Provider': 2,
    'Pharmacy': 3,
    'Vision Provider': 4
}


# Crear una función para ordenar los datos
def sort_data(file_path):
    # Leer el archivo CSV en un DataFrame
    df = pd.read_csv(file_path)

    # Ordenar por COUNTY, PROVIDER TYPE y SPECIALTY
    df.sort_values(by=['ProviderType', 'Specialty'], inplace=True)

    # Aplicar el orden personalizado a PROVIDER TYPE
    df['Provider Type Order'] = df['ProviderType'].map(provider_order)
    df.sort_values(by=['Provider Type Order', 'Specialty'], inplace=True)


    # Guardar el DataFrame ordenado en un nuevo archivo CSV
    output_file_path = os.path.join('sorted', os.path.basename(file_path))
    df.to_csv(output_file_path, index=False)

# Directorio que contiene los archivos CSV
directory = 'sources'

# Crear un directorio para los archivos ordenados
os.makedirs('sorted', exist_ok=True)

# Recorrer los archivos CSV en el directorio
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        file_path = os.path.join(directory, filename)
        sort_data(file_path)

print('Archivos ordenados y guardados en el directorio "sorted".')
