import os
import pandas as pd

# Ruta de la carpeta con los archivos CSV
carpeta_contactos = 'sources/contacts'
carpeta_destino = 'sources/contacts_fixed'

# Obtener la lista de archivos CSV en la carpeta
archivos_csv = [f for f in os.listdir(carpeta_contactos) if f.endswith('.csv')]

# Función para procesar un archivo CSV
def procesar_csv(archivo):
    ruta_completa = os.path.join(carpeta_contactos, archivo)
    df = pd.read_csv(ruta_completa)

    # Verificar si las columnas 'Name' y 'E-mail 1 - Value' existen en el CSV
    if 'Name' in df.columns and 'E-mail 1 - Value' in df.columns:
        # Renombrar las columnas
        df.rename(columns={'Name': 'Name', 'E-mail 1 - Value': 'Email'}, inplace=True)
        df = df[['Name', 'Email']]

        # Eliminar filas donde tanto 'Nombre' como 'Email' están vacíos
        df.dropna(subset=['Name', 'Email'], how='all', inplace=True)

        # Si 'Nombre' está vacío pero 'Email' tiene valor, reemplazar 'Nombre' con un valor falso
        df.loc[df['Name'].str.strip() == '', 'Name'] = 'Sin Nombre'

        # Guardar el DataFrame modificado en un nuevo archivo CSV
        df.to_csv(os.path.join(carpeta_destino, archivo), index=False)

# Procesar cada archivo CSV en la carpeta
for archivo_csv in archivos_csv:
    print(archivo_csv)
    procesar_csv(archivo_csv)

print("Proceso completado.")
