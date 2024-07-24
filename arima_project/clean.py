import os# Proporciona funciones para interactuar con el sistema de archivos.
import pandas as pd# Biblioteca para manipulación y análisis de datos, especialmente series temporales y tablas de datos.
import numpy as np# Biblioteca para operaciones numéricas y manejo de matrices.


# Función para comparar dos DataFrames y generar un resumen
def compare_dataframes(df_raw, df_cleaned):
    comparison = {}

    # Comparar número de filas y columnas
    comparison['num_rows_raw'] = df_raw.shape[0]
    comparison['num_rows_cleaned'] = df_cleaned.shape[0]
    comparison['num_columns_raw'] = df_raw.shape[1]
    comparison['num_columns_cleaned'] = df_cleaned.shape[1]

    # Comparar nombres de las columnas
    comparison['columns_raw'] = df_raw.columns.tolist()
    comparison['columns_cleaned'] = df_cleaned.columns.tolist()

    # Comparar estadísticas descriptivas para columnas numéricas
    comparison['stats_raw'] = df_raw.describe().to_dict()
    comparison['stats_cleaned'] = df_cleaned.describe().to_dict()

    return comparison

# Funcion para elaborar un diagnostico sobre los archivos
def comparison():
    # Ruta de las carpetas con los archivos CSV
    raw_folder = 'sources' # CSV'S Originales
    cleaned_folder = 'sources/cleaned'# CSV'S Limpios

    # Listar archivos CSV en ambas carpetas
    raw_files = [f for f in os.listdir(raw_folder) if f.endswith('.csv')]
    cleaned_files = [f for f in os.listdir(cleaned_folder) if f.endswith('.csv')]


    # Comparar archivos equivalentes
    comparisons = {}

    for raw_file in raw_files:
        cleaned_file = raw_file
        if cleaned_file in cleaned_files:
            raw_filepath = os.path.join(raw_folder, raw_file)
            cleaned_filepath = os.path.join(cleaned_folder, cleaned_file)

            # Leer los archivos CSV
            df_raw = read_csv_with_different_delimiters(raw_filepath)
            df_cleaned = pd.read_csv(cleaned_filepath)

            # Generar comparación
            comparisons[raw_file] = compare_dataframes(df_raw, df_cleaned)

    # Imprimir resumen de comparación
    for filename, comparison in comparisons.items():
        print(f"Comparación para {filename}:")
        print(f" - Número de filas (bruto): {comparison['num_rows_raw']}")
        print(f" - Número de filas (limpio): {comparison['num_rows_cleaned']}")
        print(f" - Número de columnas (bruto): {comparison['num_columns_raw']}")
        print(f" - Número de columnas (limpio): {comparison['num_columns_cleaned']}")
        print(f" - Columnas (bruto): {comparison['columns_raw']}")
        print(f" - Columnas (limpio): {comparison['columns_cleaned']}")
        print(f" - Estadísticas descriptivas (bruto): {comparison['stats_raw']}")
        print(f" - Estadísticas descriptivas (limpio): {comparison['stats_cleaned']}")
        print("\n")


# Función para limpiar los datos
def clean_data(df):
    # Rellenar valores faltantes:
    # Para columnas numéricas, se rellenan los valores faltantes con la mediana de la columna,
    # lo cual es robusto a outliers y representa mejor el centro de los datos.
    df.fillna(df.median(numeric_only=True), inplace=True)

    # Para columnas no numéricas (categóricas), se rellenan los valores faltantes con 'NaN',
    # indicando que el valor es desconocido.
    df.fillna('NaN', inplace=True)

    # Manejar outliers (valores atípicos) usando el principio estadístico del rango intercuartílico (IQR),
    # donde los valores menores que Q1 - 1.5*IQR y mayores que Q3 + 1.5*IQR son considerados atípicos.
    for column in df.select_dtypes(include=[np.number]).columns:
        q1 = df[column].quantile(0.25)
        q3 = df[column].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        df[column] = np.where(df[column] < lower_bound, lower_bound, df[column])
        df[column] = np.where(df[column] > upper_bound, upper_bound, df[column])


    return df

# Función para intentar leer un archivo CSV con diferentes delimitadores y codificadores
def read_csv_with_different_delimiters(filepath):
    # Lista de posibles codificaciones de caracteres
    encodings = ['utf-8', 'latin1', 'ISO-8859-1']
    # Lista de posibles delimitadores
    delimiters = [',', '.',';', '\t', '|']

    # Intentar diferentes codificaciones
    for encoding in encodings:
        try:
            # Intentar diferentes delimitadores dentro de la codificación actual
            for delimiter in delimiters:
                # Intentar leer el archivo con la combinación actual de codificación y delimitador
                try:
                    # Lectura especial para los casos de Nacimientos y Tasa
                    if filepath.split('/')[-1][:4] == 'Naci' or filepath.split('/')[-1][:4] == 'Tasa':
                        df = pd.read_csv(filepath, delimiter=';', encoding=encoding)
                        return df
                    # Caso estandar
                    else:
                        df = pd.read_csv(filepath, delimiter=delimiter, encoding=encoding)
                        return df  # Retorna el DataFrame si se puede leer exitosamente
                except pd.errors.ParserError:
                    # Si ocurre un error de parseo, intentar con el siguiente delimitador
                    continue
        except UnicodeDecodeError:
            # Si ocurre un error de codificación, intentar con la siguiente codificación
            continue


def main():
    # Ruta de la carpeta con los archivos CSV
    input_folder = 'sources'
    output_folder = 'sources/cleaned'

    # Procesar cada archivo CSV en la carpeta 'input'
    for filename in os.listdir(input_folder):
        if filename.endswith('.csv'):

            filepath = os.path.join(input_folder, filename)
            df = read_csv_with_different_delimiters(filepath) # Intentar leer el archivo CSV con diferentes delimitadores y codificadores
            df_cleaned = clean_data(df)# Limpiar los datos llamando la funcion

            # Guardar el archivo limpio en la carpeta de salida
            output_filepath = os.path.join(output_folder, filename)
            df_cleaned.to_csv(output_filepath, index=False)



if __name__ == '__main__':# Permite que el código se ejecute solo si el script es ejecutado directamente, no si es importado como un módulo.
    main()
    comparison()