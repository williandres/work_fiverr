import pandas as pd
import numpy as np
import os

# Crear la carpeta si no existe
output_folder = 'sources/breaked'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Leer el CSV
df = pd.read_csv('sources/Company_Purchases_291-964-262 - Company_Purchases_291-964-262.csv')

# Dividir y guardar
for i, g in df.groupby(np.arange(len(df)) // 5000):
    g.to_csv(f'{output_folder}/split_{i}.csv', index=False)

print("¡Archivos CSV generados con éxito!")
