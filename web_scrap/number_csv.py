import pandas as pd

# Definir el archivo de origen y el archivo de destino
input_file = 'archivo_combinado.csv'
output_file = 'archivo_filtrado.csv'

# Leer el archivo CSV de origen
df = pd.read_csv(input_file)

# Asegurarse de que la columna 'Phone' no contenga valores nulos antes de aplicar el filtro
df = df.dropna(subset=['Phone'])

# Filtrar las filas donde la columna 'Phone' comienza con '('
filtered_df = df[df['Phone'].str.startswith('(')]

# Guardar el dataframe filtrado en un nuevo archivo CSV
filtered_df.to_csv(output_file, index=False)

print(f"Filtrado completado. El archivo resultante se ha guardado como {output_file}.")
