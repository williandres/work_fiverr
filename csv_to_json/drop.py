import json

# Leer el JSON desde un archivo
with open('cleaned_data.json', 'r') as file:
    data = json.load(file)

def clean_error_fields(obj):
    if isinstance(obj, dict):
        cleaned = {}
        for k, v in obj.items():
            if v == "ERRER" or v == {}:
                continue
            cleaned[k] = clean_error_fields(v)
        return cleaned
    elif isinstance(obj, list):
        return [clean_error_fields(item) for item in obj if item != {}]
    else:
        return obj

cleaned_data = clean_error_fields(data)

# Guardar los datos limpios en un nuevo archivo
with open('cleaned_data2.json', 'w') as file:
    json.dump(cleaned_data, file, indent=4)

# Imprimir el JSON limpio
print(json.dumps(cleaned_data, indent=4))
