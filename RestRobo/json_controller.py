import json
import record_control
from datetime import datetime

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
            "Delay": item[4]
        })

    with open(filepath, 'w') as file:
        json.dump(json_data, file, indent=4)


def validatejson(data):
    valid_cells = []
    invalid_cells = []
    valid_rows = []

    first_column_values = [row[0] for row in data]

    for row_idx, row in enumerate(data):
        row_is_valid = True
        for col_idx, cell in enumerate(row):
            # primera columna
            if col_idx == 0:
                if cell and first_column_values.count(cell) == 1:
                    valid_cells.append((row_idx, col_idx))
                else:
                    invalid_cells.append((row_idx, col_idx))
                    row_is_valid = False
            # quinta columna
            elif col_idx == 4:
                try:
                    value = float(cell)
                    if 0 <= value <= 5:
                        valid_cells.append((row_idx, col_idx))
                    else:
                        invalid_cells.append((row_idx, col_idx))
                        row_is_valid = False
                except ValueError:
                    invalid_cells.append((row_idx, col_idx))
                    row_is_valid = False
            # segunda
            elif col_idx == 1:
                if cell:
                    try:
                        with open(cell, 'r') as file:
                            file_data = json.load(file)
                        if isinstance(file_data, list) and file_data and 'key' in file_data[0] and file_data[0]['key'] == 'RestRobo' and record_control.is_executable_valid(file_data[0]['app']):
                            valid_cells.append((row_idx, col_idx))
                        else:
                            invalid_cells.append((row_idx, col_idx))
                            row_is_valid = False
                    except json.JSONDecodeError:
                        invalid_cells.append((row_idx, col_idx))
                        row_is_valid = False
                    except Exception as e:
                        invalid_cells.append((row_idx, col_idx))
                        row_is_valid = False
                else:
                    invalid_cells.append((row_idx, col_idx))
                    row_is_valid = False
            # tercera
            elif col_idx == 2:
                if record_control.is_executable_valid(cell):
                    valid_cells.append((row_idx, col_idx))
                else:
                    invalid_cells.append((row_idx, col_idx))
                    row_is_valid = False
            # cuarta
            elif col_idx == 3:
                try:
                    datetime.strptime(cell, '%H:%M')
                    valid_cells.append((row_idx, col_idx))
                except ValueError:
                    invalid_cells.append((row_idx, col_idx))
                    row_is_valid = False

        if row_is_valid:
            valid_rows.append(row)

    # Guardar las filas válidas en un archivo JSON
    with open('sources/active_profiles.json', 'w') as json_file:
        json.dump(valid_rows, json_file, indent=4)

    return valid_cells, invalid_cells