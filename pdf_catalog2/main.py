import PyPDF2
import index_pdf, catalog_pdf, excel

def merge():
    pdf_files = ["sources/assets/portada.pdf", "sources/assets/index.pdf", "sources/assets/catalog.pdf", "sources/assets/contraportada.pdf"]
    pdf_writer = PyPDF2.PdfWriter()

    for pdf_file in pdf_files:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)

    with open("sources/catalogo_productos.pdf", "wb") as output_pdf:
        pdf_writer.write(output_pdf)


if __name__ == '__main__':
    catalog_pdf.main(excel.main())
    index_pdf.main(excel.main())
    merge()



