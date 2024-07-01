import json

def getjsoninfo(filepath):
    data = []

    with open(filepath, 'r') as file:
        json_data = json.load(file)

    for item in json_data:
        data.append([
            item["Name"],
            item["Filename"],
            item["App"],
            item["Hour"],
            item["Delay"]
        ])

    return data

def updatejsoninfo(data,filepath):
    json_data = []

    for item in data:
        json_data.append({
            "Name": item[0],
            "Filename": item[1],
            "App": item[2],
            "Hour": item[3],
            "Delay": item[3]
        })

    with open(filepath, 'w') as file:
        json.dump(json_data, file, indent=4)

def validatejson(data):
    valid_cells = []

    first_column_values = [row[0] for row in data]

    for row_idx, row in enumerate(data):
        for col_idx, cell in enumerate(row):
            # primera columna
            if col_idx == 0:
                if cell and first_column_values.count(cell) == 1:
                    valid_cells.append((row_idx, col_idx))
            # quinta columna
            elif col_idx == 4:
                try:
                    value = float(cell)
                    if 0 <= value <= 5:
                        valid_cells.append((row_idx, col_idx))
                except ValueError:
                    continue
            # Validaciones para la segunda, tercera y cuarta columnas
            elif col_idx == 1:
                pass  # Puedes añadir tu propia lógica de validación aquí y agregar a valid_cells si es válida
            elif col_idx == 2:
                pass  # Puedes añadir tu propia lógica de validación aquí y agregar a valid_cells si es válida
            elif col_idx == 3:
                pass  # Puedes añadir tu propia lógica de validación aquí y agregar a valid_cells si es válida

    return valid_cells