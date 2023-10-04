import pandas as pd

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv('combined_base.csv')

# Obtener estadísticas descriptivas
resumen_estadistico = df.describe()

# Obtener una vista previa de las primeras filas
vista_previa = df.head()

# Obtener información sobre los tipos de datos y la cantidad de valores no nulos
informacion_datos = df.info()

# Imprimir el resumen
print("Resumen estadístico:")
print(resumen_estadistico)
print("\nVista previa de las primeras filas:")
print(vista_previa)
print("\nInformación de los datos:")
print(informacion_datos)
