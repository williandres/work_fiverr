import pandas as pd

# Definir los archivos de origen y el archivo de destino
input_file1 = 'sources/compiled1.csv'
input_file2 = 'sources/compiled2.csv'
output_file = 'sources/final_compilation.csv'

# Leer los archivos CSV de origen
df1 = pd.read_csv(input_file1)
df2 = pd.read_csv(input_file2)

# Unir los dataframes
combined_df = pd.concat([df1, df2], ignore_index=True)

# Guardar el dataframe combinado en un nuevo archivo CSV
combined_df.to_csv(output_file, index=False)

print(f"Archivos combinados exitosamente en {output_file}.")
