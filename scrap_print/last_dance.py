import pandas as pd

# Cargar los archivos CSV en dataframes
df1 = pd.read_csv('final_compilation.csv')
df2 = pd.read_csv('compilacion.csv')

# Combina los DataFrames y elimina las filas duplicadas
combined_df = pd.concat([df1, df2]).drop_duplicates()

# Identifica las filas únicas de cada archivo
unique_df1 = df1[~df1.isin(df2.to_dict('list')).all(axis=1)]
unique_df2 = df2[~df2.isin(df1.to_dict('list')).all(axis=1)]

# Combina las filas únicas de cada DataFrame
unique_combined_df = pd.concat([unique_df1, unique_df2]).drop_duplicates()

# Guarda el resultado en un nuevo archivo CSV
unique_combined_df.to_csv('compilacion_final_2024_06_02.csv', index=False)

print("El archivo 'unique_combined.csv' ha sido creado con éxito.")
