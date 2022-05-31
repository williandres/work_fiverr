import csv

def fileCsv():
    for i in range (20220404, 20220431):
        read_file(i)

def read_file(num):
    data = []
    try:
        with open(f"./data/{num}_p60.csv","r", encoding = "utf-8") as f:
            tittles = f.readline().split(",")
            for line in f:
                data.append(line.split(","))
            print(f"----{num}-----")
            print(id_buses(data))
    except FileNotFoundError:
        pass

def id_buses(data):
    buses = []
    for row in data:
        cantidad = len(buses)
        target = int(row[3][1:])
        if cantidad == 0:
            buses.append(row[3])
        elif added_bus(0,cantidad,target,buses) == False:
            for i in range(0,cantidad):
                if target < int(buses[i][1:]):
                    buses.insert(i,row[3])
                    break
    return buses

def added_bus(initial, final, target,buses): # Binary Search
    try:
        if initial > final or len(buses) == 1:
            return False
        middle = (initial + final)//2
        compared = int(buses[middle][1:])
        if compared == target:
            return True
        elif compared < target:
            return added_bus(middle + 1, final, target,buses)
        else:
            return added_bus(initial, middle - 1, target,buses)
    except IndexError:
        return False
