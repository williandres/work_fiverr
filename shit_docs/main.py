"""
Objetivo: Excel con estas columnas

Name | Address 1 | Address 2 | Birth Date | Medicare | Medicaid
"""
from docx import Document
import pandas as pd
import re
import os

# Crear un DataFrame vacío con las columnas deseadas
df = pd.DataFrame(columns=['Medicare','Medicaid','Nombre', 'Fecha', 'Direccion','Source'])

# Función para extraer el valor después de una cadena de texto
def extraer_valor(linea, cadena_clave):
    if cadena_clave in linea:
        valor = linea.split(cadena_clave)[1].strip()
        return valor
    return ''

datos = []  # Lista para almacenar los datos extraídos
cliente = []
for doc_name in os.listdir('sources/wors/'):
    doc = Document('sources/wors/' + doc_name)

    for paragraph in doc.paragraphs:
        linea = paragraph.text
        # Extraer el número de reclamación
        numero = extraer_valor(linea, 'Claim Number:')
        if numero != '':
            match = re.match(r'(\d+.*?[A-Z])', numero)
            if match:
                primera_parte = match.group(1)
            else:
                primera_parte = 'None'

            # Encontrar la segunda parte después de la primera mayúscula hasta el próximo espacio vacío o el final de la cadena
            restante = re.search(r'[A-Z].*?\s|([A-Z].*$)', numero)
            if restante:
                segunda_parte = restante.group(0).strip()
            else:
                segunda_parte = 'None'
            cliente.append(primera_parte)
            cliente.append(segunda_parte[1:])

        # Extraer el nombre
        nombre = extraer_valor(linea, 'Name:')
        if nombre != '':
            cliente.append(nombre)
        # Extraer la fecha de nacimiento
        fecha = extraer_valor(linea, 'Birth Date:')
        if fecha != '':
            cliente.append(fecha)
        # Extraer la dirección
        direccion = extraer_valor(linea, 'Address:')
        if direccion != '':
            cliente.append(direccion)
        elif len(cliente) == 5:
            datos.append({'Medicare': cliente[0], 'Medicaid': cliente[1],'Nombre': cliente[2], 'Fecha': cliente[3], 'Direccion': cliente[4] + ' ' + linea, 'Source': doc_name})
            cliente = []

# Crear el DataFrame a partir de la lista de datos
df = pd.DataFrame(datos)

# Guardar el DataFrame en un archivo Excel
df.to_excel('sources/fisd.xlsx', index=False)

