import pandas as pd

archivo_csv = "sources/Main_data.csv"
######################
codificaciones = ["utf-8", "latin-1", "iso-8859-1", "windows-1252"]

for codificacion in codificaciones:
    print(codificacion)
    try:
        with open(archivo_csv, "r", encoding=codificacion) as file:
            lineas_validas = []
            for line in file:
                try:
                    campos = line.strip().split("\t")
                    lineas_validas.append(campos)
                except Exception as e:
                    print(f"Error en la línea: {line}")
                    print(f"Detalles del error: {e}")
        df1 = pd.DataFrame(lineas_validas)
        break  # Sal del bucle si la lectura tuvo éxito
    except UnicodeDecodeError:
        continue  # Intente con la siguiente codificación si falla
else:
    print("No se pudo leer el archivo con ninguna codificación compatible.")

######################
print(df1.describe())

