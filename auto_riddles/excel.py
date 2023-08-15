import openpyxl
import csv

matrix = []
with open("riddles/riddles.csv", mode="r", newline="", encoding="utf-8") as archivo:
    lector_csv = csv.reader(archivo)
    next(lector_csv)

    for fila in lector_csv:
        matrix.append(["{","","",""])
        matrix.append(["","'question':'",fila[0],"',"])
        matrix.append(["","'answer':'",fila[1],"',"])
        matrix.append(["},","","",""])


# Crear un nuevo libro de Excel
libro = openpyxl.Workbook()
hoja = libro.active

# Escribir la matriz en la hoja
for fila in matrix:
    hoja.append(fila)

# Guardar el archivo de Excel
nombre_archivo = "matriz.xlsx"
libro.save(nombre_archivo)

