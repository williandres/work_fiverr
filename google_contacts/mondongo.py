import os
import shutil

# Directorio donde se encuentra el archivo "privateemail.csv"
private_email_directory = "sources/privateemail.csv"

# Directorio donde se encuentran los archivos CSV originales
input_directory = "sources/contacts_final"

# Iterar a través de los archivos CSV en el directorio de entrada
for csv_file in os.listdir(input_directory):
    if csv_file.endswith(".csv"):
        # Construir la ruta completa al archivo "privateemail.csv"
        private_email_file = private_email_directory

        # Construir la ruta completa al archivo en el directorio de salida
        output_file = os.path.join("sources/emails_duplicate", csv_file)

        # Copiar el contenido de "privateemail.csv" al archivo con el mismo nombre
        shutil.copy(private_email_file, output_file)

print("Archivos duplicados con éxito.")

