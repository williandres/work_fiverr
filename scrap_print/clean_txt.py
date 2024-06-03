import os
import csv
import re

# Directorio que contiene los archivos .txt
input_directory = 'txts'
output_directory = 'csvs'
erase_w = ["Not Available", "—_Not Available"]

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

def remove_unwanted_characters(text):
    return text.replace('‘', '').replace('—', '').replace('_', '')

def process_line(line):
    # Eliminar caracteres no deseados de la línea
    line = remove_unwanted_characters(line)

    # Expresión regular para dividir la línea
    match = re.match(r"^([\w\-\'\s]+?)\s+([\w\-\'\s]+?)\s+(.+?),?\s+([A-Z]{2})\s+(\d{5})\s+(.+)$", line)

    if match:
        first_name = match.group(1).strip()
        last_name = match.group(2).strip()
        street_address = match.group(3).strip()
        city_state = f"{match.group(4)}, {match.group(5)}"
        zip_code = match.group(5)
        phone = match.group(6).strip()

        # Verificar que el teléfono no sea "Not Available"
        if phone not in erase_w:
            return [first_name, last_name, street_address, city_state, zip_code, phone]

    return []

def convert_txt_to_csv(txt_file, csv_file):
    with open(txt_file, 'r', encoding='utf-8') as infile, open(csv_file, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["First Name", "Last Name", "Street Address", "City, State", "ZIP", "Phone"])
        for line in infile:
            processed_line = process_line(line.strip())
            if processed_line:
                writer.writerow(processed_line)

for txt_filename in os.listdir(input_directory):
    if txt_filename.endswith('.txt'):
        txt_file_path = os.path.join(input_directory, txt_filename)
        csv_filename = txt_filename.replace('.txt', '.csv')
        csv_file_path = os.path.join(output_directory, csv_filename)
        convert_txt_to_csv(txt_file_path, csv_file_path)

print("Conversión completada.")
