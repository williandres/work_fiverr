import os
import pandas as pd

def concat_csvs(input_folder, output_file):
    # Lista para almacenar los DataFrames de cada archivo CSV
    all_data = []

    # Recorre todos los archivos en la carpeta de entrada
    for filename in os.listdir(input_folder):
        if filename.endswith('.csv'):
            file_path = os.path.join(input_folder, filename)
            # Lee el archivo CSV
            df = pd.read_csv(file_path)
            # Filtra las filas donde el "Phone Number" no sea "Not Available"
            df_filtered = df[df['Phone Number'] != 'Not Available']
            # Añade el DataFrame filtrado a la lista
            all_data.append(df_filtered)
    
    # Concatena todos los DataFrames en uno solo
    concatenated_df = pd.concat(all_data, ignore_index=True)
    # Guarda el DataFrame concatenado en el archivo de salida
    concatenated_df.to_csv(output_file, index=False)

if __name__ == "__main__":
    input_folder = 'sources/datos_crudos_manual'  # Cambia esto por la ruta a tu carpeta
    output_file = '/home/willian/Repositories/work_fiverr/web_scrap/sources/clients.csv'    # Cambia esto por la ruta y nombre de tu archivo de salida
    concat_csvs(input_folder, output_file)
