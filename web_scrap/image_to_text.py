from google.cloud import documentai_v1 as documentai
import os
import csv

def process_table(path, project_id, location, processor_id, output_path):
    """Process a document using the Document AI API with a Table Processor and save the output to a .txt file"""
    try:
        # Instancia del cliente
        client = documentai.DocumentProcessorServiceClient()

        # Ruta del procesador
        processor_name = client.processor_path(project_id, location, processor_id)

        # Leer la imagen
        with open(path, "rb") as image_file:
            image_content = image_file.read()

        # Crear el documento a procesar
        document = {"content": image_content, "mime_type": "image/png"}  # Cambia el MIME type según el formato de tu imagen

        # Configurar la solicitud
        request = {"name": processor_name, "raw_document": document}

        # Llamar a la API para procesar el documento
        result = client.process_document(request=request)

        document = result.document

        # Abrir el archivo de salida para escribir
        with open(output_path, 'w', encoding='utf-8') as output_file:
            # Extraer y escribir el texto de las tablas en el archivo
            for page in document.pages:
                for table in page.tables:
                    for row in table.body_rows:
                        row_text = []
                        for cell in row.cells:
                            # Obtener los segmentos de texto y concatenarlos
                            for segment in cell.layout.text_anchor.text_segments:
                                start_index = segment.start_index
                                end_index = segment.end_index
                                row_text.append(document.text[start_index:end_index])
                        output_file.write("".join(row_text))
        

        # Manejo de errores específicos de la API
        if result.error.message:
            raise Exception(f"Error: {result.error.message}")

    except Exception as e:
        print(f"...")

def txt_csv(file, num):
    with open(file, 'r', encoding='utf-8') as txt_file:
        lines = txt_file.readlines()
    
    # Eliminar líneas vacías y espacios en blanco
    lines = [line.strip() for line in lines if line.strip()]
    
    rows = [lines[i:i+6] for i in range(0, len(lines), 6)]
    
    # Manejar el caso donde el número de líneas no es múltiplo de 6
    if len(lines) % 6 != 0:
        # Añadir la última fila incompleta
        rows.append(lines[-(len(lines) % 6):])

    res = 'sources/csvs_ia/csv' + str(num) + '.csv'
    with open(res, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(rows)

if __name__ == '__main__':
    # Configura tu proyecto, ubicación y ID del procesador
    project_id = 'strange-mind-423520-h8'
    location = 'us'  # Ejemplo: 'us'
    processor_id = '90a736d085bfb08a'

    # Asegúrate de configurar la variable de entorno GOOGLE_APPLICATION_CREDENTIALS
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "sources/application_default_credentials.json"

    image_files = [f for f in os.listdir('sources/imagenes3') if os.path.isfile(os.path.join('sources/imagenes3', f))]

    for i, image_file in enumerate(image_files):
        image_path = os.path.join('sources/imagenes3', image_file)
        # Procesar la imagen y guardar el resultado en un archivo .txt
        process_table(image_path, project_id, location, processor_id, 'output.txt')
        txt_csv('output.txt',1+i)

