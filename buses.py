import csv

def fileCsv(desde,hasta):
    print("Creando o reiniciando datos del archivo 'telemetria_funcionamiento.csv'")
    file = open("./telemetria_funcionamiento.csv", "w")
    file.close()
    print(f'Definiendo los id_buses entre los archivos {desde}_p60.csv y {hasta}_p60.csv')
    for i in range (desde, hasta+1):
        read_file(i)

def read_file(num):
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
    with open(f"./telemetria_funcionamiento.csv","w", encoding = "utf-8", newline='') as f:
        writer = csv.writer(f)
        tittles = ['Id_Buses']
        writer.writerow(tittles)
        for i in range(0, len(buses)):
            writer.writerow(buses[i])

def id_buses(data):
    with open(f"./telemetria_funcionamiento.csv","r", encoding = "utf-8") as f:
        reader = csv.reader(f)
        tittles = f.readline().split(",")
        buses = []
        for row in reader:
            buses.append(row)

    for row in data:
        try:
            cantidad = len(buses)
            target = int(row[3][1:])
            if cantidad == 0:
                buses.append([row[3]])
            elif added_bus(0,cantidad,target,buses) == False:
                if cantidad == 1:
                    if target > int(buses[0][0][1:]):
                        buses.insert(1,[row[3]])
                    else:
                        buses.insert(0,[row[3]])
                if cantidad > 1:
                    for i in range(0,cantidad+1):
                        if i == cantidad:
                            buses.append([row[3]])
                            break
                        if target < int(buses[i][0][1:]):
                            buses.insert(i,[row[3]])
                            break
        except ValueError:
            pass

    return buses

def added_bus(initial, final, target,buses): # Binary Search
    try:
        if initial > final or len(buses) == 1:
            return False

        middle = (initial + final)//2
        comparar = int(buses[middle][0][1:])

        if comparar == target:
            return True
        elif comparar < target:
            return added_bus(middle + 1, final, target,buses)
        else:
            return added_bus(initial, middle - 1, target,buses)
    except IndexError:
        return False