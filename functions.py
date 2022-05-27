def upload_file(file):
    data = []
    try:
        with open(f"./data/{file}","r", encoding = "utf-8") as f:
            tittles = f.readline().split(",")
            for line in f:
                data.append(line.split(","))
        return data
    except FileNotFoundError:
        print("Archivo no ha sido encontrado")