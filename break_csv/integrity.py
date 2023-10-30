import pandas as pd
import numpy as np
import os

def verify_csv_integrity(original_file, output_folder):
    # Leer el archivo original
    original_df = pd.read_csv(original_file)
    
    # Obtener la lista de archivos en la carpeta de salida
    split_files = [f for f in os.listdir(output_folder) if f.endswith('.csv')]
    
    # Verificar que la cantidad de archivos es coherente con la división esperada
    expected_files = np.ceil(len(original_df) / 5000)
    if len(split_files) != expected_files:
        print(f"Error: Se esperaban {expected_files} archivos, pero se encontraron {len(split_files)}")
        return
    
    total_rows = 0
    
    # Verificar cada archivo dividido
    for i, file in enumerate(sorted(split_files)):
        df = pd.read_csv(os.path.join(output_folder, file))
        
        # Para todos los archivos excepto el último, deberían tener 5000 filas
        if i != len(split_files) - 1 and len(df) != 5000:
            print(f"Error: Se esperaban 5000 filas en {file} pero se encontraron {len(df)}")
            return
        total_rows += len(df)
        
        # Verificar que los datos coincidan con el archivo original
        start_index = i * 5000
        end_index = start_index + len(df)
        if not original_df.iloc[start_index:end_index].equals(df):
            print(f"Error: Los datos en {file} no coinciden con el archivo original.")
            return
    
    # Verificar que la suma total de las filas de todos los archivos divididos sea igual al archivo original
    if total_rows != len(original_df):
        print(f"Error: Se esperaban {len(original_df)} filas en total, pero se encontraron {total_rows}")
        return
    
    print("Todos los archivos CSV son consistentes con el archivo original.")

# Usar la función
original_file = 'sources/Company_Purchases_291-964-262 - Company_Purchases_291-964-262.csv'
output_folder = 'sources/breaked'
verify_csv_integrity(original_file, output_folder)
