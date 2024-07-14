import json
import re
import csv


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

def get_llaves():
    #{Accion Padre: [Hijo 1, Hijo2, Hijo3]}
    illo = {}
    # Leer el archivo CSV
    with open('sources/papis.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for fila in reader:
            llave = fila[0]
            valores = fila[1:]
            illo[llave] = valores
    return illo

def set_saf(dict):
    with open('sources/biches.csv', mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for llave, valores in dict.items():
            writer.writerow([llave] + valores)


def modificar(data):
    acciones_nombre = get_llaves()
    dsd = {}
    for i in data:
        cat = []
        acciones_padre = []
        acciones_hijo = []
        for j,valor in i['Actions'].items():
            if j in list(acciones_nombre.keys()):
                acciones_padre.append(j)
                acciones_hijo.append(acciones_nombre[j])
            if not isinstance(valor, dict) and j not in ["Bonus Actions","Multiattack","Reactions","Legendary Actions","Mythic Actions","Lair Actions","Regional Effects","Environment"]:
                cat.append(j)


        comp = {}
        for x in range(len(acciones_padre)):
            tittle = acciones_padre[x]
            hijos = {}
            for j,valor in i['Actions'].items():
                if j in acciones_hijo[x]:
                    hijos[j] = valor
            comp[tittle] = hijos

        borrar = []
        for x in acciones_hijo:
            for j in x:
                borrar.append(j)
        
        for j,valor in i['Actions'].items():
            if j in acciones_padre:
                dicc = {'Description': valor}
                dicc.update(comp[j])
                i['Actions'][j] = dicc
        for j in borrar:
            valor_eliminado = i['Actions'].pop(j, None)
        
        if len(cat) >= 4:
            dsd[i['Name']] = cat
        
    set_saf(dsd)
    return data


if __name__ == '__main__':
    datos_leidos = leer_archivo_json('sources/Final_Bestiary3.json')
    coso = modificar(datos_leidos)
    crear_archivo_json(coso, 'sources/Final_Bestiary4.json')