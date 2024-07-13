import json
import re
from collections import Counter

def process_first_string(s):
    # Eliminar 'plus'
    s = s.replace('plus', '')
    # Extraer números
    numbers = re.findall(r'\d+', s)
    # Eliminar los números de la cadena original
    s = re.sub(r'\d+', '', s).strip()
    return s, numbers

def process_second_string(s):
    # Extraer patrones específicos
    patterns = re.findall(r'\d+[a-zA-Z]\d+', s)
    # Eliminar patrones de la cadena original
    for pattern in patterns:
        s = s.replace(pattern, '')
    # Usar strip() para limpiar la cadena
    s = s.strip()
    return s, patterns

def dividir_cadena(dg,dt):
    # Dividir por 'and' y 'or'
    partes = re.split(r'\band\b|\bor\b', dt)

    # Dividir cada parte por '(' y procesar las subpartes
    resultado_dt = []
    resultado_dg = [] 
    for parte in partes:
        subpartes = parte.split('(')
        for subparte in subpartes:
            subparte = subparte.strip().strip(',')  # Eliminar comas al principio y al final y aplicar strip()
            if subparte:  # Evitar agregar cadenas vacías
                resultado_dt.append(subparte)

    resultado_dg.append(dg)

    if len(resultado_dt) > 1:
        cadena1_procesada, numeros_cadena1 = process_first_string(resultado_dt[0])
        cadena2_procesada, patrones_cadena2 = process_second_string(resultado_dt[1])

        resultado_dt[0] = cadena1_procesada
        resultado_dt[1] = cadena2_procesada
        try:
            resultado_dg.append(str(numeros_cadena1[0]) + ' ' + '(' + str(patrones_cadena2[0]) + ')')
        except:
            pass



    return [resultado_dg,resultado_dt]

def crear_archivo_json(datos, nombre_archivo):
    """
    Crea un archivo JSON con los datos proporcionados.

    :param datos: Diccionario con los datos a guardar en el archivo JSON.
    :param nombre_archivo: Nombre del archivo JSON a crear.
    """
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=4)

def leer_archivo_json(nombre_archivo):
    """
    Lee un archivo JSON y devuelve los datos como un diccionario.

    :param nombre_archivo: Nombre del archivo JSON a leer.
    :return: Diccionario con los datos leídos del archivo JSON.
    """
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        datos = json.load(archivo)
    return datos

def eliminar_nones(dic):
    if isinstance(dic, dict):
        return {k: eliminar_nones(v) for k, v in dic.items() if v is not None}
    elif isinstance(dic, list):
        return [eliminar_nones(i) for i in dic]
    else:
        return dic


def modificar(data):
    final = []
    for i in data:
        for j,valor in i['Actions'].items():
            final.append(j)
            if isinstance(valor, dict):
                if 'Damage Type' in valor:
                    dt = valor['Damage Type']
                    if dt == '':
                        valor['Damage Type'] = 'None'
                    else:
                        illo = dividir_cadena(valor['Damage'],dt)
                        valor['Damage'] = illo[0]
                        valor['Damage Type'] = illo[1]
    
    #$#
    conteo_cadenas = Counter(final)

    conteo_ordenado = sorted(conteo_cadenas.items(), key=lambda item: item[1], reverse=True)

    # Crear el archivo .txt y escribir el resumen
    with open("sources/summary_actions.txt", "w") as archivo:
        for cadena, conteo in conteo_ordenado:
            archivo.write(f"{cadena}: {conteo}\n")
    return data

if __name__ == '__main__':
    datos_leidos = leer_archivo_json('sources/Final_Bestiary.json')
    coso = modificar(datos_leidos)
    mierda = eliminar_nones(coso)
    crear_archivo_json(coso, 'sources/Final_Bestiary3.json')




