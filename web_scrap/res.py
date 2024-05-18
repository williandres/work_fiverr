import pandas as pd

# Definir el archivo de origen y el archivo de destino
input_file = '/home/willian/Repositories/work_fiverr/web_scrap/sources/clients.csv'
output_file = 'compiled2.csv'

# Leer el archivo CSV de origen
df = pd.read_csv(input_file)

# Crear la columna 'Street Address' combinando las columnas relevantes
df['Street Address'] = df['House Number'].astype(str).fillna('') + ' ' + \
                       df['Pre-directional'].fillna('') + ' ' + \
                       df['Street'].fillna('') + ' ' + \
                       df['Street Suffix'].fillna('') + ' ' + \
                       df['Post-directional'].fillna('') + ' ' + \
                       df['Apartment Number'].fillna('')

# Limpiar espacios extra en 'Street Address'
df['Street Address'] = df['Street Address'].str.replace(r'\s+', ' ', regex=True).str.strip()

# Crear la columna 'City-State' combinando 'City' y 'State'
df['City-State'] = df['City'].fillna('') + ',' + df['State'].fillna('')

# Seleccionar las columnas deseadas y renombrarlas
columns_to_keep = {
    'First Name': 'First Name',
    'Last Name': 'Last Name',
    'Street Address': 'Street Address',
    'City-State': 'City-State',
    'Zip Code': 'Zip',
    'Phone Number': 'Phone'
}

filtered_df = df[list(columns_to_keep.keys())].rename(columns=columns_to_keep)

# Guardar el dataframe recortado en un nuevo archivo CSV
filtered_df.to_csv(output_file, index=False)

print(f"Archivo recortado creado exitosamente como {output_file}.")
