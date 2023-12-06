import PyPDF2

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




def options():
    while True:
        origin = input("Ingrese la dirección del archivo que desea modificar: ")
        added = input("Ingrese la dirección del archivo que desea añadir: ")
        n = input("Ingrese el número de la página donde lo desea añadir (se agruegara el contenido en la siguiente pagina): ")
        if n.isdigit():
            insert_pdf_page(int(n), origin, added)
            break
        else:
            print("Por favor, ingrese un número válido.")

def main():
    while True:
        n = input("Ingrese el número de la página donde lo desea añadir (se agruegara el contenido en la siguiente pagina): ")
        if n.isdigit():
            insert_pdf_page(int(n), 'sources/catalogo_productos.pdf', 'sources/assets/rest.pdf')
            break
        else:
            if n.lower() == 'god':
                options()
                break
            else:
                print("Por favor, ingrese un número válido o 'god'.")

if __name__ == '__main__':
    main()
 