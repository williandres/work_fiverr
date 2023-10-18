import pandas as pd

# Especifica la ruta de tu archivo CSV
archivo_csv = "sources/sampleData_main.csv"
df1 = pd.read_csv(archivo_csv, sep="\t", quoting=3)

print(df1.head(100))

