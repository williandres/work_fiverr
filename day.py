import csv

def read_buses(desde,hasta):
    """Funcion que convierte todos las filas de 'telemetria_funcionamiento.csv' en una lista con los id_buses. 
       -buses = list : crea una lista a con todos los id_buses
       
       Argumentos que posteriormente se envian a la funcion buses_day
       -tittles_buses = list, captura los titulos para posteriormente añadir nuevas columnas.
       -desde = int, argumento que determina el incio del rango de los archivos por explorar. 
       -hasta = int, argumento que determina el final del rango de los archivos por explorar.
    
    """
    with open(f"./telemetria_funcionamiento.csv","r", encoding = "utf-8") as f:
        reader = csv.reader(f)
        tittles_buses = next(reader)
        buses = []
        for row in reader:
            buses.append(row)
    print(f'Definiendo buses ({len(buses)})')
    buses_day(buses,tittles_buses,desde,hasta)

def buses_day(buses,tittles_buses,desde,hasta):
    """Funcion encargada de crear una lista 'data' con todas las filas dentro del archivo telemetria por dia(csv)
       posteriormente llama una funcion buses_evaluate()  
        Argumentos que posteriormente se enviaran a buses_evaluate() 
       -tittles_buses = list, captura los titulos para posteriormente añadir nuevas columnas.
       -desde = int, argumento que determina el incio del rango de los archivos por explorar. 
       -hasta = int, argumento que determina el final del rango de los archivos por explorar.
       -buses = list, argumento con la lista de todos los buses
       -data = list, arguemento con la lista de todas las filas del archivo telemetria por dia(csv)
       -i = int, es el indicador del titulo del archivo, que se puede usar como fecha 
    """
    for i in range (desde,hasta+1):
        data = []
        try:
            with open(f"./data/{i}_p60.csv","r", encoding = "utf-8") as f:
                tittles = f.readline().split(",")
                for line in f:
                    data.append(line.split(","))
                buses_evaluate(data,buses,i,tittles_buses)
        except FileNotFoundError:
            pass

def buses_evaluate(data,buses,num,tittles):
    """Funcion encargada de insertar el titulo de segun el dia y si el id_bus ese dia esta : "Sin Registro","Sin datos","Dato irregular" o "Dato correcto";
        -date = str : apartir del argumento 'num' lo convertimos en una fecha con buena estandarizacion.
        -correcto =  int : variable que se actualiza en el caso que el id bus encuentre una linea en 'data' donde el kilometraje sea mayor a 0.
        -total = int : variable que se actualiza en el caso que el id bus encuentre su id en una linea de 'data'.
        Al terminar de construir la lista 'buses' llama a la funcion write_buses() donde escribe la lista en el csv
    """
    date = str(num)[6:]+"-"+str(num)[4:6]+"-"+str(num)[:4]
    tittles.append(date)
    print(f'Construyendo telemetria de la fecha: {date}...')
    for bus in buses:
        correcto = 0
        total = 0
        for line in data: #Bucle donde evalua linea por linea
            if bus[0] == line[3]:
                total += 1
            if bus[0] == line[3] and float(line[9]) > 0:
                correcto += 1
        if correcto == 0 and total == 0: #Condicionales que segun 'correcto' y 'total' insertan el tipo de dato que es
            bus.append("Sin Registro")
        elif correcto == 0 and total > 0:
            bus.append("Sin datos")
        elif correcto <= (90*total)/100:
            bus.append("Dato irregular")
        elif correcto > (90*total)/100:
            bus.append("Dato correcto")
    write_buses(buses,tittles)

def write_buses(buses,tittles):
    """Funcion encargada de escribir los titulos y los buses con la lista ya actualizada en el archivo "telemetria_funcionamiento.csv"
    """
    with open(f"./telemetria_funcionamiento.csv","w", encoding = "utf-8", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(tittles)
        for bus in buses:
            writer.writerow(bus)