import csv

def read_buses():
    with open(f"./telemetria_funcionamiento.csv","r", encoding = "utf-8") as f:
        reader = csv.reader(f)
        tittles = f.readline().split(",")
        buses = []
        for row in reader:
            buses.append(row)
    buses_day(buses)

def buses_day(buses):
    tittles_buses = ['Id_Buses']
    for i in range (20220404, 20220431):
        data = []
        try:
            with open(f"./data/{i}_p60.csv","r", encoding = "utf-8") as f:
                tittles = f.readline().split(",")
                for line in f:
                    data.append(line.split(","))
                buses_evaluate(data,buses,i,tittles)
        except FileNotFoundError:
            pass

def buses_evaluate(data,buses,num,tittles):
    tittles.append(num)
    for bus in buses:
        correcto = 0
        total = 0
        for line in data:
            if bus[0] == line[3]:
                total += 1
            if bus[0] == line[3] and float(line[9]) > 0:
                correcto += 1
        if correcto == 0:
            bus.append("Sin datos")
        elif correcto > (90*total)/100:
            bus.append("Dato correcto")
        elif correcto <= (90*total)/100:
            bus.append("Dato irregular")
    write_buses(buses,tittles)

def write_buses(buses,tittles):
    with open(f"./telemetria_funcionamiento.csv","w", encoding = "utf-8", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(tittles)
        for i in range(0, len(buses)):
            writer.writerow(buses[i])