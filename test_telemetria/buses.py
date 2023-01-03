import csv

def fileCsv(desde,hasta):
    """Funcion que crea o reinicia a 'telemetria_funcionamiento.csv'. 
       Luego envia un numero  determinado entre 'desde' y hasta por medio de un loop a la funcion read_file
       -desde = int, argumento que determina el incio del rango de los archivos por explorar 
       -hasta = int, argumento que determina el final del rango de los archivos por explorar 
    """
    print("Creando o reiniciando datos del archivo 'telemetria_funcionamiento.csv'")
    file = open("./telemetria_funcionamiento.csv", "w")
    file.close()
    print(f'Definiendo los id_buses entre los archivos {desde}_p60.csv y {hasta}_p60.csv')
    for i in range (desde, hasta+1):
        read_file(i)

def read_file(num):
    """ Funcion que lee el archivo de la telemetria de un dia(csv) y lo convierte a una lista.
        - data = list : lista  que contiene toda los valores de un archivo de telemetria por dia(csv)
        -telemetria_id(id_buses(data)) : Luego de crear la lista con sus valores llama a 
         la funcion telemetria_id() que como argumento envia otra funcion id_buses(data)
        -tittles : variable encargada de capturar la primera fila del archivo de la telemetria por dia(csv) "Son datos inutiles"
    """
    data = []
    try:
        with open(f"./data/{num}_p60.csv","r", encoding = "utf-8") as f:
            tittles = f.readline().split(",")
            for line in f:
                data.append(line.split(","))
            telemetria_id(id_buses(data))
    except FileNotFoundError:
        pass

def telemetria_id(buses):
    """ Funcion que escribe todos los buses registrados a partir de la lista de buses retornada por
        la funcion id_buses().
        -Los escribe en el archivo 'telemetria_funcionamiento.csv'
    """
    with open(f"./telemetria_funcionamiento.csv","w", encoding = "utf-8", newline='') as f:
        writer = csv.writer(f)
        tittles = ['Id_Buses']
        writer.writerow(tittles)
        for i in range(0, len(buses)):
            writer.writerow(buses[i])

def id_buses(data):
    """ Funcion que construye un lista con todos los id_buses registrados
        -retorna la lista 'buses' 
        
        -data = list: argumento de la funcion que trae todos los filas del archivo de telemetria por dia (csv) en forma de lista.
        -buses = list: lista creada a partir de los id_buses del archivo "telemetria_funcionamiento.csv".
         en caso de que el archivo este vacio creara una lista vacia a la que instertar los buses
        
        Se crea un bucle que recorre cada lista 'fila' dentro de la lista 'data' insertando el id_bus en la lista 'buses' de menor a mayor
        -count = int : numero que termina la longitud de lista buses; utilizada para enviar como argumento a la funcion add_bus, 
         y para evaluar unas excepciones cuando lista buses esta vacia o con solo un valor 
        -target = int :captura el id_bus de una fila de la lista 'data' y lo convierte en un numero quitandole la 'Z' del id_bus
    """
    with open(f"./telemetria_funcionamiento.csv","r", encoding = "utf-8") as f:
        reader = csv.reader(f)
        tittles = f.readline().split(",")
        buses = []
        for row in reader:
            buses.append(row)

    for row in data:
        try:
            count = len(buses)
            target = int(row[3][1:])
            if count == 0: #Si la lista'buses' esta vacia inserte el primer id que encuentre
                buses.append([row[3]])
            elif count == 1: #Si la lista'buses' esta con un solo valor inserte el id segun si es mayor o menor al valor ya existente
                if target > int(buses[0][0][1:]):
                    buses.insert(1,[row[3]])
                else:
                    buses.insert(0,[row[3]])
            elif add_bus(0,count,target,buses) == False: #Si el id_bus no se encuentra la lista'buses' se debe insertar. 
                for i in range(0,count+1): #Bucle que evalua cada valor en la lista 'buses' 
                    if i == count: #En el caso que el id_bus tenga que poscionarse en la ultima pocision
                        buses.append([row[3]])
                        break
                    elif target < int(buses[i][0][1:]): #Inserta de menor a mayor
                        buses.insert(i,[row[3]])
                        break
        except ValueError:
            pass

    return buses

def add_bus(initial, final, target,buses): 
    """Funcion que retorna valor True o False
       -Retorna True en el caso que el bus por comparar ya se encuentra en lista.
       -Retorna False en el caso que determine que el bus no se encuentra en la lista.
       Los argumentos que recibe esta funcion son para ejecutar una busqueda binaria:
        -initial = int : establece la posicion desde donde se debe buscar el 'target' en la lista 'buses'.
        -final = int :  establece la posicion hasta donde se debe buscar el 'target' en la lista 'buses'.
        -target = int : es el valor numerico del id_bus por buscar en lista.
        -buses = list : lista de los buses registrados
    """
    try:
        if initial > final:
            return False

        middle = (initial + final)//2
        compare = int(buses[middle][0][1:])

        if compare == target:
            return True
        elif compare < target:
            return add_bus(middle + 1, final, target,buses)
        else:
            return add_bus(initial, middle - 1, target,buses)
    except IndexError:
        return False