import PyPDF2
import pandas as pd
import re
import os
import time

# Crear un DataFrame vacío con las columnas deseadas
df = pd.DataFrame(columns=['Medicare', 'Medicaid', 'Nombre', 'Fecha', 'Direccion', 'Source'])

# Función para extraer el valor después de una cadena de texto
def extraer_valor(linea, cadena_clave):
    if cadena_clave in linea:
        valor = linea.split(cadena_clave)[1].strip()
        return valor
    return 'y'

def extraer_valor_fecha(linea, cadena_clave):
    if cadena_clave in linea:
        valor = linea.split(cadena_clave)[1].strip()
        return valor
    return 'x'

def extraer_texto_de_pdf(ruta_archivo):
    with open(ruta_archivo, 'rb') as archivo_pdf:
        lector = PyPDF2.PdfReader(archivo_pdf)
        num_paginas = len(lector.pages)
        texto_completo = ''

        for pagina in range(num_paginas):
            pagina_obj = lector.pages[pagina]
            texto_completo += pagina_obj.extract_text()

    return texto_completo

datos = []
cliente = []

# Iterar sobre los archivos PDF en el directorio
for doc_name in os.listdir('sources/pdfs/'):
    doc_path = os.path.join('sources/pdfs/', doc_name)
    texto = extraer_texto_de_pdf(doc_path)
    lineas = texto.split('\n')

    for linea in lineas:
        # Extraer el número de reclamación
        numero = extraer_valor(linea, 'Claim Number:')
        if numero != 'y':
            match = re.match(r'(\d+.*?\[A-Z\])', numero)
            if match:
                primera_parte = match.group(1)
            else:
                primera_parte = numero
            restante = re.search(r'\[A-Z\].*?\s|(\[A-Z\].*$)', numero)
            if restante:
                segunda_parte = restante.group(0).strip()
            else:
                segunda_parte = numero[10:]
            cliente.append(primera_parte)
            cliente.append(segunda_parte[1:])

        # Extraer el nombre
        nombre = extraer_valor(linea, 'Name:')
        if nombre != 'y':
            cliente.append(nombre)

        # Extraer la fecha de nacimiento
        fecha = extraer_valor(linea, 'Birth Date:')
        if fecha != 'y':
            cliente.append(fecha)

        # Extraer la dirección
        direccion = extraer_valor_fecha(linea, 'Address:')
        if direccion != 'x':
            cliente.append(direccion)
        elif len(cliente) >= 5:
            datos.append({'Medicare': cliente[0], 'Medicaid': cliente[1], 'Nombre': cliente[2], 'Fecha': cliente[3],
                          'Direccion': cliente[4] + ' ' + linea, 'Source': doc_name})
            cliente = []

# Crear el DataFrame a partir de la lista de datos
df = pd.DataFrame(datos)
# Guardar el DataFrame en un archivo Excel
df.to_excel('sources/fisd.xlsx', index=False)