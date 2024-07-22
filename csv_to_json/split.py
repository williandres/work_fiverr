import json

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

def modificar(dt):
    pete = []
    incompleted = []
    for i in dt:
        completed = True
        for j,valor in i['Actions'].items():
            if j in ["Bonus Actions","Multiattack","Reactions","Legendary Actions","Mythic Actions","Lair Actions","Regional Effects","Environment"]:
                if isinstance(valor, dict):
                    for m,t in valor.items():
                        if len(m) > 40 or t =="":
                            completed = False
            elif isinstance(valor, dict):
                try:
                    partes = valor['Additional Information'].split('.')
                    for z in partes:
                        if len(z) < 50:
                            completed = False
                    if len(valor['Additional Information']) > 1000:
                        completed = False
                except:
                    pass
            else:
                partes = valor.split('.')
                partes = [elemento for elemento in partes if elemento]
                print(partes)
                for z in partes:
                    if len(z) < 45:
                        completed = False
                if len(valor) > 1000:
                    completed = False


        if completed == True:
            pete.append(i)
        if completed == False:
            incompleted.append(i)

    print(pete)
    return pete, incompleted


if __name__ == '__main__':
    datos_leidos = leer_archivo_json('sources/Final_Bestiary4.json')
    coso, cosa = modificar(datos_leidos)
    crear_archivo_json(coso, 'sources/completed_probably.json')
    crear_archivo_json(cosa, 'sources/issue_probably.json')