import openpyxl

matrix = []
with open("ideas.txt", mode="r", encoding="utf-8") as archivo_ideas:
    ideas = archivo_ideas.read().splitlines()

    for fila in ideas:
        matrix.append([f"'{fila}',"])


# Crear un nuevo libro de Excel
libro = openpyxl.Workbook()
hoja = libro.active

# Escribir la matriz en la hoja
for fila in matrix:
    hoja.append(fila)

# Guardar el archivo de Excel
nombre_archivo = "positive_thoughts.xlsx"
libro.save(nombre_archivo)

