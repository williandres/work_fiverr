import random

# Leer las líneas del archivo
with open("ideas.txt", mode="r", encoding="utf-8") as archivo_txt:
    lineas = archivo_txt.readlines()

# Eliminar líneas duplicadas
lineas_unicas = list(set(lineas))

# Desordenar las líneas únicas
random.shuffle(lineas_unicas)

# Escribir las líneas desordenadas y únicas en un nuevo archivo
with open("ideas_desordenadas.txt", mode="w", encoding="utf-8") as archivo_desordenado:
    archivo_desordenado.writelines(lineas_unicas)

print("Líneas desordenadas y únicas guardadas en 'ideas_desordenadas.txt'")
