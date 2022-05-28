def read_file(num):
    data = []
    try:
        with open(f"./data/test_0{num}_p60.csv","r", encoding = "utf-8") as f:
            tittles = f.readline().split(",")
            for line in f:
                data.append(line.split(","))
        print(data)
    except FileNotFoundError:
        pass

def fileCsv():
    for i in range (265465, 265480):
        read_file(i)
