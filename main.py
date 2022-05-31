import functions as fun

def run():
    #fun.fileCsv()
    data = []
    carro = ""
    with open(f"./data/20220404_p60.csv","r", encoding = "utf-8") as f:
        print("Dia 1")
        tittles = f.readline().split(",")
        for line in f:
            data.append(line.split(","))
        i = 0
        total = 0
        con_kilometraje = 0
        for row in data:
            if data[i][3] == "Z674005":
                total += 1
            if data[i][3] == "Z674005" and float(data[i][9]) != 0:
                x = data[i][3]
                y = data[i][9]
                z = data[i][0]
                print(f'Id vehiculo: {x} Kilometraje: {y} Hora: {z}')
                con_kilometraje += 1
            i += 1
        print(f'Hay un total de registros para el vehiculo "Z674005" de {total} y con kilometraje mayor a cero de {con_kilometraje} ')
    data = []
    with open(f"./data/20220405_p60.csv","r", encoding = "utf-8") as f:
        print("Dia 2")
        tittles = f.readline().split(",")
        for line in f:
            data.append(line.split(","))
        i = 0
        total = 0
        con_kilometraje = 0
        for row in data:
            if data[i][3] == "Z674005":
                total += 1
            if data[i][3] == "Z674005" and float(data[i][9]) != 0:
                x = data[i][3]
                y = data[i][9]
                z = data[i][0]
                print(f'Id vehiculo: {x} Kilometraje: {y} Hora: {z}')
                con_kilometraje += 1
            i += 1
        print(f'Hay un total de registros para el vehiculo "Z674005" de {total} y con kilometraje mayor a cero de {con_kilometraje} ')
    data = []
    with open(f"./data/20220406_p60.csv","r", encoding = "utf-8") as f:
        print("Dia 3")
        tittles = f.readline().split(",")
        for line in f:
            data.append(line.split(","))
        i = 0
        total = 0
        con_kilometraje = 0
        for row in data:
            if data[i][3] == "Z674005":
                total += 1
            if data[i][3] == "Z674005" and float(data[i][9]) != 0:
                x = data[i][3]
                y = data[i][9]
                z = data[i][0]
                print(f'Id vehiculo: {x} Kilometraje: {y} Hora: {z}')
                con_kilometraje += 1
            i += 1
        print(f'Hay un total de registros para el vehiculo "Z674005" de {total} y con kilometraje mayor a cero de {con_kilometraje} ')
    data = []
    with open(f"./data/20220407_p60.csv","r", encoding = "utf-8") as f:
        print("Dia 4")
        tittles = f.readline().split(",")
        for line in f:
            data.append(line.split(","))
        i = 0
        total = 0
        con_kilometraje = 0
        for row in data:
            if data[i][3] == "Z674005":
                total += 1
            if data[i][3] == "Z674005" and float(data[i][9]) != 0:
                x = data[i][3]
                y = data[i][9]
                z = data[i][0]
                print(f'Id vehiculo: {x} Kilometraje: {y} Hora: {z}')
                con_kilometraje += 1
            i += 1
        print(f'Hay un total de registros para el vehiculo "Z674005" de {total} y con kilometraje mayor a cero de {con_kilometraje} ')

if __name__== "__main__":
    run()