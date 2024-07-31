import PyPDF2
import os
import sys

def insert_pdf_page(n, origin, added):
    origin_pdf = PyPDF2.PdfReader(origin, 'rb')
    added_pdf = PyPDF2.PdfReader(added, 'rb')

    # Create a new PdfWriter object
    output = PyPDF2.PdfWriter()

    # Add all pages from the original PDF
    for i in range(len(origin_pdf.pages)):
        output.add_page(origin_pdf.pages[i])

    # Insert the pages from the added PDF at the specified position
    for i, page in enumerate(added_pdf.pages):
        output.insert_page(page, n + i)

    # Write the combined PDF to the original file
    with open(origin, 'wb') as f_origin:
        output.write(f_origin)




def main():
    carpeta = "sources/assets/rest"
    for nombre_archivo in os.listdir(carpeta):
        ruta_archivo = os.path.join(carpeta, nombre_archivo)
        while True:
            n = input(f'Ingrese el número de la página donde lo desea añadir [{nombre_archivo}], o "sg" para añadir el siguiente archivo, o "ex" para salir: ')
            if n.isdigit():
                insert_pdf_page(int(n), 'sources/assets/resumen.pdf', ruta_archivo)
                break
            else:
                if n.lower() == 'sg':
                    break
                if n.lower() == 'ex':
                    sys.exit()
                else:
                    print("Por favor, ingrese una opcion valida")

if __name__ == '__main__':
    main()